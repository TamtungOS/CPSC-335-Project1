# Hector S Mojica Arevalo & CJ Rinaldi
# Hector.Mojica@csu.fullerton.edu
# CPSC 335
# Project 1

# Project 1 Algorithm 2 Prompt
'''
Algorithm 2: Greedy Approach to Hamiltonian Problem

You are given a set of cities that are laid out in a circle, connected by a circular road that runs clockwise.
Each city has a gas station that provides gallons of fuel, and the distances between these cities are known. 
You have a car that can drive some number of miles per gallon of fuel,
and your goal is to pick a starting city such that you can fill up your car in that city (using that city’s gas station).
You can then drive to the next city, refill up your car with that city's fuel, drive to the next city,
and so on and so forth until you return back to the starting city with 0 or more gallons of fuel left.
This city is called a preferred starting city.
In this problem, it is guaranteed that there will always be exactly one valid starting city.

The problem set involves series of arrays. The first array is the distance between neighboring cities.
Assume that city i is distances[i] away from city i + 1 .
Since the cities are connected via a circular road, the last city is connected to the first city.
In other words, the last distance in the distances array is equal to the distance from the last city to the first city.
The second array is an  array of gas available at each city, where gas [i] is equal to the gas available at city i .
The total amount of gas available (from all gas stations) is enough to travel to all cities. Your gas tank always starts out empty,
and a positive integer value for the number of miles that your car can travel per gallon of fuel (miles per gallon, or MPG) is also given. 

Design an algorithm that returns the index of the preferred starting city.

Sample Input:

city_distances =       [5, 25, 15, 10, 15]
fuel =                       [1, 2, 1, 0, 3]
mpg =                        10

The preferred starting city for the sample above is city 4


'''
# Define function, takes distance between cities,
# fuel from each city, and the miles per gallon as its parameters
def find_starting_city(city_distances, fuel, mpg):
    start_city = 0 # Initializing the 0 to represent beginning of city list
    current_tank = 0 # Current tank at start of loop
    total_surplus = 0 # Tracks the amount of gasoline at each stage of the algorithm

# Loop that takes the range of the amount of items in the city_distances list
# and calculates the mileage after fueling as well finding the total gas in total_surplus
# and current_tank
    for i in range(len(city_distances)):
        mileage = fuel[i] * mpg
        net_mileage = mileage - city_distances[i]

        total_surplus += net_mileage # Running total for the amount of net gasoline in the car
        current_tank += net_mileage # Running total for the amount of gas currently in the car

        # Logic checking if the current_tank has less than 0 miles of gasoline, 
        # if the current tank gets lower than 0, meaning a negative amount of gasoline
        # the current loop will not pass requirements. Meaning we reset the loop
        if current_tank < 0:
            current_tank = 0
            start_city = i + 1 # Tracking which city we fail at, we know which cities we iterate through will not
                               # not be able to be used, so we skip the known bad cities to test untested options
    if total_surplus >= 0:
        return start_city

# Example inputs fro Project 1 description

city_distances = [5, 25, 15, 10, 15]
cities = [1, 2, 1, 0, 3]
mpg = 10
i = 0
city_balance = []

find_starting_city(city_distances = city_distances, fuel = cities, mpg = mpg)
