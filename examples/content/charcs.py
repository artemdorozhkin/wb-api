import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

content = api.content
charcs = content.get_charcs(subject_id=1)

for charc in charcs:
    print(charc.charc_id)
    print(charc.name)
