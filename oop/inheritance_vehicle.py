class vehicle:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price


class car(vehicle):
    def __init__(self, brand, model, price,seat):
        self.seat=seat
        super().__init__(brand, model, price)
    
    def car_info(self) ->str:
         return f'brand:{self.brand}, model:{self.model},price:{self.price},seats:{self.seat}'



class bike(vehicle):
    def __init__(self, brand, model, price,engine_pwr):
        self.engine_pwr=engine_pwr
        super().__init__(brand, model, price)

    def bike_info(self) ->str:
         return f'brand:{self.brand}, model:{self.model},price:{self.price},cc:{self.engine_pwr}'
  


  

cr=car('toyota','alexjhg',657889,5)
bik=bike('honda','rt235',35645,145)
print(cr.car_info())
print(bik.bike_info())

        
        