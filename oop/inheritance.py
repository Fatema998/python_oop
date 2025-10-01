class gadget:
    def __init__(self,brand,price,color,origin) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.origin=origin


class laptop:
    def __init__(self,memory,ssd):

        self.memory=memory
        self.ssd=ssd

class phone(gadget):
    def __init__(self, brand, price, color, origin,duel_sim):
        self.duel_sim=duel_sim
        super().__init__(brand, price, color, origin)


    def phn_call(self,numbr,txt):
        return f'snding sms to : {numbr} with:{txt}'
    

    def __repr__(self) ->str:

        return f'phn : {self.brand} {self.price} {self.duel_sim}'


class camera:
    def __init__(self,pixel):

        self.pixel=pixel



fatema_phn=phone('iphn',13000000000,'black','china', True)
print(fatema_phn.brand)
print(fatema_phn)
print(fatema_phn.phn_call('01987565347456','hi rafi vai'))
     
    
    
