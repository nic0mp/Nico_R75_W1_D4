# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    
    
    def __init__(self):
        self.cart = []

    def add2Cart(self):
        products = input('What would you like to add? ')
        self.cart.append(products)

    def removeFromCart(self,item):
        removedItem = input('What would you like to remove? ')
        self.cart.remove(removedItem)

    def showMyCart(self):
        print('These items are in your cart:')
        for item in self.cart:
            print(item)


myCart = Cart()

# Test
# myCart.add2Cart('milk')
# myCart.add2Cart('milk')
# myCart.showMyCart()
# myCart.add2Cart('pork')

def run():
    while True:
        response = input('What do you want to do? add/show/remove or quit ')
        
        if response.lower()== 'quit':
            myCart.showMyCart()
            print('Thanks for shopping')
            break
        elif response.lower() == 'add':
            myCart.add2Cart()
        elif response.lower() == 'show':
            myCart.showMyCart()
        elif response.lower == 'remove':
            myCart.removeFromCart()
            
        


run()
 
    