import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

stats = api.statistics
incomes = stats.get_incomes(date_from="2024-07-31")

for income in incomes:
    print(income.date)
    print(income.income_id)
