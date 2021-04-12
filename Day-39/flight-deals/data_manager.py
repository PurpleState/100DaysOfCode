import requests
from datetime import datetime

records_endpoint = "RECORDS ENDPOINT"
BEARER_TOKEN = "TOKEN"
today = datetime.now()

class DataManager:
    sheet_headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    def __init__(self):
        # self.get_sheet_data() for testing
        self.destination_data = {}

        #TODO: 1. Initialising the class function

    def get_sheet_data(self):

        #TODO: 2. How return works for a  class, is it necessary to declare the variable  in init
        sheet_response = requests.get(records_endpoint, headers=self.sheet_headers)
        self.destination_data = sheet_response.json()["prices"]
        return self.destination_data

    def put_sheet_data(self, sheet_row):
        body = {
            "price": {
                'city': sheet_row['city'],
                'iataCode': sheet_row['iataCode'],
                'id': sheet_row['id'],
                'lowestPrice': sheet_row['lowestPrice']
            }
        }
        requests.put(f"{records_endpoint}/{sheet_row['id']}", json=body, headers=self.sheet_headers)

