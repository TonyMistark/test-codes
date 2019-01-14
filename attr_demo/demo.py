import attr


@attr.s
class SomeClass(object):
    a_number = attr.ib(default=42)
    list_of_numbers = attr.ib(factory=list)

    def hard_math(self, another_number):
        return self.a_number + sum(self.list_of_numbers) * another_number



if __name__ == "__main__":
    sc = SomeClass(1, [1, 2, 3])
    print("sc: ", sc)
    print("sc.hard_math: ", sc.hard_math(3))
    print("sc==SomeClass: ", sc == SomeClass(1, [1, 2, 3]))
    print("sc!=SomeClass: ", sc != SomeClass(2, [1, 2, 3]))
    print("attr.asdict(sc): ", attr.asdict(sc))
    print("SomeClass(): ", SomeClass())
    C = attr.make_class("C", ["a", "b"])
    print("C('foo', 'bar'): ", C("foo", "bar"))
