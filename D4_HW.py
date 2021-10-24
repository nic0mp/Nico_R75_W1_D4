# Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program
# The comments in the cell below are there as a guide for thinking about the problem. However, 
# if you feel a different way is best for you and your own thought process, please do what feels best
#  for you by all means.
# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    
    
    def __init__(self):
       self.cart = []

    def add2Cart(self,item):
        self.cart.append(item)

    def removeFromCart(self,item):
        self.cart.remove(item)

    def showMyCart(self):
        print(self.cart)


myCart = Cart()

myCart.add2Cart('milk')
myCart.add2Cart('milk')
myCart.showMyCart()
myCart.add2Cart('pork')
myCart.showMyCart()