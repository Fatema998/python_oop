class bank:
    def __init__(self,blance):
        self.blance=blance
        self.min_withdrw=100
        self.max_withdrw=100000000



    def get_blc(self):
        return self.blance
    
    def deposite(self,amount):
        if amount>0:
           
           self.blance+=amount


    def withdrw(self,amount):
        if amount <self.min_withdrw:
            print(f'fokira {self.min_withdrw}')


        elif amount>self.max_withdrw:
            print(f'bank fokir hoiya jbe {self.max_withdrw}')
        else:
            self.blance-=amount
            print(f'blance dek{amount}')
            print(f'aftr widrw:{self.get_blc()}')



fatema_bank=bank(1499999)
fatema_bank.withdrw(4356)
fatema_bank.withdrw(89645)
fatema_bank.deposite(67348)
print(fatema_bank.get_blc())