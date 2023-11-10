import sqlite3

class Inventory:
    def __init__(self, databaseName='Group project database.db', tableName='Inventory'):
        self.databaseName = databaseName
        self.tableName = tableName
        self.conn = sqlite3.connect(self.databaseName)
        self.cursor = self.conn.cursor()
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.tableName}
                     (ProductID text PRIMARY KEY, ProductName text, ProductQuantity integer)''')
        self.cursor.execute("INSERT OR IGNORE INTO Inventory (ProductID, ProductName, ProductQuantity) VALUES ('1273', 'Harry Potter', '1273')")
        self.conn.commit()

    def viewInventory(self):
        self.cursor.execute(f"SELECT * FROM {self.tableName}")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def searchInventory(self, ProductID):
        self.cursor.execute(f"SELECT * FROM {self.tableName} WHERE ProductID=?", (ProductID,))
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def decreaseStock(self, ProductID):
        self.cursor.execute(f"UPDATE {self.tableName} SET ProductQuantity = ProductQuantity - 1 WHERE ProductID=?", (ProductID,))
        self.conn.commit()


#inventory = Inventory('C:/Program Files/DB Browser for SQLite/Methods and Tools of Software Development 2023 folder/Group project database.db', 'Inventory')
