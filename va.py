from pydantic import validate_arguments


@validate_arguments
def pos_or_kw(a: int, b: int = 2) -> str:
    return f'a={a} b={b}'


print(pos_or_kw('1'))
