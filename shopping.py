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

shop = Shopper("daraz")
shop.add_to_cart("Ring Light",500,1)
shop.add_to_cart("",500,1)


print(shop.checkout(1000))


