import functools


def log1(function):
    def wrapper(*args, **kwargs):
        print("log1 wrapper befor: %s() is called" % function.__name__)
        func = function(*args, **kwargs)
        print("log1 wrapper afer: %s() is called" % function.__name__)
        return func
    return wrapper


def log2(desc):
    def decrator(function):
        def wrapper(*args, **kwargs):
            print("log2 wrapper befor: %s() is called, and desc: %s" % (function.__name__, desc))
            func = function(*args, **kwargs)
            print("log2 wrapper afer: %s() is called, and desc: %s" % (function.__name__, desc))
            return func
        return wrapper
    return decrator


def log3(desc):
    def decrator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print("log3 wrapper befor: %s() is called, and desc: %s" % (function.__name__, desc))
            func = function(*args, **kwargs)
            print("log3 wrapper afer: %s() is called, and desc: %s" % (function.__name__, desc))
            return func
        return wrapper
    return decrator

@log1
@log2("desc2")
@log3("desc3")
def test_func(say_somting):
    print("execute test_func and you say: %s" % say_somting)



if __name__ == "__main__":
    test_func("Hello World!")
