#imports
from helper import helper
from db_operations import db_operations
import random
#import MySQL
import mysql.connector


#global variables
db_ops = db_operations()

def startScreen():
    #this makes all the tables
    #db_ops.create_rider_table()
    #db_ops.create_driver_table()
    #db_ops.create_ride_table()
    #db_ops.create_driver_table()
    #db_ops.alter_rider()
    # selectRiders()
    #db_ops.alter_driver()
    #db_ops.populate_rider_table("rider.csv")
    #db_ops.populate_driver_table("driver.csv")
    #db_ops.populate_ride_table("ride.csv")
    return

def firstStep():
    #ask user who they are
    print('''Hello! Are you
        1. A new User
        2. A Rider
        3. A Driver
        0. To Exit''')
    choice = helper.get_choice([1,2,3,0])
    return choice

def newUser():

    print("Enter 1 to make a new Rider account. Enter 2 to make a new Driver account.")
    choice = helper.get_choice([1,2])
    #gather information about new rider
    if choice == 1:
        name = input("Please Enter your Name: ")
        phone = input("Please enter a phone number: ")
        email = input("Please enter your email: ")
        data = [(name, phone, email)]
        placeholders = ("%s,"*3)[:-1]
        query = "INSERT INTO rider(Name, Phone, Email) VALUES("+placeholders+")"
        db_ops.bulk_insert(query, data)
    #gather information about new driver
    if choice == 2:
        name = input("Please Enter your Name: ")
        phone = input("Please enter a phone number: ")
        mode = input("Please enter your mode (0 or 1): ")
        data = [(name, phone, mode)]
        placeholders = ("%s,"*3)[:-1]
        query = "INSERT INTO driver (Name, Phone, Mode) VALUES("+placeholders+")"
        db_ops.bulk_insert(query,data)


def driverOptions():
    #ask for driverID
    driverID = input("Hello Driver! Please enter your ID: ")
    driverID = int(driverID)
    print("What would you like to do? \n 1. View your Rating \n 2. View your Rides \n 3. Change your Driver mode \n Enter a Number: ")
    driverChoice = helper.get_choice([1,2,3])
    driverDict = {"drID" : driverID}
    if driverChoice == 1:
        #query for average rating
        query = '''SELECT AVG(Rating)
        FROM ride
        WHERE driverID =%(drID)s;
        '''
        avg_rating = db_ops.single_attribute_params(query, driverDict)
        helper.pretty_print(avg_rating)
    elif driverChoice == 2:
        #query for all rides
        query = '''SELECT *
        FROM ride
        WHERE driverID =%(drID)s;
        '''
        rides = db_ops.select_query_params(query, driverDict)
        helper.pretty_print(rides)
    elif driverChoice == 3:
        #query to update driver mode
        newMode = input("Please enter your new DriverMode (0 for unavailable, 1 for available): ")
        newMode = int(newMode)
        driverDict["mode"] = newMode
        update_query = '''UPDATE driver SET Mode = %(mode)s
        WHERE driverID = %(drID)s;
        '''
        db_ops.modify_query_params(update_query, driverDict)
        select_query = '''SELECT *
        FROM driver
        WHERE driverID = %(drID)s;
        '''
        profile = db_ops.select_query_params(select_query, driverDict)
        helper.pretty_print(profile)
        print("Your mode has been updated!")
    else:
        print("option not chosen")
    return

def riderOptions():
    #get riderID
    riderID = input("Hello Rider! Please enter your ID: ")
    riderID = int(riderID)
    print("What would you like to do? \n 1. View your rides \n 2. Find a driver \n 3. Rate your ride")
    riderChoice = helper.get_choice([1,2,3])
    riderDict = {"riID" : riderID}

    if riderChoice == 1:
        #query to view all rides
        query = '''SELECT *
        FROM ride
        WHERE riderID = %(riID)s;
        '''
        rides = db_ops.select_query_params(query, riderDict)
        helper.pretty_print(rides)
    if riderChoice == 2:
        #find drivers available to drive
        query = '''SELECT driverID
        FROM driver 
        WHERE Mode = 1;
        '''
        availDrivers = db_ops.select_query(query)
        activeList = []
        #add to avaialble riders and choose a random driver
        for i in range(len(availDrivers)):
            id = availDrivers[i]
            activeList.append(id[0])

        num = random.randint(0, len(activeList) -1)
        driverID = activeList[num]
        driverDict = {"drID" : driverID}
        pickup = input("Please enter a pick up address: ")
        dropoff = input("Please enter a drop off address: ")
        data = [(driverID, riderID, pickup, dropoff)]
        placeholders = ("%s,"*4)[:-1]
        query = "INSERT INTO ride(driverID, riderID, pickUp, dropOff) VALUES("+placeholders+")"
        
        db_ops.bulk_insert(query, data)
        #get ride just created
        query = '''SELECT rideID
        FROM ride 
        ORDER BY rideID DESC
        LIMIT 1;
        '''
        #provide rideID
        new_rideID = db_ops.single_record(query)
        print("Your ride ID is: ", new_rideID)
        #send back to main menu

    if riderChoice == 3:
        #get most recent ride
        query = '''SELECT *
        FROM ride 
        WHERE riderID = %(riID)s
        ORDER BY rideID DESC
        LIMIT 1;
        '''
        recent_ride = db_ops.select_query_params(query, riderDict)
        if len(recent_ride) != 0:
            #ask if this is the correct ride
            helper.pretty_print(recent_ride)
            print("Is this the ride you want to leave a rating for? Enter 1 for Yes, Enter 2 for No: ")
            rideChoice = helper.get_choice([1,2])

            if rideChoice == 1:
                #show recent driver
                recent_driverID = recent_ride[0][1]
                print("Your recent driver was: ", recent_driverID)
                recent_rideID = recent_ride[0][0]
                #get rating
                print("Please enter a rating 1-5: ")
                rating = helper.get_choice([1,2,3,4,5])
                riderDict["rate"] = rating
                riderDict["recRideID"] = recent_rideID
                #update record
                update_query = '''UPDATE ride SET rating = %(rate)s WHERE rideID = %(recRideID)s;   
                '''
                db_ops.modify_query_params(update_query, riderDict)
                check_query = '''SELECT * 
                FROM ride
                WHERE rideID = %(recRideID)s;
                '''
                helper.pretty_print(db_ops.select_query_params(check_query, riderDict))

            if rideChoice == 2:
                #get all rides
                query = '''SELECT *
                FROM ride
                WHERE riderID = %(riID)s;
                '''
                rides = db_ops.select_query_params(query, riderDict)
                print("Here is a list of your rides: ")
                helper.pretty_print(rides)
                #ask which ride they want to rate
                changeRideID = input("Enter the ride ID of the ride you want to change: ")
                changeRideID = int(changeRideID)
                riderDict["recRideID"] = changeRideID
                print("Please enter a rating 1-5: ")
                #get rating
                rating = helper.get_choice([1,2,3,4,5])
                riderDict["rate"] = rating
                #update query
                update_query = '''UPDATE ride SET rating = %(rate)s WHERE rideID = %(recRideID)s;   
                '''
                db_ops.modify_query_params(update_query, riderDict)
                check_query = '''SELECT * 
                FROM ride
                WHERE rideID = %(recRideID)s;
                '''
                helper.pretty_print(db_ops.select_query_params(check_query, riderDict))
        else: 
            print("You have no rides to rate")





#main method
# startScreen()
while True:
    user_choice = firstStep()
    if user_choice == 1:
        newUser()
    elif user_choice == 2:
        riderOptions()
    elif user_choice == 3:
        driverOptions()
    else:
        break



db_ops.destructor()







