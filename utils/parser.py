from collections import OrderedDict
from os import listdir, path
from datetime import datetime
import xmltodict
from typing import Optional


class FileParser(object):
    def __init__(self, storage_path):
        self.storage_path: str = storage_path

    def get_content(self, filename: str) -> OrderedDict:
        """Parse xml file to OrderedDict object
        :param filename: file name with flights xml data
        :return: OrderedDict file content
        """
        file_path: str = path.join(self.storage_path, filename)

        with open(file_path, 'rb') as raw_file:
            content: OrderedDict = xmltodict.parse(raw_file)

        return content

    def parse_product(self, raw_product: dict) -> dict:
        """parse flights product
        :param raw_product: raw flights object
        :return: formatted object
        """
        pricing: dict = raw_product.get('Pricing', {})
        pricing = self.parse_price(price=pricing)
        raw_flights: list = raw_product.get('OnwardPricedItinerary', {}).get('Flights', {}).get('Flight', [])

        if isinstance(raw_flights, dict):
            raw_flights = [raw_flights]

        return_flights: list = raw_product.get('ReturnPricedItinerary', {}).get('Flights', {}).get('Flight', [])

        if isinstance(return_flights, dict):
            return_flights = [return_flights]

        flights = [self.parse_flight(flight) for flight in raw_flights]
        return_flights = [self.parse_flight(flight, flight_type='return') for flight in return_flights]
        origin: str = flights[0].get('origin')
        destination: str = flights[-1].get('destination')
        departure_date: datetime = flights[0].get('departure_date')
        return_date: Optional[datetime] = None

        if return_flights:
            return_date = return_flights[0].get('departure_date')

        flights += return_flights
        airlines: list = []
        flight_classes: list = []
        total_duration: int = 0

        for flight in flights:
            carrier_id: str = flight.get('carrier', {}).get('id')
            flight_class: str = flight.get('flight_class')
            total_duration += flight.get('duration')

            if carrier_id not in airlines:
                airlines.append(carrier_id)

            if flight_class and flight_class not in flight_classes:
                flight_classes.append(flight_class)

        formatted_product: dict = {
            'type': 'round' if return_flights else 'oneway',
            'prices': pricing.get('prices'),
            'price_currency': pricing.get('currency'),
            'total_price': pricing.get('total'),
            'adults': pricing.get('adults'),
            'childs': pricing.get('childs'),
            'infants': pricing.get('infants'),
            'airlines': airlines,
            'total_duration': total_duration,
            'origin': origin,
            'destination': destination,
            'departure_date': departure_date,
            'return_date': return_date,
            'flight_classes': flight_classes,
            'flights': flights,
        }

        return formatted_product

    @staticmethod
    def parse_flight(raw_flight: dict, flight_type: str = 'onward') -> dict:
        """parse flight object
        :param raw_flight: raw flight data
        :param flight_type: flight direction
        :return: formatted flight object
        """
        carrier: dict = raw_flight.get('Carrier', {})
        departure_date: datetime = datetime.strptime(raw_flight.get('DepartureTimeStamp'), '%Y-%m-%dT%H%M')
        arrival_date: datetime = datetime.strptime(raw_flight.get('ArrivalTimeStamp'), '%Y-%m-%dT%H%M')
        duration: int = (arrival_date - departure_date).seconds
        formatted_flight: dict = {
            'type': flight_type,
            'carrier': {
                'id': carrier.get('@id'),
                'name': carrier.get('#text')
            },
            'flight_number': int(raw_flight.get('FlightNumber')),
            'origin': raw_flight.get('Source'),
            'destination': raw_flight.get('Destination'),
            'departure_date': departure_date,
            'arrival_date': arrival_date,
            'flight_class': raw_flight.get('Class'),
            'stops': int(raw_flight.get('NumberOfStops')),
            'fare_basis': raw_flight.get('FareBasis'),
            'warning_text': raw_flight.get('WarningText'),
            'ticket_type': raw_flight.get('TicketType'),
            'duration': duration
        }

        return formatted_flight

    @staticmethod
    def parse_price(price) -> dict:
        """parse price object
        :param price: raw parse object
        :return: formatted price object
        """
        formatted_price: dict = {'total': 0, 'currency': price.get('@currency'), 'prices': []}
        service_charges: list = price.get('ServiceCharges', [])
        adults: int = 0
        childs: int = 0
        infants: int = 0

        for service_charge in service_charges:
            price_type: str = service_charge.get('@type', '')
            charge_type: str = service_charge.get('@ChargeType', '')
            price: float = float(service_charge.get('#text', ''))

            if charge_type == 'TotalAmount':
                formatted_price['total'] += price

            if price_type == 'SingleAdult':
                adults = 1

            if price_type == 'SingleChild':
                childs = 1

            if price_type == 'SingleInfant':
                infants = 1

            formatted_price['prices'].append({
                'price_type': price_type,
                'charge_type': charge_type,
                'price': price,
            })

        formatted_price['adults'] = adults
        formatted_price['childs'] = childs
        formatted_price['infants'] = infants

        return formatted_price

    def parse_file(self, filename: str) -> dict:
        """full parse file with xml data
        :param filename: file name with xml data in storage
        :return: formatted data
        """
        product_types: list = []
        origins: list = []
        destinations: list = []
        departure_dates: list = []
        return_dates: list = []
        adults: int = 0
        childs: int = 0
        infants: int = 0
        flight_classes: list = []
        airlines: list = []

        file_content = self.get_content(filename=filename)
        raw_products: list = file_content.get('AirFareSearchResponse', {}).get('PricedItineraries', {}).get('Flights',
                                                                                                            [])
        formatted_products: list = []

        for raw_product in raw_products:
            formatted_product: dict = self.parse_product(raw_product=raw_product)
            formatted_products.append(formatted_product)
            product_types.append(formatted_product.get('type'))
            origins.append(formatted_product.get('origin'))
            destinations.append(formatted_product.get('destination'))
            departure_dates.append(formatted_product.get('departure_date').strftime('%Y-%m-%d'))

            if formatted_product.get('return_date'):
                return_dates.append(formatted_product.get('return_date').strftime('%Y-%m-%d'))

            if formatted_product.get('adults') > adults:
                adults = formatted_product.get('adults')

            if formatted_product.get('childs') > childs:
                childs = formatted_product.get('childs')

            if formatted_product.get('infants') > infants:
                infants = formatted_product.get('infants')

            flight_classes += formatted_product.get('flight_classes')
            airlines += formatted_product.get('airlines')

        parsed_data: dict = {
            'types': set(product_types),
            'origins': set(origins),
            'destinations': set(destinations),
            'departure_dates': set(departure_dates),
            'return_dates': set(return_dates),
            'adults': adults,
            'childs': childs,
            'infants': infants,
            'flight_classes': set(flight_classes),
            'airlines': set(airlines),
            'products': formatted_products,
        }

        return parsed_data

    def parse_storage(self) -> dict:
        """get formatted objects from all files
        :return:
        """
        filenames: list = listdir(path=self.storage_path)
        result = {filename: self.parse_file(filename) for filename in filenames}

        return result
