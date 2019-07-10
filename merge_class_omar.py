class Merge(object):
    _merged_classes = []

    @classmethod
    def merge_class(cls, target_class):
        if target_class not in cls._merged_classes:
            cls._merged_classes = cls._merged_classes + [target_class]

    def __getattr__(self, name):
        for cls in self._merged_classes:
            if hasattr(cls, name):
                return getattr(cls, name).__get__(self)
        raise AttributeError()


class Base(object):
    def z(self, x):
        print("Base.z", self)
        return x * 2


class A(Base, Merge):
    def a(self, num):
        print("A.a", self)
        return num


class B(object):
    def b(self, num):
        print("B.b", self)
        return num

    def a(self, num):
        print("B.a", self)
        return num
A.merge_class(B)


if __name__ == "__main__":
    a = A()
    a.a(3)
    a.b(2)
    a.z(1)
    a.y(1)
