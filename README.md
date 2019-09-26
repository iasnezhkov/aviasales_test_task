# Aviasales test task


### Как запустить сервис

#### Зависимости

* python 3.7
* postgres

#### Настройки

> настройки находятся в config.py

* указать путь к базе данных postgres `SQLALCHEMY_DATABASE_URI`

#### Заполнение базы
* экпортировать путь к приложению: `export FLASK_APP=autoapp.py`
* обновить бд: `flask db upgrate`
* заполнить данные: `flask populate`

#### Запуска сервиса
* экпортировать путь к приложению: `export FLASK_APP=autoapp.py`
* запустить сервис: `flask run`
> сервис будет доступен на 127.0.0.1:5000


#### Запросы

* Какие варианты перелёта из DXB в BKK мы получили?

Для получения вариантов полета нужно сделать запрос с заданными точками

GET `http://127.0.0.1:5000/api/v1/product/?origin=DXB&destination=BKK`

По умолчанию будут возвращены `oneway` билеты, для `round` билетов нужно сделать следующий запрос:

GET `http://127.0.0.1:5000/api/v1/product/?origin=DXB&destination=BKK&flight_type=round`

* Самый дорогой/дешёвый, быстрый/долгий и оптимальный варианты

GET `http://127.0.0.1:5000/api/v1/product/?origin=DXB&destination=BKK&flight_type=oneway&sort=total_price`

Варианты параметра `sort`: `total_price` - по цене, `total_duration` - по длительности, `optimal` - оптимальные.
Если параметр сортировки начинается с `-` то сортировка будет по убыванию.

* В чём отличия между результатами двух запросов (изменение маршрутов/условий)?

GET `http://127.0.0.1:5000/api/v1/search/diff?first_search_id=1&second_search_id=2`

Для того чтобы узнать идентификаторы поиска, нужно сделать запрос

GET `http://127.0.0.1:5000/api/v1/search`