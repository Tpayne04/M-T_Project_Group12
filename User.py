import sqlite3
import sys

class User:

    ## Variables
    __databaseName = "User.db"
    __tableName = "Users"
    __loggedIn = False # stores as int in database. 0 is logged out, 1 is logged in.
    __userID = ""



    ## Functions
    def __init__(self, userID = "", loggedIn = False):
        self.userID = userID
        self.loggedIn = loggedIn



    def User(self, databaseName = "User.db", tableName = "Users"):

        self.connection = sqlite3.connect(databaseName)
        print("DATABASE CONNECTED")
        self.cursor = self.connection.cursor()



    def createAccount(self, databaseName = "User.db", tableName = "Users"):
        # Connect to database
        self.connection = sqlite3.connect(databaseName)
        print("DATABASE CONNECTED")
        self.cursor = self.connection.cursor()

        # Ask for new username
        username = input("Enter a username: ")
        
        # Inserts username into database and sets it to not logged in
        query = f"INSERT INTO Users (userID, loggedIn) VALUES (?, ?)"
        self.cursor.execute(query, (username, '0'))
        self.connection.commit()

        print("Account Successfully Created!")
        return True



    def login(self, databaseName = "User.db", tableName = "Users"):
        # Connect to database
        self.connection = sqlite3.connect(databaseName)
        print("DATABASE CONNECTED")
        self.cursor = self.connection.cursor()
        
        # Asks for username
        username = input("Please enter your username: ")

        # Checks if username in database
        query = f"SELECT * FROM Users WHERE userID = ?"
        self.cursor.execute(query, (username,))
        results = self.cursor.fetchall()
        
        if not results:
            print("Invalid Username. Please try again, or create an account.")
            return False;

        query = f"UPDATE Users SET loggedIn = ? WHERE userID = ?"
        self.cursor.execute(query, ('1', username))
        self.connection.commit()
        self.__userID = username
        self.__loggedIn = True
        return True;



    def logout(self, databaseName = "User.db", tableName = "Users"):
        # Connect to database
        self.connection = sqlite3.connect(databaseName)
        self.cursor = self.connection.cursor()

        # Gets username
        username = self.__userID

        query = f"UPDATE Users SET loggedIn = ? WHERE userID = ?"
        self.cursor.execute(query, ('0', username))
        self.connection.commit()

        self.__userID = ""
        self.__loggedIn = False
        return False



    def viewAccountInformation(self):
        print("Username: " + self.getUserID())
        if self.getLoggedIn() == True:
            print("Status: Logged In")
        else:
            print("Status: Logged Out")



    def setUserID(self):
        pass
    


    def getUserID(self):
        username = self.__userID
        return username



    def setLoggedIn(self):
        pass



    def getLoggedIn(self):
        status = self.__loggedIn
        return status










