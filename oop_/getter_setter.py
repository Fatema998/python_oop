class stu:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name



    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age=age


s1=stu('fatema',20)
s2=stu('fatemaa',21)
s3=stu('fatemaaa',25)

print(s1.get_name())
print(s1.get_age())
print(s2.get_name())
print(s2.get_age())
print(s3.get_name())
print(s3.get_age())
s1.set_age(25)
s1.set_name('alex')
   

