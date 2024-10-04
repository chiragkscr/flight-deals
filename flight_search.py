
API_ENDPOINT="https://api.tequila.kiwi.com"
API_KEY="0S31BbClRSBbXgaFBtuF9Ab1eTPRAqB8"
import requests
from flight_data import FlightData
class FlightSearch:
    def get_Destination_code(self, city):
        location_endpoint=f"{API_ENDPOINT}/locations/query"
        headers={"apikey":API_KEY}
        query={"term": city,
               "location_types":"city"}
        response=requests.get(url=location_endpoint, headers=headers, params=query)
        result=response.json()['locations']
        code=result[0]["code"]
        return code
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers={"apikey": API_KEY}
        query={
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "max_stopovers":0,
            "curr":"INR"

        }

        response=requests.get(url=f"{API_ENDPOINT}/v2/search", headers=headers, params=query)

        try:
            data=response.json()["data"][0]
        except:
            print(f"No Flights found for {destination_city_code}")
            return None
        # print(response.json())

        flight_data=FlightData(price=data['price'],
                               origin_city=data["route"][0]["cityFrom"],
                               origin_airport=data["route"][0]["flyFrom"],
                               destination_city=data["route"][0]["cityTo"],
                               destination_airport=data["route"][0]["flyTo"],
                               out_date=data["route"][0]["local_departure"].split("T")[0],
                               return_date=data["route"][0]["local_departure"].split("T")[0])
        print(f"{flight_data.departure_city}: Rs{flight_data.price}")
        return flight_data