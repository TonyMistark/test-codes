import sys
from time import sleep
from tqdm import tqdm


def tt(n):
    p = tqdm(range(n))
    for cha in p:
        sleep(0.04)
        p.set_description("Processing %s", cha)
        tqdm.write(f"{cha=}")


def t2():
    for batch in tqdm(range(100), total=100, position=0, file=sys.stdout, desc="desc"):
        if batch % 5 == 0:
            tqdm.write(str(batch))
            sleep(0.01)


if __name__ == "__main__":
    # tt(100)
    t2()
