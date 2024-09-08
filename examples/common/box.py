import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv(override=True)

api = WBApi(api_key=os.getenv("API_TOKEN"))

tariffs = api.common
box = tariffs.get_box(date="2024-09-08")

print(box)
