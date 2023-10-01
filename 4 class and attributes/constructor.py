class Phone:
    manufactured = "China"

    def __init__(
        self,
        owner,
        brand,
        price,
    ):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f"sending to: {phone} {sms}"
        print(text)
        
my_phone = Phone('Kala Chan','Oppo',9800)
her_phone = Phone('Shee',"iPhone",120000)
print(my_phone.owner,my_phone.brand,my_phone.price)
print(her_phone.owner,her_phone.brand,her_phone.price)

my_phone.send_sms(3456,'yeeeee')
her_phone.send_sms(254544,'loso')

dad_phone=Phone('Abbu',"Nokia",3000)
print(dad_phone.owner,dad_phone.brand,dad_phone.price)
