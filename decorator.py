def trimmer(func):
    def wrapper(*args):
        _list = []
        for arg in args: 
            if isinstance(arg, str):
                _list.append(arg.strip())
            else: 
                _list.append(arg)    

        _tuple = tuple(_list)
        func(*_tuple)
    return wrapper

@trimmer
def print_text(a: str, b: int, c:bool):
    print([a,b,c])

print_text( " text " , 10, True)
