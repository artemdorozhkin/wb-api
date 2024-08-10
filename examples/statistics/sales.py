import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

stats = api.statistics
sales = stats.get_sales(date_from="2024-07-31")

for sale in sales:
    print(sale.date)
    print(sale.nm_id)
    print(sale.total_price)
