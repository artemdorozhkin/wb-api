from typing import List

from wb_api.base_api import BaseAPI
from wb_api.enum.locale import Locale

from wb_api.schemas.common.box import Box
from wb_api.schemas.common.commission import Commission, Commissions
from wb_api.utils import validate_date


class Common(BaseAPI):
    def __init__(self, wb_api) -> None:
        base_url: str = (
            "https://common-api{sandbox}.wildberries.ru/api/{api_vers}/tariffs"
        )
        super().__init__(api_client=wb_api, base_url=base_url)

    def get_commissions(
        self,
        locale: Locale = Locale.RU,
    ) -> List[Commission]:
        """
        Комиссия по категориям товаров

        Args:
            locale (Locale):
                Язык полей ответа parentName и subjectName:
                    ru — русский
                    en — английский
                    zh — китайский

        Returns:
            List[Commission]: Список комиссий.
        """
        data = self.get_data(
            endpoint="commission",
            locale=locale,
        )
        if "report" in data:
            return Commissions(commissions=data["report"]).commissions

    def get_box(self, date: str) -> Box:
        """
        Тарифы для коробов

        Для товаров, которые поставляются на склад в коробах (коробках), возвращает стоимость:

            доставки со склада или пункта приёма до покупателя;
            доставки от покупателя до пункта приёма;
            хранения на складе Wildberries.
            Максимум — 60 запросов в минуту.

        Args:
            date (str): Дата в формате ГГГГ-ММ-ДД
        """
        validate_date(date)

        data = self.get_data(endpoint="box", date=date)
        if "response" in data:
            if "data" in data["response"]:
                return Box(**data["response"]["data"])
