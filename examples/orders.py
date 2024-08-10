import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

stats = api.statistics
orders = stats.get_orders(date_from="2024-07-31")

for order in orders:
    print(order.date)
    print(order.order_type)
    print(order.nm_id)
