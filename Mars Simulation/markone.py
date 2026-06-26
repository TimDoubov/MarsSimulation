#Basic Variables
people = 300
food = 3000
daily_shipment = 200
Day = 0
Survive = True
#Deletes how much food people eat daily
def daily_food(f, p):
    return f - p * 3 #+ daily_shipment
#Loops through day until death
while Survive == True:
    Day += 1
    food = daily_food(food, people)
    if food <= 0:
        people -= int(abs(food/3))
        food = 0
    if people <= 0:
        Survive = False
        people = 0
    print(f"Mars Survival: Day {Day}, People alive: {people}, Food Left: {food}")




