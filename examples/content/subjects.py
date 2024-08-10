import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"), test_mode=True)

content = api.content
subjects = content.get_all_subjects()

for subject in subjects:
    print(subject.subject_id)
    print(subject.subject_name)
