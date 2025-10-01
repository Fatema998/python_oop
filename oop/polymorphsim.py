class animal:
    def __init__(self,name):
        self.name=name


    def make_sund(self):
        print('animal making some sund')


class cat(animal):
    def __init__(self, name):
        super().__init__(name)


    def make_sund(self):
       print('meaooooooooo meooooooo')


class dog(animal):
    def __init__(self, name):
        super().__init__(name)


    def make_sund(self):
        print('geoooooooo')


class cow(animal):
    def __init__(self, name):
        super().__init__(name)
    


    def make_sund(self):
        print('hamba')




class horse(animal):
    def __init__(self, name):
        super().__init__(name)


    def make_sund(self):
        print('kmnea dake jani na')


class versity_sap_frnd(animal):
    def __init__(self, name):
        super().__init__(name)



    def make_sund(self):
        print('kub vala re ')




cartu=cat('crtu')
cartu.make_sund()
dg=dog('lcl')
dg.make_sund()
cw=cow('raw')
cw.make_sund()
hrs=horse('primry')
hrs.make_sund()
vrsty=versity_sap_frnd('na koi')
vrsty.make_sund()

animals=[cartu,dg,cw,hrs,vrsty]
for a in animals:
    a.make_sund()