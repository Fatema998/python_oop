class shpping:
    def __init__(self,name):
       self.name=name 
       self.cart=[]
    def add_cart(self,item,price,quantity):
        prduct={'item': item, 'price': price,'quantity': quantity}
        self.cart.append(prduct)
    def checkout(self,amount):
        total=0
        for item in self.cart:

            total+=item['price'] *item['quantity']
        print('total price',total)
        if(amount<total):
            print(f'pls provide {total-amount} more')
        else:
            extra=amount-total
            print(f'extr mny: {extra}')

fatema=shpping('alex')
fatema.add_cart('nur',60,2)
fatema.add_cart('jur',67,3)
print(fatema.cart)
fatema.checkout(1300)
   