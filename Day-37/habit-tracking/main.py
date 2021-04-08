import requests
from datetime import datetime

USERNAME = "NAME GOES HERE"
TOKEN = "TOKEN GOES HERE"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": "aish",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Yoga",
    "unit": "Minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
yesterday = datetime(year=2021,month=4,day=7)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you perform yoga today?")
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixel_creation_endpoint,json=pixel_config, headers=headers)
# print(response.text)


pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "15"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.put(url=pixel_update_endpoint,json=new_pixel_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
