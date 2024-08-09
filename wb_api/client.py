from wb_api.statistics import Statistics


class WBApi:
    def __init__(self, api_key: str, test_mode: bool = False) -> None:
        self.api_key = api_key
        self.test_mode = test_mode

    @property
    def statistics(self) -> Statistics:
        return Statistics(self)
