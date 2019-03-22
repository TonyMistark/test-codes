from dataclasses import dataclass
# python3.7引入的新模块dataclass
# 例如：


@dataclass
class A:
    a: int
    b: int
    c: str
    d: str = "test"

a = A(1, 2, "3")
print(a)


# 以上的代码和下面的代码是等价的

class B:
    def __init__(self, a, b, c, d="test"):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

b = B(1, 2, "3")
print(b)


# 再看类的继承


@dataclass
class C:
    a: int
    b: str


@dataclass
def D(C):
    c: int
    d: int

d = D(a=1, b="2", c=3, d=4)
print(d)


# 以上的代码和下面的代码是等价的


class C2:
    def __init__(self, a:int, b:str):
        self.a = a
        self.b = b

class D2(C2):
    def __init__(self, a: int, b: str, c: int, d: int):
        super().__init__(a, b)
        self.c = c
        self.d = d

d2 = D2(a=1, b="2", c=3, d=4)
print(d2)


# dataclass 还提供了make_dataclass来快速创建类
# 示例如下


from dataclasses import make_dataclass

A = make_dataclass(
        "A",
        [("a", int), "b", ("c", str), ("d", int, 1),],
        namespace={"add_one": lambda self: self.a + 1}
        )


# 以上的代码和下面的代码是等价的


@dataclass
class E:
    a: int
    b: ""
    c: str
    d: int = 1

    def add_one(self):
        self.a += 1


