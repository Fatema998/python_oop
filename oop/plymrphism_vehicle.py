class vehicle:
    def __init__(self,name):
        self.name=name


    def  move(self):
        print('Vehicle is moving')



class car(vehicle):
    def __init__(self, name):
        super().__init__(name)


    def move(self):
        print('driving on road')




class boat(vehicle):
    def __init__(self, name):
        super().__init__(name)


    def move(self):
        print('sailing on water')




class airplane(vehicle):
    def __init__(self, name):
        super().__init__(name)


    def move(self):
        print('flying in the sky')



cr1=car('toyota')
plane1=airplane('amirat')
boat1=boat('titanic')


fatema=[cr1,plane1,boat1]
for f in fatema:
    f.move()
     