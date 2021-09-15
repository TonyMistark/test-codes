import time

class Potato:
    @classmethod
    def make(cls, num, *args, **kwargs):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kwargs))
        return potato

all_potatos = Potao.make(5)

