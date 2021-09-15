def log(func):
    def wrapper():
        print("start execute")
        func()
        print("end execute")
    return wrapper

@log
def my_func():
    print("Hello World")

my_func()
