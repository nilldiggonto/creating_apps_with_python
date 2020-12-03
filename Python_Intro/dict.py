
student_dict = {
    'name': ['ini','mini','mo'],
    'grades':[2,3,2.5],
}

print(student_dict)
print(student_dict['name'])

print(student_dict.items())

for key,value in student_dict.items():
    print (key)
    print(value)

print( sum(student_dict['grades']))


##
student = {
    'name':'john',
    'class':'unknown',
    'grades':(45,23,24,10)
}

def average_grade(dict):
    grades = dict['grades']
    return sum(grades)/ len(grades)


print(average_grade(student))

##
def average_grade_of_students(student_dict):
    total = 0
    count = 0
    for student in student_dict:
        total += sum(student_dict['grades'])
        count += len(student_dict['name'])
    return total/count

print(average_grade_of_students(student_dict))
