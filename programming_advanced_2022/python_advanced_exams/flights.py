def flights(*args):
    day_flights = {}
    for i in range(0, len(args), 2):
        city = args[i]
        if city == "Finish":
            return day_flights
        passengers = int(args[i + 1])

        if city not in day_flights:
            day_flights[city] = 0
        day_flights[city] += passengers


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
