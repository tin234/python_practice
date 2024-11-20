person1 = {"name": "Alice", "age": 30}
person2 = {"name": "Alice", "age": 30}
person3 = {"name": "Bob", "age": 25}

def compare_people(person1, person2):
    return person1["name"] == person2["name"] and person1["age"] == person2["age"]

print(compare_people(person1, person2))  # True
print(compare_people(person1, person3))  # False
