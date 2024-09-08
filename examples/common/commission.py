import os
from wb_api import WBApi
from dotenv import load_dotenv

load_dotenv()

api = WBApi(api_key=os.getenv("API_TOKEN"))

tariffs = api.common
comms = tariffs.get_commissions()

for comm in comms:
    print(comm.kgvp_marketplace)
    print(comm.paid_storage_kgvp)
    print(comm.parent_name)
