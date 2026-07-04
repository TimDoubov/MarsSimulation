#Imports
import random
#Basic Variables
people = 300
food = 3000
day = 0
survive = True
shipment_success = 0
research_points = 1.00
researchers = 0
#Determines how much food is made in a day
# relative to technology research
def daily_gain(farmer,points):
    #Number of food one farmer will get for a day
    return farmer * int(points)
    
#Collects and adds research points - each person is a hundreth of a point
def daily_research (people):
    global research_points
    research_points += people/100


#Deletes how much food people eat daily
def daily_food(f, p, s):
    return f - p * 3 + s
#Marks the beginning
print(f"Welcome to the Mars simulation - Please enter your name: ")
name = input()
print(f"Welcome {name} - Good Luck")

#Loops through day until death or day 100
while survive == True:
    day += 1
    free_work = people
    researchers = 0
    #Printing starting statements and questions
    print(f"Simulation Day {day} - People Alive: {people} - Food Avaliable: {food}")
    print(f"Current farming efficiency: {int(research_points)} food per farmer")
    #Input for farmers
    print(f"How many people would you like to go farm? ({free_work} people are free):")
    farmers = int(input())
    #Makes that value is valid
    if farmers > free_work or farmers < 0:
        print ("INVALID INPUT")
        survive = False
    else:
        free_work -= farmers
        #Input for researchers only if there is free_work
        if free_work > 0:

            print(f"How many people to research lab? ({free_work} people are free): ")
            researchers = int(input())
            #Makes sure that value is valid
            if researchers > free_work or researchers < 0:
                print ("INVALID INPUT")
                survive = False
            else:
                free_work -= researchers

    daily_research(researchers)

    food = daily_food(food, people, daily_gain(farmers, research_points))
    if food <= 0:
        people -= int(abs(food/3))
        food = 0
    if people <= 0:
        survive = False
        people = 0
    if day == 100:
        survive = False

if day == 100:
 print(f"You survived Mars - {people} remain")
else:
    print("You failed")



