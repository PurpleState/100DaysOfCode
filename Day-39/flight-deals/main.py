#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import  DataManager
from pprint import pprint
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},
              {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 42},
              {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 485},
              {'city': 'Sydney', 'iataCode': 'SYD', 'id': 5, 'lowestPrice': 551},
              {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 95},
              {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 414},
              {'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 240},
              {'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 260},
              {'city': 'Cape Town', 'iataCode': 'CPT', 'id': 10, 'lowestPrice': 378}]

data_manager = DataManager()
#sheet_data = data_manager.get_sheet_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

# if I use row and when index
for row in sheet_data:
    if row["iataCode"] == '':
        print("still being called")
        iataCode = flight_search.get_destination_code(row['city']) # TODO: 5. when to use instance and when to create a new object and update
        row["iataCode"] = iataCode
        data_manager.put_sheet_data(row)

print(sheet_data)
# TODO: 6. why objects are so mutable, how and when the objects will mutate, and in which case it will not change

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(destination)
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )

print(type(flight))
print(flight)
