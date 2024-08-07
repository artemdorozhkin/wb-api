from wb_api import WBApi

api = WBApi("API_KEY")

stats = api.statistics
incomes = stats.get_incomes("2024-07-31")
stocks = stats.get_stocks("2024-07-31")
orders = stats.get_orders("2024-07-31")
sales = stats.get_sales("2024-07-31")
realization_reports = stats.get_realization_reports("2024-08-05", "2024-08-06", 1)
