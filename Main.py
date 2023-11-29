
#from optparse import check_choice
import sqlite3
import sys
import Inventory
import Cart
import User

Inventory.inventory(Inventory)
Cart.cart(Cart)
User.user(User)

while (getLoggedIn == False):
    print("Hello! Here are your options, 1: login, and 2: create an account. Type the number (1 or 2) you want to do.")
    choice = input(int())
    print()


option = 0
while (option != 4):

    print("1) View Account info")
    print("2) View Inventory Info")
    print("3) View Cart Info")
    print("4) Logout")

    option = input("Enter an option: ")

    if (option == 1):
        user.viewAccountInfo()
        


    elif (option == 2):

        invOption = 0
        while(invOption != 3):

            print("1) View Inventory")
            print("2) Search Inventory")
            print("3) Go Back")

            invOption = input("Enter an option: ")

            if (invOption == 1):
                inventory.viewInventory()

            elif (invOption == 2):
                inventory.searchInventory()

            elif (invOption != 3):
                print("Invalid Option.")



    elif (option == 3):
        
        cartOption = 0
        while(cartOption != 5):
            
            print("1) View Cart")
            print("2) Add to Cart")
            print("3) Remove from Cart")
            print("4) Checkout")
            print("5) Go Back")

            cartOption = input("Enter an option: ")

            if (cartOption == 1):
                cart.viewCart()

            elif (cartOption == 2):
                cart.addtoCart()

            elif (cartOption == 3):
                cart.removeFromCart()

            elif (cartOption == 4):
                cart.checkout()

            elif (cartOption != 5):
                print("Invalid Option.")



    elif (option == 4):
        print("Thanks for shopping with us!")
        user.logout()



    else:
        print("Invalid Option.")
