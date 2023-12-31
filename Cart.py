import sqlite3
import Inventory

class Cart:


    def __init__(self, databaseName = "CartClass.db", tableName = "Cart"):
        self.databaseName = databaseName
        self.tableName = tableName
    

    # Zero constructor. Nothing needs to be initialized here, but it allows for the functions to be used.
    def Cart():
        pass


    # Initially sets up the database / table names that will be used throughout the class to access the
    # appropriate database and table
    def Cart(self):
        self.connection = sqlite3.connect("CartClass.db")
        self.cursor = self.connection.cursor()
        self.create_table()
        query = f"CREATE TABLE IF NOT EXISTS {self.tableName} (UserID INTEGER, ProductID TEXT, ProductQuantity INTEGER)"
        self.cursor.execute(query)
        self.connection.commit()


    # Displays all books in the logged in User's cart. Please note: this cooperates with the inventory database
    # to display all the correct information on the inventory items - it just selectively shows the books in
    # the User's cart
    def viewCart(self, userID):
        self.connection = sqlite3.connect("CartClass.db")
        self.cursor = self.connection.cursor()

        query = f"SELECT * FROM {self.tableName} WHERE UserID = ?"
        self.cursor.execute(query, (userID,))
        cartItems = self.cursor.fetchall()

        if cartItems:
            print ("All items in cart:")
            for item in cartItems:
                print(f"ProductID: {item[1]}")
                print(f"Quantity: {item[2]}")
        else:
            print("The cart is empty.")

        print()
    

    # This relies on the user viewing the inventory previously - from the main. Once they select a book, 
    # this ISBN is used to add an item to the appropiate cart
    def addToCart(self, userID, ProductID, ProductQuantity):
        self.connection = sqlite3.connect("CartClass.db")
        self.cursor = self.connection.cursor()

        inventory = Inventory.Inventory()
        inventory.connection = sqlite3.connect('Inventory.db')
        inventory.cursor = inventory.connection.cursor()

        testQuery = f"SELECT * FROM Inventory WHERE productID = ?"
        inventory.cursor.execute(testQuery, (ProductID,))
        results = inventory.cursor.fetchall()

        if results:
            query = f"INSERT INTO {self.tableName} (UserID, ProductID, Quantity) VALUES (?, ?, ?)"
            self.cursor.execute(query, (userID, ProductID, ProductQuantity))
            self.connection.commit()
            print(f"ProductID {ProductID} was added to the cart for the user {userID}.")
            print()

        else:
            print("Invalid product ID. Please try again.")
            print()
        
        
    

    # This relies on the user viewing the cart previously - from the main. Once they select a book to remove, 
    # this ISBN is used to remove an item form the user's cart
    def removeFromCart(self, userID, ProductID):
        self.connection = sqlite3.connect("CartClass.db")
        self.cursor = self.connection.cursor()
        
        query = f"DELETE FROM {self.tableName} WHERE UserID = ? AND ProductID = ?"
        self.cursor.execute(query, (userID, ProductID))
        self.connection.commit()
        print(f"ProductID {ProductID} was removed from the cart for the user {userID}.")


    # The user checks out - this removes all their cart items. It also calls the inventory class function
    # to decrease the stock of the books by the correct amount the user bought (prior to remove them from the cart)
    def checkOut(self, userID):
        self.connection = sqlite3.connect("CartClass.db")
        self.cursor = self.connection.cursor()

        querySelect = f"SELECT * FROM {self.tableName} WHERE UserID = ?"
        self.cursor.execute(querySelect, (userID,))
        cartItems = self.cursor.fetchall()

        if not cartItems:
            print("The cart is empty.")
            return
        
        inventory = Inventory.Inventory()
        inventory.connection = sqlite3.connect('Inventory.db')
        inventory.cursor = self.connection.cursor()

        for item in cartItems:
            ProductID = item[1]
            ProductQuantity = item[2]

            # Updates inventory
            
            inventory.decreaseStock(ProductID, ProductQuantity)

        query_delete = f"DELETE FROM {self.tableName} WHERE UserID = ?"
        self.cursor.execute(query_delete, (userID,))
        self.connection.commit()
        print(f"The checkout was completed for user {userID} and the cart is now empty.")


    
