# flask -> Routes 

# @router,app('/login')
# def login():
#     print("Welcome to the login page")

# split the output to different strings
import functools

def split_string(function):
    @functools.wraps(function)
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@split_string
@uppercase_decorator
def greet():
    return "Hi There"

print(greet())

# Accept arguments in Decorator Function
# Create a general purpose decorator func

# LIST COMPREHENSIONS 

my_students = [{"name":"Naomi Lagat", "total_score": 450}, {"name":"Brian Kiprono", "total_score": 500}]

# Get the total average of the students
average_total_score = sum([ my_student["total_score"] for my_student in my_students ]) / len(my_students)
print(average_total_score)

# GENERATOR EXPRESSIONS 

# yield - OUTPUT,
#  4 sides 

def squares(length): 
    for l in range(length):
       yield l ** 2 

for square in squares(6):
    print (square)