from typing import List

from wb_api.base_api import BaseAPI
from wb_api.enum.locale import Locale

from wb_api.schemas.common.commission import Commission, Commissions


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
