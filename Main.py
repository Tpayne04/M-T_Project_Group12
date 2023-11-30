
#from optparse import check_choice
import sqlite3
import sys
import Inventory
import Cart
import User

inventory = Inventory.Inventory()
cart = Cart.Cart()
user = User.User()

while (user.getLoggedIn() == False):
    print()
    print("Hello! Welcome to our E-Commerce Book Store!")
    print("1) Log In")
    print("2) Create An Account")
    print("3) Exit")
    choice = input("Please enter an option: ")
    print()

    if (choice == '1'):
        user.login()

    elif (choice == '2'):
        user.createAccount()

    elif (choice == '3'):
        sys.exit()

    else:
        print("Invalid Option. Try Again.")


option = 0
while (option != '4'):

    print("1) View Account info")
    print("2) View Inventory Info")
    print("3) View Cart Info")
    print("4) Logout")
    print()

    option = input("Enter an option: ")

    if (option == '1'):
        user.viewAccountInformation()
        print()
        


    elif (option == '2'):

        invOption = 0
        while(invOption != '3'):

            print("1) View Inventory")
            print("2) Search Inventory")
            print("3) Go Back")

            invOption = input("Enter an option: ")
            print()

            if (invOption == '1'):
                inventory.viewInventory()
                print()

            elif (invOption == '2'):
                searchProduct = input("Enter the product ID: ")
                inventory.searchInventory(searchProduct)
                print()

            elif (invOption != '3'):
                print("Invalid Option.")



    elif (option == '3'):
        
        cartOption = 0
        while(cartOption != '5'):
            
            print("1) View Cart")
            print("2) Add to Cart")
            print("3) Remove from Cart")
            print("4) Checkout")
            print("5) Go Back")

            cartOption = input("Enter an option: ")
            print()

            if (cartOption == '1'):
                username = user.getUserID()
                cart.viewCart(username)

            elif (cartOption == '2'):
                username = user.getUserID()
                product = input("Enter the ID of the product you want to add to your cart: ")
                quantity= input("How many do you want to buy: ")
                cart.addToCart(username, product, quantity)

            elif (cartOption == '3'):
                username = user.getUserID()
                product = input("Enter the ID of the product you want to remove from your cart: ")
                cart.removeFromCart(username, product)

            elif (cartOption == '4'):
                username = user.getUserID()
                cart.checkOut(username)

            elif (cartOption != '5'):
                print("Invalid Option.")



    elif (option == '4'):
        print("Thanks for shopping with us!")
        user.logout()



    else:
        print("Invalid Option.")
