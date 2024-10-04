class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price=price
        self.departure_airport_code=destination_airport
        self.departure_city=destination_city
        self.origin_city=origin_city
        self.orgin_airport=origin_airport
        self.out_date=out_date
        self.return_date=return_date
