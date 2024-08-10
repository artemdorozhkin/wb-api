import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

content = api.content
countries = content.get_countries()

for country in countries:
    print(country.name)
    print(country.full_name)
