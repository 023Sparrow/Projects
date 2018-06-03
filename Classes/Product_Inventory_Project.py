class Product():
    def __init__(self,id,name,price,quantity):
        self.name = name
        self.price = price
        self.id = id
        self.quantity = quantity

    def viewProduct(self):
        print('''
Product ID: {}
Product name: {}
Product price: {}
Product quantity: {}'''.format(self.id,self.name,self.price,self.quantity))

    def getquantiy(self):
        return self.quantity

    def pricechange(self,newprice):
        if newprice > 0:
            self.price = newprice
        else:
            print('Error! The price must above zero.')

    def quantitychange(self,newquantity):
        if newquantity > 0:
            self.quantity = newquantity
        else:
            print('Error! The quantity must above zero.')

class Inventory():
    def __init__(self):
        self.listProd = []

    def addProduct(self,id):
        self.listProd.append(id)

    def removeProduct(self,id):
        if id in self.listProd:
            self.listProd.remove(id)
        else:
            print('Error! There is no such product in the product list.')

    def viewInventory(self):
        print(self.listProd)

if __name__ == '__main__':
    prod1 = Product(1,"colgate",2.20,5)
    print (prod1.getquantiy())
    prod1.viewProduct()

    invent1 = Inventory()
    invent1.addProduct(1)
    invent1.removeProduct(2)
    invent1.viewInventory()
