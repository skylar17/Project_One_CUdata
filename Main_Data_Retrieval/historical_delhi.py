import os
import csv

historical_in_csv = os.path.join("cleaned_historical.csv")

# Lists to store data
location = []
city = []
utc = []
parameter = []
value = []
latitude = []
longitude = []

with open(historical_in_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:

        if row[1] == "Delhi":

            location.append(row[0])

            city.append(row[1])

            utc.append(row[2])

            parameter.append(row[3])

            value.append(row[4])

            latitude.append(row[6])

            longitude.append(row[7])


dh_clean = zip(location, city, utc, parameter, value, latitude, longitude)

output_file = os.path.join("dh_clean.csv")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    #writer.writerow("Location", "City", "Date/Time", "Parameter", "Value", "LAT", "LON")
    
    writer.writerows(dh_clean)
