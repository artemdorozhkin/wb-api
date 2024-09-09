import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv(override=True)

api = WBApi(api_key=os.getenv("API_TOKEN"))

tariffs = api.common
return_ = tariffs.get_return(date="2024-09-08")

print(return_)
