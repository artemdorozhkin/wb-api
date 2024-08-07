from wb_api.statistics import Statistics


class WBApi:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    @property
    def statistics(self) -> Statistics:
        return Statistics(self.api_key)
