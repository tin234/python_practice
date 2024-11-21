class Person:
    def __eq__(self, value: object) -> bool: 
        print("in eq class")
        return True


p1 = Person()
p2 = Person()
print(p1 == p2)

def compare_people(person1, person2):
    return person1["name"] == person2["name"] and person1["age"] == person2["age"]

print(compare_people(person1, person2))  # True
print(compare_people(person1, person3))  # False

