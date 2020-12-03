
class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/ len(self.marks)

    @classmethod
    def classmate(cls,origin,mate_name,*args):
        return cls(mate_name,origin.school,*args)
        


john = Student('john','a_school')
print(john.name)
print(john.school)

doe = john.classmate(john,'doe')
print(doe.name)
print(doe.school)



class ForeignStudent(Student):
    def __init__(self,name,school,country,continent):
        super().__init__(name,school)
        self.country = country
        self.continent = continent

kona = ForeignStudent('kona','y_school','BD','Asia')
print(kona.country)
print(kona.school)
print(kona.continent)

nimi = kona.classmate(kona,'nimi','IRN','EAST')
print(nimi.school)
print(nimi.country)
print(nimi.continent)
# nii = ForeignStudent.classmate(kona,'nimi','IRN','EAST')


#####################################
def items(*args):
    print(args)

items(1,2,3,4,5,6)

def items_list(*args,**kwargs):
    print(args)
    print(kwargs)

items_list(1,2,3,4, food='rice', fruit='banana')