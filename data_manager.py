import requests

API_ENDPOINT="https://api.sheety.co/15ca84023c144f7fdb5c0ce05a589ac5/prices/sheet1"
class DataManager:
    def __init__(self):
        self.destination={}

    def get_destination_data(self):
        response = requests.get(url=API_ENDPOINT)
        data = response.json()
        self.destination = data
        return data['sheet1']

    def update_destination_data(self):
        for city in self.destination:
            new_data={
                "sheet1":{
                    "iataCode":city['iataCode']
                }
            }
            response=requests.put(url=f"{API_ENDPOINT}/{city['id']}", json=new_data)










