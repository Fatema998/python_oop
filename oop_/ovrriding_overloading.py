class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def info(self):
        return 'i am a person'

class math:
    def add(self ,*args):
        return sum(args)
    
m=math()
print(m.add(2,5))
print(m.add(2,3))
print(m.add(9,5))
class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

    def info(self):
        return 'i am a cricketer'
    

    def __gt__(self,other):
        return self.age > other.age
sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)
    
if sakib>musfiq:
    print(f'{sakib.name} is oldr thn {musfiq.name}')
else:
    print(f'{musfiq.name} is old rhn {sakib.name}')


Cricketers=[sakib,musfiq,kamal,jack,kalam]
for c in Cricketers:
    print(c.name,c.age,c.height,c.weight)

