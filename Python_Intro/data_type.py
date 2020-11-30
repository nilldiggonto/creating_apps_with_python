### LIST
car_price_list = [10,299,300,20,40]#list is mutable
print(car_price_list)
car_price_list.append(999999999)
print(car_price_list)
print(len(car_price_list))


### TUPLE
car_price_tuple = (10,299,300,20,40) #tuple is immutable
# car_price_tuple.append(999999999) #we can't use append in tuples
# To add tuple value
car_price_tuple = car_price_tuple + (99999,) 
print(car_price_tuple)
print(len(car_price_tuple))

### SET
car_number = { 2,3,3,3,3,4} #all value must be unique
print(car_number) #printing only the unique value
#add add value to set
car_number.add(55)
print(car_number)
print(len(car_number))
### TYpe
print(type(car_price_tuple))
print(type(car_price_list))
print(type(car_number))



############# MORE ABOUT SET ################
roll = {1,2,3,4,5,6,7}
std_id = { 5,4,3,1,2}

print(roll.intersection(std_id))
print(roll.union(std_id))