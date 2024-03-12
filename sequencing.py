# DICTIONARIES

# CREATE A DICTIONARY 

SDFT08_students = {
    "name_one": "Clare Oparo",
    "name_two": "Collins Kip",
    "name_three": "Naomi Lagat",
    "name_four": "Dennis Kipkirui"
}

def access_dict_items(items):
    print(items['name_two'])

# add / remove items within a dict

def add_item(items):
    items["name_five"] = "Joseph Wambua"
    print(items)

def remove_items(items):
    # del items['name_one']
    items.clear()
    print(items)

# change values within specific keys on a dict
SDFT08_students['name_three'] = "Nelson Doe"
# print(SDFT08_students)
# iterate over the items within a dict

# for item in SDFT08_students:
#     print(SDFT08_students[item])

# access_dict_items(SDFT08_students)
# add_item(SDFT08_students)
# remove_items(SDFT08_students)

# TUPLES 

# How to create a tuple ('sdnjsdv', 'smdhbvjhsf')

numbers = (10, 4, 5, 70, 90, 10, 90)

# access the different items 
# print(numbers)

# numbers[0] = "Yes"
# print(numbers)

# iterate 
for item in numbers: 
    # perform some func
    # print(item)
    pass

# LIST 
my_list = ["Joseph Wambua", True, 10, 100000.5434534, {"name": "Clare Oparo"}, (10, 20 , 30)]

# Access the items 
for my_list_item in my_list:
    print(my_list_item)

# access an dividual items
print(my_list[5])

# add elements .append 

my_list.append({"country_name": "Egypt"})
print(my_list)

# changing reassignment property 
my_list[3] = False
print(my_list)

# removing elements 
# my_list.remove(0)
# print(my_list)
print(my_list[4]['name'])