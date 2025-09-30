class Stu:
    def __init__(self, name, c_class, id):
        self.name = name
        self.c_class = c_class
        self.id = id

    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.c_class}, id: {self.id}'


class Techr:
    def __init__(self, name, sub, id) -> None:
        self.name = name
        self.sub = sub
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, Subject: {self.sub}, id: {self.id}'


class Cls:
    def __init__(self, name) -> None:
        self.name = name
        self.teachrs = []  
        self.stus = []      
        self.next_id = 1   

    def add_teachr(self, name, sub):
        teachr = Techr(name, sub, self.next_id)
        self.teachrs.append(teachr)
        self.next_id += 1

    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            stuu = Stu(name, 'C', self.next_id)
            self.stus.append(stuu)
            extra = fee - 6500
            self.next_id += 1
            return f'{name} is enrolled with id: {stuu.id}, extra money: {extra}'

    def __repr__(self) -> str:
        print(f'Class name: {self.name}')
        print('Teachers:')
        for t in self.teachrs:
            print(t)
        print('Students:')
        for s in self.stus:
            print(s)
        return 'All done'
        

fatema = Cls('md ali')


print(fatema.enroll('alex', 3488))     
print(fatema.enroll('arman', 7865))   
print(fatema.enroll('ohi', 79479))    
print(fatema.enroll('shelina', 671378))


fatema.add_teachr('tom', 'algo')
fatema.add_teachr('korcu', 'cse')


print(fatema)
