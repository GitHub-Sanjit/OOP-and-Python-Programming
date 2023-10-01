def call():
    print('calling someone i dont know')
    return 'call done'


class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    feature = ['camera','speaker','hammer']

    def call(self):
        print("calling one person")
        
    def send_sms(self,phone,sms):
        text = f'sending sms to: {phone} and message: {sms}'
        print(text)
        return text

my_phone= Phone()
print(my_phone.feature)
print(my_phone.brand)
my_phone.call()
my_phone.send_sms(4152,"I forgot to miss you")