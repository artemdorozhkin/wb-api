import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

content = api.content
colors = content.get_colors()

for color in colors:
    print(color.name)
    print(color.parent_name)
