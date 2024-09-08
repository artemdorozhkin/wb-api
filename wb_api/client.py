from wb_api.common import Common
from wb_api.content import Content
from wb_api.statistics import Statistics


class WBApi:
    def __init__(self, api_key: str, test_mode: bool = False) -> None:
        self.api_key = api_key
        self.test_mode = test_mode

    @property
    def statistics(self) -> Statistics:
        return Statistics(self)

    @property
    def content(self) -> Content:
        return Content(self)

    @property
    def common(self) -> Common:
        return Common(self)
