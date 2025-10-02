class stu:
    schl='diu'


    @classmethod
    def sch_nm(cls):

        return cls.schl
    

    @staticmethod
    def ok_fn():
        return 'dhur jamu na'
    

s1=stu()
print(stu.sch_nm())
print(s1.sch_nm())
print(stu.ok_fn())
print(s1.ok_fn())
