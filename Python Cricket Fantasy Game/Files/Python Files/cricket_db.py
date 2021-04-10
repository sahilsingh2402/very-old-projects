#Tables creation

#importing module
import sqlite3

#Connection with cricket_db.db
my_db = sqlite3.connect('cricket_db.db')  
cursor = my_db.cursor()

#Match table creation
cursor.execute('''CREATE TABLE IF NOT EXISTS match (Player TEXT NOT NULL,Scored INTEGER,Faced INTEGER,Fours INTEGER,Sixes INTEGER,Bowled INTEGER,Maiden INTEGER,Given INTEGER,wkts INTEGER,Catches INTEGER,Stumping INTEGER,RO INTEGER);''')

#Stats table creation
cursor.execute('''CREATE TABLE IF NOT EXISTS stats (player PRIMARY KEY,matches INTEGER,runs INTEGER,hundreds INTEGER,fifties INTEGER,value INTEGER,ctg TEXT NOT NULL);''')

#Teams table creation
cursor.execute('''CREATE TABLE IF NOT EXISTS teams (name TEXT NOT NULL,players TEXT NOT NULL,value INTEGER);''')

#Displaying data if exists
sql_query = "select * from match"
cursor.execute(sql_query)
results = cursor.fetchall()

if (results):
    #To check
    for element in results:
        print(element)
        
    #To add more players   
    opt=input("\nAdd more players details (Yes(Y)/No(N)):")
    
else:
    print("No players data found ")

    #To add new players
    opt = input("\nAdd players data (Yes(Y)/No(N)):")
    
#Adding data to match table
while (opt == 'Y' or opt == 'y'):

    #Inputting player name
    name = input("Player name: ")
    row = [name]

    #Inputting player score
    score = int(input("Score: "))
    row.append(score)

    #Inputting faced balls
    faced = int(input("Faced: "))
    row.append(faced)

    #Inputting fours
    fours = int(input("Fours: "))
    row.append(fours)

    #Inputting sixes
    sixes = int(input("Sixes: "))
    row.append(sixes)

    #Inputting balls            
    bowled = int(input("Bowled: "))
    row.append(bowled)

    #Inputting maiden
    maiden = int(input("Maiden: "))
    row.append(maiden)

    #Inputting wasted/given
    given = int(input("Given: "))
    row.append(given)

    #Inputting wickets
    wkts = int(input("Wkts: "))            
    row.append(wkts)
                
    #Inputting catches
    catches = int(input("Catches: "))
    row.append(catches)

    #Inputting stump outs
    stumping = int(input("Stumping: "))
    row.append(stumping)

    #Inputting run outs
    ro = int(input("RO: "))
    row.append(ro)   
    
    try:
        #Adding data to database       
        cursor.execute("INSERT INTO match (player,scored, faced, fours,sixes,bowled,maiden,given,wkts,catches,stumping,ro) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                     (row[0],row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]) )
        my_db.commit()

        print("Records added successfully to table match.")
                
    except:
        #Except block to handle exceptions
        print("Error in operation.")
        my_db.rollback()   

    #Adding data to stats
    print("\nPlayers information for Stats table")

    #Inputting total number of matches
    total_matches = int(input("Total matches: "))            
    row.append(total_matches)

    #Inputting total number of runs
    total_runs = int(input("Total runs: "))
    row.append(total_runs)

    #Inputting total number of hundreds
    hundreds = int(input("100s: "))
    row.append(hundreds)
                
    #Inputting total number of fifties
    fifties = int(input("50s: "))
    row.append(fifties)
                
    #Inputting value
    value = int(input("Value: "))
    row.append(value)
                
    #Inputting category
    category = input("Category as (BAT,BWL,AR,WK): ")
    row.append(category)
    
    try:
        #Adding data to database
        cursor.execute("INSERT INTO stats (player,matches,runs, hundreds, fifties,value,ctg) VALUES (?,?,?,?,?,?,?)", 
                          (row[0],row[12], row[13], row[14],row[15],row[16],row[17]))
        my_db.commit()
        print("Records added successfully to stats table.")
                
    except:
        #To handle exceptions
        print("Error in operation.")
        my_db.rollback()
        
    opt=input("Add more playerS (Y/N) : ")

#To Close database
print("Exiting!!!")   
my_db.close() 

    
    
    
    
    
    

    
    

    
    
    
    
    
 
                          
        

        
     
        
        
    
    
    
        

    
    
    
    
    

    
    
         
    
    
                          
        

    
    
        
        
        
    
    
        

    

