from typing import Any, Optional
import requests
from wb_api.exceptions import (
    TokenIsMissing,
    TokenIsMalformed,
    TokenNotFound,
    TokenIsNotApplicable,
    ToManyRequests,
)
from wb_api.utils import snake_to_camel_case


class BaseAPI:
    def __init__(self, api_client, base_url: str) -> None:
        self.base_url = base_url
        self.api_key = api_client.api_key
        self.test_mode = api_client.test_mode

    def get_data(
        self,
        endpoint: str,
        api_vers: Optional[str] = "v1",
        **kwargs,
    ) -> Any:
        kwargs = {snake_to_camel_case(key): value for key, value in kwargs.items()}

        sandbox = "-sandbox" if self.test_mode else ""
        url = f"{self.base_url.format(api_vers=api_vers, sandbox=sandbox)}/{endpoint}"
        response = requests.get(
            url=url,
            headers={"Authorization": f"Bearer {self.api_key}"},
            params=kwargs,
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
