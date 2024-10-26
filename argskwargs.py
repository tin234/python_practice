def list_wrapper(initial_collection=None):
    collection = list(initial_collection)
    return collection
    
def add(item, *extra):
    collection.append(item)
    collection.extend(extra)
    return collection
    

collection = list_wrapper([1, 2, 3])
print(collection)
#Добавляем элементов в список
add(4, 5, 6)
print(collection)
#Расширяем список
add(8, 9)
print(collection)


def add(item, *args, **kwargs):
        if kwargs.get("trim", False):
            item = str(item).strip()
        
        collection.append(item)
        collection.extend(args)
        
        if kwargs.get("clear", False):
            collection.clear()
        
        return collection


collection = list_wrapper([1, 2, 3])

# Добавляем элементы с trim=True
add("new item", 4, 5, trim=True)
print(collection)
# Добавляем элементы с clear=True, что очищает коллекцию после добавления
add(6, 7, clear=True)
print(collection)
