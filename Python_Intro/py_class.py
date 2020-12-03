class Student:
    def __init__(self,name,section):
        self.name = name
        self.section = section
        self.grades = []

    def average(self):
        return sum(self.grades)/len(self.grades)

    def section_belong(self):
        print(f'I belong to section {self.section}')

    @classmethod
    def school_name(cls):
        print('We Are the student of this School')

    @staticmethod
    def grade_name():
        print('We are all A Grade')


john = Student('john','water')
doe = Student('doe','Sky')

john.section_belong()

john.school_name()
doe.school_name()
Student.school_name()
Student.grade_name()

#############################
class Store:
    def __init__(self,name):
        self.name = name
        self.items = []

    def add_item(self,name,price):
        item = {'name':name, 'price':price}
        self.items.append(item)
    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total
    
    @classmethod
    def brand(cls,store):
        new_store = store.name+ '-brand'
        return new_store

    @staticmethod
    def store_detail(store):
        return f'{store.name} where product price is, {store.stock_price()}'



item_one = Store('Amazon')
item_one.add_item('plate',20)


print(Store.store_detail(item_one))
print(Store.brand(item_one))

