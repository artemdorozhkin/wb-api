import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

content = api.content
parents = content.get_all_parents()

for parent in parents:
    print(parent.id)
    print(parent.name)
