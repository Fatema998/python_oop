class phone:
    manufactured='china'

    def __init__(self,owner,brand,price):
        self.ower=owner
        self.brand=brand
        self.price=price


    def send_sms(self,phn,sms):
        txt=f'sending to {phn} {sms}'
        print(txt)
        

my_phn=phone('fatema' ,'iphn',98000)
print(my_phn.owner,my_phn.brand,my_phn.price)
hr_phn=phone('sshe','iphn','450000000')
print(hr_phn.ower,hr_phn.brand,hr_phn.price)

cr_phn=phone('kr','sarah',679933)
print(cr_phn.ower,cr_phn.brand,cr_phn.price)

