class Merge(object):

    @classmethod
    def merge_class(cls, target_class):
        for k, v in target_class.__dict__.items():
            print(f"k: {k}--v: {v}")
            if k.startswith("__"):
                continue
            #if hasattr(k, v):
            #    print("Warning", k, v)
            setattr(cls, k, v)

class A(Merge):
    def a(self, num):
        return num


class B(object):
    def get_b(self, num):
        return num
A.merge_class(B)


if __name__ == "__main__":
    b = A().get_b(111)
    print(f"b: {b}")
