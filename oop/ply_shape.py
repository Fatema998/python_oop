class shape:
    def __init__(self,name):
        self.name=name


    

class rec(shape):
    def __init__(self, name,width,height) ->None:
        self.width=width
        self.height=height
        super().__init__(name)

    def area(self):
        return self.width* self.height
    
class cir(shape):
    def __init__(self, name,radius):
        self.radius=radius
        super().__init__(name)

    def area(self):
        return 3.1416*self.radius*self.radius


r1=rec('rec',5,10)
c1=cir('cer',7)
shp=[r1,c1]
for s in shp:
    print(s.name,s.area())