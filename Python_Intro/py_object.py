

class StudentInfo:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def total(self):
        return sum(self.grades)

    def average(self):
        return sum(self.grades)/ len(self.grades)

student_one = StudentInfo('nill',[10,20,30,40,50])
student_two = StudentInfo('Diggonto',[20,30,40,50,60])
print(student_one.name)
print(student_one.grades)
print(student_one.total())


print(student_two.name)
print(student_two.grades)
print(student_two.total())

#################
class Store:
    def __init__(self,name):
        self.name = name
        self.item = []

    def add_item(self,name,price):
        item = {'name':name, 'price':price}
        self.item.append(item)

    def stock_price(self):
        return sum([item['price'] for item in self.item])

store_one = Store('Amazon')

store_one.add_item('plate',40)

print(store_one.name)
print(store_one.item)
print(store_one.stock_price())


