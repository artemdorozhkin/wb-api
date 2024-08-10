# WB API Продавца SDK Python Library

Клиент для работы по [WB API Продавца](https://openapi.wildberries.ru/)

#### [Требования](#требования-1)

#### [Установка](#установка-1)

#### [Начало работы](#начало-работы-1)

#### [Примеры использования SDK](#примеры-использования-sdk-1)

- [Получение статистики](#получение-статистики)
  - [Поставки](#поставки)
  - [Остатки](#остатки)
  - [Заказы](#заказы)
  - [Продажи](#продажи)
  - [Отчет о продажах по реализации](#отчет-о-продажах-по-реализации)

## Требования

1. Python >= 3.8
2. pip

## Установка

1. Установите pip.
2. В консоли выполните команду

```bash
pip install --upgrade wb-api-sdk
```

## Начало работы

1. Импортируйте класс `WBApi` из модуля `wb_api`

```python
from wb_api import WBApi
```

2. Установите API_TOKEN для авторизации

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")
```

3. Вызовите нужный метод API. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/)

## Примеры использования SDK

### Получение статистики

1. Получить статистику по Поставкам, Остаткам, Заказам, Продажам и Отчет о продажах по реализации можно вызвав методы свойства `statistics`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

stats = api.statistics
```

#### Поставки

1. Для получения статистики по поставкам за период, воспользуйтесь методом `get_incomes`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

stats = api.statistics
incomes = stats.get_incomes(date_from="2024-07-31")
```

2. Метод возвращает список объектов `Income`

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/statistics/api/ru/#tag/Statistika/paths/~1api~1v1~1supplier~1incomes/get)

#### Остатки

1. Для получения статистики по остаткам товаров на складах WB, воспользуйтесь методом `get_stocks`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

stats = api.statistics
stocks = stats.get_stocks(date_from="2024-07-31")
```

2. Метод возвращает список объектов `Stock`

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/statistics/api/ru/#tag/Statistika/paths/~1api~1v1~1supplier~1stocks/get)

#### Заказы

1. Для получения статистики по заказам, воспользуйтесь методом `get_orders`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

stats = api.statistics
orders = stats.get_orders(date_from="2024-07-31")
```

2. Метод возвращает список объектов `Order`

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/statistics/api/ru/#tag/Statistika/paths/~1api~1v1~1supplier~1orders/get)

#### Продажи

1. Для получения статистики по продажам, воспользуйтесь методом `get_sales`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

stats = api.statistics
sales = stats.get_sales(date_from="2024-07-31")
```

2. Метод возвращает список объектов `Sale`

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/statistics/api/ru/#tag/Statistika/paths/~1api~1v1~1supplier~1sales/get)

#### Отчет о продажах по реализации

1. Для получения отчета о продажах по реализации, воспользуйтесь методом `get_realization_reports`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

stats = api.statistics
realization_reports = stats.get_realization_reports(date_from="2024-08-05", date_to="2024-08-06")
```

2. Метод возвращает список объектов `Sale`

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/statistics/api/ru/#tag/Statistika/paths/~1api~1v5~1supplier~1reportDetailByPeriod/get)

### Работа с контентом [в разработке]

1. Начать работу с API контента можно вызвав методы свойства `content`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

content = api.content
```

#### Категории

1. Для получения списка всех родительских категорий товаров, воспользуйтесь методом `get_all_parents`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

content = api.content
parents = content.get_all_parents()
```

2. Метод возвращает список объектов `Parent`

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/content/api/ru/#tag/Konfigurator/paths/~1content~1v2~1object~1parent~1all/get)

#### Предметы

1. Для получения списка всех всех доступных предметов, родительских категорий предметов, и их идентификаторов, воспользуйтесь методом `get_all_subjects`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

content = api.content
subjects = content.get_all_subjects()
```

2. Метод возвращает список объектов `Subject`

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/content/api/ru/#tag/Konfigurator/paths/~1content~1v2~1object~1all/get)
