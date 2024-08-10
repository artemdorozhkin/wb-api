import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

content = api.content
ndses = content.get_nds()  # or `content.get_vat()`

for nds in ndses:
    print(nds)
