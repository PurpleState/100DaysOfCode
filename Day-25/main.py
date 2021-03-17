#with open('weather_data.csv') as data_file:
#  data = data_file.readline()
#  print(data)

import csv

with open("weather_data.csv") as data_file:
  data = csv.reader(data_file)
  temperatures = []
  for row in data:
    print(row)
    if row[1] != temp:
      temperatures(row[1])
  print(temperatures) 
  
import pandas 

pandas.read_csv("weather_data.csv")
print(data)

print(data["temp"])
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())

print(data.condition)

#get data in row
data[data.day=="Monday"]
