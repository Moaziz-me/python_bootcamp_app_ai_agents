import csv

with open("file/weather.csv", "r") as file:
    df_weather = list(csv.reader(file))

while True:
    city_input = input("Enter city: ")

    result = False

    for row in df_weather:
        if row[0] == city_input:
            print(row[1])
            result = True

    if not result:
        print("City not found")

