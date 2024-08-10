import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

stats = api.statistics
stocks = stats.get_stocks(date_from="2024-07-31")

for stock in stocks:
    print(stock.last_change_date)
    print(stock.warehouse_name)
    print(stock.quantity)
