my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    },
    "brother": {
        "name": "Grant",
        "age": 21
    },
    "grandpa": {
        "name": "Dustin",
        "age": 30
    },
    "dog": {
        "name": "Curt",
        "age": 10
    }
}

# for key,value in my_family.items():
#     print(f"{value['name']} is my {key} and is {str(value['age'])} years old.")

#Doing it with a comprehension

{ print(f"{value['name']} is my {key} and is {str(value['age'])} years old.") for key,value in my_family.items() }