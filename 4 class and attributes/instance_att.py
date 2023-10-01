class Shop:
    shoppingmall = "Jamuna"
    def __init__(self,buyer) -> None:
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute
        
    def add_to_cart(self,item):
        self.cart.append(item)
        
mehzabeen = Shop('Meh jabeen')
mehzabeen.add_to_cart('shoes')
mehzabeen.add_to_cart('phone')
print(mehzabeen.cart)

nisho = Shop('Nissho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)

apurbo = Shop('apurbo')
apurbo.add_to_cart('chiruni')
apurbo.add_to_cart('watch')
print(apurbo.cart)
