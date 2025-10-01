from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def eat(self):
        pass


    def move(self):
        print(f'{self.name}knh dike jaiyum')


class cow(animal):
    def __init__(self,name):
        self.name=name
        


    


    def eat(self):
        print(f'{self.name}gas kaiyum')

    def move(self):
        print(f'{self.name}mathea jamu')


class cat(animal):
    def __init__(self,name) ->None:
        self.name=name
    

    def eat(self):
        print(f'{self.name}mac kaiyum')

    def move(self):
        print(f'{self.name}mathea jamu')


class dog(animal):
    def __init__(self,name) ->None:
        self.name=name
        

    def eat(self):
        print(f'{self.name}ice cream kaiyum')
        
    def move(self):
        print(f'{self.name}mathea jamu')


class fox(animal):
    def __init__(self,name) ->None:
        self.name=name
        

    def eat(self):
        print(f'{self.name}gas kaiyum')

    def move(self):
        print(f'{self.name}mathea jamu')


cw=cow('raju')
ct=cat('mini')
dg=dog('tomi')
fx=fox('dj_seyal')

animals=[cw,ct,dg,fx]
for a in animals:
    a.eat()
    a.move()