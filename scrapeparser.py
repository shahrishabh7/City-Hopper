import csv

class Flight(object):
    def __init__(self,airlines,departure_time,arrival_time,origin,destination,price,layovers):
        self.airlines = airlines
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.origin = origin
        self.destination = destination
        self.price = price
        self.layovers = layovers

# str is a massive string representing webscraped flight data
# The method outputs a list of objects 'flights' which contain arrival/departure location/time and price details for each flight
def parser(str):
    data = []
    #Delete square brackets
    str = str[2:-2]

    # Split by ',' and create array of strings
    flights = str.split("', '")

    for flight in flights:
        row = flight.split("\\n")
        times = row[2].split('-')
        arrival,departure = times[0],times[1]
        locations = row[3].split('-')
        origin,destination = locations[0],locations[1]
        price = row[-3][1:]
        newflight = Flight(row[-5],departure,arrival,origin,destination,price,row[-6])
        data.append(newflight)
    return data