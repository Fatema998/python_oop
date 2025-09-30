def call():
    print('ai call dor')
    return'dici call'


class phn:
    price =12000
    color='blue'
    brand='sumsung'
    feature=['camera','speker','hammer']



    def  call (self):
        print('call  dea call dea')


    def send_sms(self,phn ,sms):
        text=f'snd sms to : {phn} and msg : {sms}'
        return text
    
    my_phn=phn()
    print(my_phn.feature)
    my_phn.call()
    result=my_phn.send_sms(1897843567, 'miss u')
    print(result)