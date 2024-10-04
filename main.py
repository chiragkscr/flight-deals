#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

data_manager=DataManager()
flight_search=FlightSearch()
sheet_data=data_manager.get_destination_data()
# pprint(sheet_data)

ORIGIN_CITY_IATA="LON"

for row in sheet_data:
    if row['iataCode']=="":
        code=flight_search.get_Destination_code(row['city'])
        row["iataCode"]=code

data_manager.destination=sheet_data
data_manager.update_destination_data()

tomorrow= datetime.now() + timedelta(days=1)
six_months_from_today=datetime.now()+timedelta(days=(6*30))

for destination in sheet_data:
    flight= flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )









