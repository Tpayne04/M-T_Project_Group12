import sqlite3

class User:

    ## Variables
    __databaseName = ""
    __tableName = ""
    __loggedIn = False
    __userID = ""



    ## Functions
    def __init__(self, userID = "", loggedIn = False):
        self.userID = userID
        self.loggedIn = loggedIn

    
    # Zero constructor. Nothing needs to be initialized here, but it allows for the
    # functions to be used.
    def User():
        print("FIX ME: USER\n")


    # Initially sets up the database / table names that will be used throughout the class 
    # to access the appropriate database and table. NOT USED FOR USER LOGIN!
    def User(databaseName, tableName):
        print("FIX ME: USER\n")


    # Input, validation, and verification to allow someone to login. 
    # Updates the loggedIn boolean and returns true/false back to main upon successful login. 
    # Sets the userID to the user who logged in for tracking.
    def login():
        print("FIX ME: LOGIN\n")

        userID = input("Please enter your User ID: ")

        # if verified
        loggedIn = True
        return True

        # if not verified
        loggedIn = False
        return False


    # Resets the userID back to blank and loggedIn back to false.
    # Returns false to be used in main.
    def logout():

        userID = ""
        loggedIn = False
        return False


    # Displays all the appropriate account information to the currently logged in user.
    # Query based on tracked userID in the class
    def viewAccountInformation():
        print("FIX ME: VIEWACCOUNTINFORMATION\n")


    # Contains all input and output related to creating an account – validation included. 
    # Once a correct person’s inputs are gathered, handles database interaction appropriately.
    def createAccount():
        print("FIX ME: CREATEACCOUNT\n")

        userID = input("Please enter a valid user name: ")
        print("\n")



    # Getter for loggedIn
    def getLoggedIn():
        print("FIX ME: GETLOGGEDIN\n")


    # Getter for userID
    def getUserID():
        print("FIX ME: GETUSERID\n")

