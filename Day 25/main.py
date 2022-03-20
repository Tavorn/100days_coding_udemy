import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].to_list()
print(len(fur_color))
# data_dict = data.to_dict()
# print(data_dict)

"""
Fur Color, Count
0, grey ,24233
1, red, 83992
2, black, 30993-
how many Cinnamon, Black and Gray
"""

# import csv
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
#
# monday_temp = int(monday.temp)
# print(monday_temp)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# with open("weather_data.csv") as weather_file:
#     weather_data = weather_file.readlines()
#     for data in weather_data:
#         print(data)
