from typing import Any, Dict, List, Optional

import requests

from wb_api.client import WBApi
from wb_api.exceptions import (
    ToManyRequests,
    TokenIsMalformed,
    TokenIsNotApplicable,
    TokenNotFound,
    TokenIsMissing,
)
from wb_api.schemas.statistics import (
    Income,
    Incomes,
    Order,
    Orders,
    Sale,
    Sales,
    Stock,
    Stocks,
)
from wb_api.schemas.statistics.realization_report import (
    RealizationReport,
    RealizationReports,
)
from wb_api.utils import validate_date


class Statistics:
    def __init__(self, wb_api: WBApi) -> None:
        self.api_key = wb_api.api_key
        self.base_url = (
            "https://statistics-api-sanbox.wildberries.ru/api/{api_vers}/supplier"
            if wb_api.test_mode
            else "https://statistics-api.wildberries.ru/api/{api_vers}/supplier"
        )

    def get_incomes(self, date_from: str) -> List[Income]:
        """
        Поставки.
            Максимум 1 запрос в минуту

        Args:
            date_from (str):
                Дата и время последнего изменения по поставке.
                Дата в формате RFC3339. Можно передать дату или дату со временем. Время можно указывать с точностью до секунд или миллисекунд.
                Время передаётся в часовом поясе Мск (UTC+3).
                Примеры:
                "2019-06-20"
                "2019-06-20T23:59:59"
                "2019-06-20T00:00:00.12345"
                "2017-03-25T00:00:00"

        Returns:
            List[Income]: Список поставок.
        """
        data = self.__get_data("incomes", date_from)
        return Incomes(incomes=data).incomes

    def get_stocks(self, date_from: str) -> List[Stock]:
        """
        Остатки товаров на складах WB.
            Данные обновляются раз в 30 минут.
            Сервис статистики не хранит историю остатков товаров, поэтому получить данные о них можно только в режиме "на текущий момент".
            Максимум 1 запрос в минуту

        Args:
            date_from (str):
                Дата и время последнего изменения по товару.
                Для получения полного остатка следует указывать максимально раннее значение.
                Например, "2019-06-20"
                Дата в формате RFC3339. Можно передать дату или дату со временем. Время можно указывать с точностью до секунд или миллисекунд.
                Время передаётся в часовом поясе Мск (UTC+3).
                Примеры:
                "2019-06-20"
                "2019-06-20T23:59:59"
                "2019-06-20T00:00:00.12345"
                "2017-03-25T00:00:00"

        Returns:
            List[Stock]: Список остатков товаров.
        """
        data = self.__get_data("stocks", date_from)
        return Stocks(stocks=data).stocks

    def get_orders(self, date_from: str, flag: Optional[int] = 0) -> List[Order]:
        """
        Заказы.
            Гарантируется хранение данных не более 90 дней от даты заказа.
            Данные обновляются раз в 30 минут.
            Для идентификации заказа следует использовать поле srid.
            1 строка = 1 заказ = 1 единица товара.
            Максимум 1 запрос в минуту

        Args:
            date_from (str):
                Дата и время последнего изменения по заказу.
                Дата в формате RFC3339. Можно передать дату или дату со временем. Время можно указывать с точностью до секунд или миллисекунд.
                Время передаётся в часовом поясе Мск (UTC+3).
                Примеры:
                "2019-06-20"
                "2019-06-20T23:59:59"
                "2019-06-20T00:00:00.12345"
                "2017-03-25T00:00:00"
            flag (Optional[int], optional): Defaults to 0.

                Если параметр flag=0 (или не указан в строке запроса), при вызове API возвращаются данные, у которых значение поля lastChangeDate (дата время обновления информации в сервисе) больше или равно переданному значению параметра dateFrom. При этом количество возвращенных строк данных варьируется в интервале от 0 до примерно 100 000.

                Если параметр flag=1, то будет выгружена информация обо всех заказах или продажах с датой, равной переданному параметру dateFrom (в данном случае время в дате значения не имеет). При этом количество возвращенных строк данных будет равно количеству всех заказов или продаж, сделанных в указанную дату, переданную в параметре dateFrom.

        Returns:
            List[Order]: Список заказов.
        """
        data = self.__get_data("orders", date_from, flag)
        return Orders(orders=data).orders

    def get_sales(self, date_from: str, flag: Optional[int] = 0) -> List[Sale]:
        """
        Продажи и возвраты.
            Гарантируется хранение данных не более 90 дней от даты продажи.
            Данные обновляются раз в 30 минут.
            Для идентификации заказа следует использовать поле srid.
            1 строка = 1 продажа/возврат = 1 единица товара.
            Максимум 1 запрос в минуту

        Args:
            date_from (str):
                Дата и время последнего изменения по заказу.
                Дата в формате RFC3339. Можно передать дату или дату со временем. Время можно указывать с точностью до секунд или миллисекунд.
                Время передаётся в часовом поясе Мск (UTC+3).
                Примеры:
                "2019-06-20"
                "2019-06-20T23:59:59"
                "2019-06-20T00:00:00.12345"
                "2017-03-25T00:00:00"
            flag (Optional[int], optional): Defaults to 0.

                Если параметр flag=0 (или не указан в строке запроса), при вызове API возвращаются данные, у которых значение поля lastChangeDate (дата время обновления информации в сервисе) больше или равно переданному значению параметра dateFrom. При этом количество возвращенных строк данных варьируется в интервале от 0 до примерно 100 000.

                Если параметр flag=1, то будет выгружена информация обо всех заказах или продажах с датой, равной переданному параметру dateFrom (в данном случае время в дате значения не имеет). При этом количество возвращенных строк данных будет равно количеству всех заказов или продаж, сделанных в указанную дату, переданную в параметре dateFrom.

        Returns:
            List[Sale]: Список продаж и возвратов.
        """
        data = self.__get_data("sales", date_from, flag)
        return Sales(sales=data).sales

    def get_realization_reports(
        self,
        date_from: str,
        date_to: str,
        rrdid: Optional[int],
        limit: Optional[int] = 100_000,
    ) -> List[RealizationReport]:
        """
        Детализация к еженедельному отчёту реализации.
            В отчёте доступны данные за последние 3 месяца. Максимум 1 запрос в минуту.
            Если нет данных за указанный период, метод вернет null.
            Технический перерыв в работе метода: каждый понедельник с 3:00 до 16:00.

        Args:
            date_from (str):
                Дата и время последнего изменения по заказу.
                Дата в формате RFC3339. Можно передать дату или дату со временем. Время можно указывать с точностью до секунд или миллисекунд.
                Время передаётся в часовом поясе Мск (UTC+3).
                Примеры:
                "2019-06-20"
                "2019-06-20T23:59:59"
                "2019-06-20T00:00:00.12345"
                "2017-03-25T00:00:00"
            date_to (str):
                Конечная дата отчета
            rrdid (Optional[int]):
                Уникальный идентификатор строки отчета. Необходим для получения отчета частями.
                Загрузку отчета нужно начинать с rrdid = 0 и при последующих вызовах API передавать в запросе значение rrd_id из последней строки, полученной в результате предыдущего вызова.
                Таким образом для загрузки одного отчета может понадобиться вызывать API до тех пор, пока количество возвращаемых строк не станет равным нулю.
            limit (Optional[int], optional): Defaults to 100_000.

                Максимальное количество строк отчета, возвращаемых методом. Не может быть более 100 000.

        Returns:
            List[RealizationReport]: Список отчетов по реализации.
        """
        data = self.__get_data(
            "reportDetailByPeriod", date_from, date_to, rrdid, limit, api_vers="v5"
        )
        return RealizationReports(realization_reports=data).realization_reports

    def __get_data(
        self,
        endpoint: str,
        date_from: str,
        date_to: Optional[str] = None,
        rrdid: Optional[int] = None,
        limit: Optional[int] = None,
        flag: Optional[int] = None,
        api_vers: Optional[str] = "v1",
    ) -> Any:
        validate_date(date_from)

        params: Dict[str, Any] = {"dateFrom": date_from}

        if date_to:
            params["dateTo"] = date_to
        if rrdid is not None:
            params["rrdId"] = rrdid
        if limit:
            params["limit"] = limit
        if flag is not None:
            params["flag"] = flag

        url = f"{self.base_url.format(api_vers=api_vers)}/{endpoint}"
        response = requests.get(
            url=url,
            headers={"Authorization": f"Bearer {self.api_key}"},
            params=params,
        )

        if response.ok:
            return response.json()

        self.__handle_errors(response)

    def __handle_errors(self, response: requests.Response) -> None:
        try:
            reason = response.json().get("detail", "").lower()
        except (ValueError, KeyError):
            reason = ""

        if response.status_code == 401:
            if "empty authorization header" in reason:
                raise TokenIsMissing("Токен отсутствует")
            elif "token is malformed" in reason:
                raise TokenIsMalformed("Токен не правильно сформирован")
            elif "token withdrawn" in reason:
                raise TokenNotFound("Токен удален")
            else:
                raise TokenIsNotApplicable(
                    "Используемый токен не применим к данным методам"
                )
        elif response.status_code == 429:
            raise ToManyRequests(
                "Превышено допустимое кол-во запросов в единицу времени"
            )
        else:
            response.raise_for_status()
