class rafi_vai_bank:
    def __init__(self,holder_name,initial_deposit ,branch='main') ->None:
        self.holder=holder_name
        self.branch=branch
        self.__blance=initial_deposit


    def deposit(self,amount):
        self.__blance+= amount

    def get_balance(self):
        return self.__blance
    

    def with_drw(self,amount):
        if(amount<=self.__blance):
            self.__blance=self.__blance-amount
            return amount
        else:
            return f'tk nai beyadop bedi'
        

fatema=rafi_vai_bank('nur',456789034567)

fatema.holder='nuri'
fatema.deposit(765432345678)
print(fatema.get_balance())
print(fatema.holder)



            

        


    