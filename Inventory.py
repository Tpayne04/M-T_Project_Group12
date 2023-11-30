import sqlite3
import sys

class Inventory:
    def __init__(self):
        pass

    def Inventory(self, databaseName='Inventory.db', tableName='Inventory'):
        self.databaseName = databaseName
        self.tableName = tableName
        self.conn = sqlite3.connect(r"Inventory.db")
        self.cursor = self.conn.cursor()
    
        # Check if table already exists, it should, this code is almost redundant now. Leaving it in case inventory's database fails.
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.tableName}';")
        if self.cursor.fetchone() is None:
            # If table doesn't exist, create it and insert a row
            self.cursor.execute(f'''CREATE TABLE {self.tableName}
                        (ProductID text PRIMARY KEY, ProductName text, ProductQuantity integer)''')
            self.cursor.execute("INSERT OR IGNORE INTO Inventory (ProductID, ProductName, ProductQuantity) VALUES ('1273', 'Harry Potter', '1273')")
            self.conn.commit()


    #getters n setters
    def getDatabaseName(self):
        return self.databaseName

    def getTableName(self):
        return self.tableName

    def setDatabaseName(self, databaseName):
        self.databaseName = databaseName

    def setTableName(self, tableName):
        self.tableName = tableName

    def viewInventory(self):
        self.conn = sqlite3.connect(r"Inventory.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute(f"SELECT * FROM Inventory")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def searchInventory(self, ProductID):
        self.conn = sqlite3.connect(r"Inventory.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute(f"SELECT * FROM Inventory WHERE ProductID=?", (ProductID,))
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def decreaseStock(self, ProductID, Quantity):
        self.conn = sqlite3.connect(r"Inventory.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute(f"UPDATE Inventory SET ProductQuantity = ProductQuantity - {Quantity} WHERE ProductID=?", (ProductID,))
        self.conn.commit()

