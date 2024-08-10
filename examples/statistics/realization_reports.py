import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

stats = api.statistics
reports = stats.get_realization_reports(date_from="2024-07-31", date_to="2024-08-01")

for report in reports:
    print(report.date_from)
    print(report.nm_id)
    print(report.commission_percent)
