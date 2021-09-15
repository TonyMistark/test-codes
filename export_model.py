from pydantic import BaseModel

class BarModel(BaseModel):
    whatever: int


class FooBarModel(BaseModel):
    banana: float
    foo: str
    bar: BarModel


m = FooBarModel(banana=3.14, foo="hello", bar={"whatever": 123})

print("m.dict: ", m.dict())

print("include: ", m.dict(include={"foo", "bar"}))

print("include: ", m.dict(exclude={"foo", "bar"}))

print("dict m: ", dict(m))

