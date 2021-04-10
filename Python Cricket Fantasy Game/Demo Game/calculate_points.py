#Points calculation

#Importing module
import sqlite3

#Connection with cricket_db.db
my_db = sqlite3.connect("cricket_db.db")
cursor = my_db.cursor()
cursor.execute("SELECT * FROM match")
row = cursor.fetchall()

#Defining function to calculate
def calculate_points(row):
    points = 0
    score = row[1]
    
    try:
        #Strike rate = runs/balls faced
        strike_rate = float(row[1]) / float(row[2])  
    except:
        strike_rate = 0
    
    #Variables    
    fours = float(row[3])
    sixes = float(row[4])    
    twos = int((score - 4 * fours - 6 * sixes) / 2)
    wickets = 10 * float(row[8])
    
    try:
        economy = float(row[7]) / (float(row[5]) / 6)
    except:
        economy = 0
        
    fielding = float(row[9]) + float(row[10]) + float(row[11])

    #Points on the basis of given conditions
    
    #1 point for hitting a boundary
    #2 points for over boundary
    #10 points each for catch and wicket
    points = points + (fours + 2 * sixes + 10 * fielding + twos + wickets)

    #10 points for century
    if score > 100:
        points = points + 10

    #5 points for half century
    elif score >= 50:
        points = points + 5

    #for strike rate>100
    if strike_rate > 1:  
        points = points + 4

    #2 points for strike rate >= 80
    elif strike_rate >= 0.8:
        points = points + 2

    #Additional 10 points for 5 wickets
    if wickets >= 5:
        points = points + 10

    #Additional 5 points for 3 wickets
    elif wickets > 3:
        points = points + 5

    #4 points for eco rate between 3.5 and 4.5
    if economy >= 3.5 and economy <= 4.5:
        points = points + 4

    #7 points for economy rate between 2 and 3.5
    elif economy >= 2 and economy < 3.5:
        points = points + 7

    #10 points for economy rate less than 2
    elif economy < 2:
        points = points + 10
        
    return points

#Empty dictionary
player_points = {}

#Adding elements to dictionary through iteration
for element in row:
    player_points[element[0]] = calculate_points(element)

#Check
print(player_points)


