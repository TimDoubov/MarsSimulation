#Imports
import random
#Basic Variables
people = 300
food = 3000
max_shipment = 300
day = 0
survive = True
shipment_success = 0

def daily_shipment(m,s):
    return int(m*s)


#Deletes how much food people eat daily
def daily_food(f, p, s):
    return f - p * 3 + s
#Loops through day until death or day 100
while survive == True:
    day += 1
    shipment_success = random.random()
    food = daily_food(food, people, daily_shipment(max_shipment, shipment_success))
    if food <= 0:
        people -= int(abs(food/3))
        food = 0
    if people <= 0:
        survive = False
        people = 0
    if day == 100:
        survive = False
    print(f"Mars Survival: Day {day}, People alive: {people}, Food Left: {food}, Shipment Success: %{int(shipment_success*100)}")




