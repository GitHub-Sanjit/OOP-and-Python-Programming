class Shop:
    cart = []
    def __init__(self,buyer) -> None:
        self.buyer = buyer
        
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