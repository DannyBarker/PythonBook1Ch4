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

for key,value in my_family.items():
    arr = list()
    for nest_value in value.values():
        arr.append(nest_value)
        print(arr)
