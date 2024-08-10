# WB API Продавца SDK Python Library

Клиент для работы по [WB API Продавца](https://openapi.wildberries.ru/)

#### [Требования](#требования-1)

#### [Установка](#установка-1)

#### [Начало работы](#начало-работы-1)

#### [Примеры использования SDK](#примеры-использования-sdk-1)

- [API статистики](#получение-статистики)
  - [Поставки](#поставки)
  - [Остатки](#остатки)
  - [Заказы](#заказы)
  - [Продажи](#продажи)
  - [Отчет о продажах по реализации](#отчет-о-продажах-по-реализации)
- [API Контента](#api-контента-в-разработке)
  - [Категории](#категории)
  - [Предметы](#предметы)
  - [Характеристики предмета](#характеристики-предмета)
  - [Цвет](#цвет)
  - [Пол](#пол)
  - [Сезон](#сезон)
  - [ТВЭД](#тнвэд)
  - [Ставка НДС](#ставка-ндс)

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

### API статистики

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

### API Контента [в разработке]

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

#### Характеристики предмета

1. Для получения списка характеристик предмета, воспользуйтесь методом `get_charcs`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

content = api.content
charcs = content.get_charcs(subject_id=1)
```

2. Метод возвращает список объектов `Charc`

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/content/api/ru/#tag/Konfigurator/paths/~1content~1v2~1object~1charcs~1%7BsubjectId%7D/get)

#### Цвет

1. Для получения списка значений характеристики Цвет, воспользуйтесь методом `get_colors`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

content = api.content
colors = content.get_colors()
```

2. Метод возвращает список объектов `Color`

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/content/api/ru/#tag/Konfigurator/paths/~1content~1v2~1directory~1colors/get)

#### Пол

1. Для получения списка значений характеристики Пол, воспользуйтесь методом `get_kinds`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

content = api.content
kinds = content.get_kinds()
```

2. Метод возвращает список строк

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/content/api/ru/#tag/Konfigurator/paths/~1content~1v2~1directory~1kinds/get)

#### Страна Производства

1. Для получения списка значений характеристики Страна Производства, воспользуйтесь методом `get_countries`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

content = api.content
countries = content.get_countries()
```

2. Метод возвращает список объектов `Country`

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/content/api/ru/#tag/Konfigurator/paths/~1content~1v2~1directory~1countries/get)

#### Сезон

1. Для получения списка значений характеристики Сезон, воспользуйтесь методом `get_seasons`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

content = api.content
seasons = content.get_seasons()
```

2. Метод возвращает список строк

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/content/api/ru/#tag/Konfigurator/paths/~1content~1v2~1directory~1seasons/get)

#### ТНВЭД

1. Для получения списка ТНВЭД кодов, воспользуйтесь методом `get_tnved`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

content = api.content
tnved_list = content.get_tnved()
```

2. Метод возвращает список объектов `TNVED`

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/content/api/ru/#tag/Konfigurator/paths/~1content~1v2~1directory~1tnved/get)

#### Ставка НДС

1. Для получения списка значений характеристики Ставка НДС, воспользуйтесь методом `get_vat` или `get_nds`

```python
from wb_api import WBApi

api = WBApi(api_key="<API_TOKEN>")

content = api.content
vat_list = content.get_vat()
nds_list = content.get_nds()
```

2. Метод возвращает список строк

3. [Подробнее в документации к WB API Продавца](https://openapi.wildberries.ru/content/api/ru/#tag/Konfigurator/paths/~1content~1v2~1directory~1vat/get)
