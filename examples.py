import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

stats = api.statistics
# incomes = stats.get_incomes("2024-07-31")
# stocks = stats.get_stocks("2024-07-31")
# orders = stats.get_orders("2024-07-31")
# sales = stats.get_sales("2024-07-31")
# realization_reports = stats.get_realization_reports("2024-08-05", "2024-08-06", 1)

content = api.content
# parents = content.get_all_parents()
# subjects = content.get_all_subjects()
