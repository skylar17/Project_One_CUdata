import os
import csv

historical_in_csv = os.path.join("2017-06-22.csv")

# Lists to store data
location = []
city = []
utc = []
parameter = []
value = []
unit = []
latitude = []
longitude = []

with open(historical_in_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:

        if row[1] == "IN":

            location.append(row[0])

            city.append(row[1])

            utc.append(row[3])

            parameter.append(row[5])

            value.append(row[6])

            unit.append(row[7])

            latitude.append(row[8])

            longitude.append(row[9])


cleaned_historical = zip(location, city, utc, parameter, value, unit, latitude, longitude)

output_file = os.path.join("cleaned_historical_in.csv")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    #writer.writerow("Location", "City", "Date/Time", "Parameter", "Value", "Unit", "LAT", "LON")
    
    writer.writerows(cleaned_historical)