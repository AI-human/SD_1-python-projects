import os
class Shopper:
    def __init__(self,name):
        self.name = name
        self.cart = []


    def add_to_cart(self,item,price,quantity):
        self.cart.append({'name':item,'price':price,'quantity':quantity})

    def checkout(self,amount):
        price = 0
        for item in self.cart:
            price = price + item['price'] * item['quantity']
        if amount<price:
            return f"Please give {price - amount}"
        elif amount==price:
            return "Here your product"
        else :
            return f"Here your extra money {amount - price}"

def menu():
    os.system('cls')
    print("Input your name")
    name = input()
    shop = Shopper(name)
    print("1. Add to cart")
    print("2. Checkout")
    print("3. Exit")
    print("Input your choice")
    choice = int(input())
    while 1:
        if choice==1:
            os.system('cls')
            print("Input item name")
            item = input()
            print("Input item price")
            price = int(input())
            print("Input item quantity")
            quantity = int(input())
            shop.add_to_cart(item,price,quantity)
            print("1. Add to cart")
            print("2. Checkout")
            print("3. Exit")
            print("Input your choice")
            choice = int(input())
        elif choice==2:
            os.system('cls')
            print("Input amount")
            amount = int(input())
            reply = shop.checkout(amount)
            print(reply)
            print("1. Add to cart")
            print("2. Checkout")
            print("3. Exit")
            print("Input your choice")
            choice = int(input())
        elif choice==3:
            os.system('cls')
            print("Thank you for shopping")
            break
    
menu()