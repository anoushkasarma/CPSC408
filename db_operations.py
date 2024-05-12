import mysql.connector
from helper import helper

class db_operations():
    # constructor with connection path to DB
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost",
        user="root",
        password="CPSC408!",
        auth_plugin='mysql_native_password',
        database="RideShare")
        #create cursor object
        self.cursor = self.connection.cursor()
        #Print out connection to verify and close
        print(self.connection)
        print("connection made...")

    # function to simply execute a DDL or DML query.
    # commits query, returns no results. 
    # best used for insert/update/delete queries with no parameters
    def modify_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    # function to simply execute a DDL or DML query with parameters
    # commits query, returns no results. 
    # best used for insert/update/delete queries with named placeholders
    def modify_query_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        self.connection.commit()

    # function to simply execute a DQL query
    # does not commit, returns results
    # best used for select queries with no parameters
    def select_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    # function to simply execute a DQL query with parameters
    # does not commit, returns results
    # best used for select queries with named placeholders
    def select_query_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        return self.cursor.fetchall()

    # function to return the value of the first row's 
    # first attribute of some select query.
    # best used for querying a single aggregate select 
    # query with no parameters
    def single_record(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
    
    # function to return the value of the first row's 
    # first attribute of some select query.
    # best used for querying a single aggregate select 
    # query with named placeholders
    def single_record_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        return self.cursor.fetchone()[0]
    
    # function to return a single attribute for all records 
    # from some table.
    # best used for select statements with no parameters
    def single_attribute(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        results.remove(None)
        return results
    
    def single_attribute2(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        return results
    
    # function to return a single attribute for all records 
    # from some table.
    # best used for select statements with named placeholders
    def single_attribute_params(self, query, dictionary):
        self.cursor.execute(query,dictionary)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        return results
    
    # function for bulk inserting records
    # best used for inserting many records with parameters
    def bulk_insert(self, query, data):
        self.cursor.executemany(query, data)
        self.connection.commit()
    
    # function that creates table songs in our database
    def create_rider_table(self):
        query = '''
        CREATE TABLE rider(
            riderID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            Name VARCHAR(20) NOT NULL,
            Phone VARCHAR(10)
        );
        '''
        self.cursor.execute(query)
        self.connection.commit()
        print('Rider Table Created')

    def alter_rider(self):
         query = ''' ALTER TABLE rider MODIFY COLUMN Email VARCHAR(100);
        '''
         self.cursor.execute(query)
         self.connection.commit()
         print('Rider Table Altered')

    def create_driver_table(self):
        query = '''
        CREATE TABLE driver(
            driverID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            Name VARCHAR(20) NOT NULL,
            Phone VARCHAR(10),
            Mode BOOL
            );
            '''
        self.cursor.execute(query)
        self.connection.commit()
        print('Driver Table Created')

    def alter_driver(self):
        query = ''' ALTER TABLE driver MODIFY COLUMN driverID INT;
        '''
        self.cursor.execute(query)
        self.connection.commit()
        print('Driver Table Altered')


    def create_ride_table(self):
        query = '''
        CREATE TABLE ride(
            rideID INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            driverID INTEGER NOT NULL,
            riderID INTEGER NOT NULL,
            rating INTEGER,
            pickup VARCHAR(150) NOT NULL,
            dropoff VARCHAR(150),
            FOREIGN KEY (driverID) REFERENCES driver(driverID),
            FOREIGN KEY (riderID) REFERENCES rider(riderID)
            );
            '''
        self.cursor.execute(query)
        self.connection.commit()
        print('Ride Table Created')


    # function that returns if table has records
    # def is_songs_empty(self):
    #     #query to get count of songs in table
    #     query = '''
    #     SELECT COUNT(*)
    #     FROM songs;
    #     '''
    #     #run query and return value
    #     result = self.single_record(query)
    #     return result == 0

    # function to populate songs table given some path
    # to a CSV containing records
    def populate_rider_table(self, filepath):
        data = helper.data_cleaner(filepath)
        print(data)
        attribute_count = len(data[0])
        print(attribute_count)
        placeholders = ("%s,"*attribute_count)[:-1]
        query = "INSERT INTO rider(Name, Phone, Email) VALUES("+placeholders+")"
        print(query)
        self.bulk_insert(query, data)
        print("Your riders have been added!")

    

    def populate_driver_table(self, filepath):
        data = helper.data_cleaner(filepath)
        attribute_count = len(data[0])
        placeholders = ("%s,"*attribute_count)[:-1]
        query = "INSERT INTO driver (Name, Phone, Mode) VALUES("+placeholders+")"
        self.bulk_insert(query, data)
        print("Your drivers have been added!")


    def populate_ride_table(self, filepath):
            data = helper.data_cleaner(filepath)
            attribute_count = len(data[0])
            placeholders = ("%s,"*attribute_count)[:-1]
            query = "INSERT INTO ride (pickup, dropoff, driverID, riderID, rating) VALUES("+placeholders+")"
            self.bulk_insert(query, data)
            print("Your rides have been added!")




    # # Question 1
    # def add_songs_to_table(self, filepath):
    #         data = self.checkSongs(filepath)
    #         #adds all data into playlist.db
    #         if len(data) != 0:
    #             attribute_count = len(data[0])
    #             placeholders = ("?,"*attribute_count)[:-1]
    #             query = "INSERT INTO songs VALUES("+placeholders+")"
    #             self.bulk_insert(query, data)
    #             print("Your songs were successfully added to the playlist!")
    #         else:
    #             print("No new updates!")
       

    #BONUS QUESTION 1
    def checkSongs(self, filepath):
            data = helper.data_cleaner(filepath)
            
            #query to get list of all songs
            query = '''SELECT *
            FROM rider;'''

            #get old songs
            old_songs = self.single_attribute2(query)

            add_songs = []

            #checks to see if the songs are already in database or not
            for song in data:
                if song[0] not in old_songs:
                    add_songs.append(song)

            return add_songs











            # for i in len(song_ids):
            #     for j in len(in_playlist):
            #         if song_ids[i] == in_playlist[j]:







    # destructor that closes connection with DB
    def destructor(self):
        self.connection.close()
        self.cursor.close()