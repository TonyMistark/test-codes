import sys
import string
import binascii


DEBUG = False


SD = {i: v for i, v in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")}


def log_args_result(func):
    def wrapper(*args, **kwargs):
        if DEBUG:
            print(func.__name__, f"{args=}")
        result = func(*args, **kwargs)
        if DEBUG:
            print(func.__name__, result)
        return result
    return wrapper


@log_args_result
def convert_str_to_16(s):
    return binascii.b2a_hex(s.encode('utf-8'))


@log_args_result
def convert_16_to_2(s):
    str2 =  str(bin(int(s, 16)))[2:]
    delta = 8 - len(str2)
    if delta > 0:
        str2 = "0" * delta + str2
    return str2


@log_args_result
def convert(s):
    str_2_total = ""
    for i in s:
        str_16 = convert_str_to_16(i)
        str2 = convert_16_to_2(str_16)
        str_2_total += str2
    groups = []
    temp_str = ""
    for i in range(0, len(str_2_total), 6):
        tmp = str_2_total[i: i+6]
        delta = 6 - len(tmp)
        if delta > 0:
            tmp += "0" * delta
        delta = 6 - len(tmp)
        groups.append(int(tmp, 2))
    return groups


@log_args_result
def process_3_cell(s):
    result = convert(s)
    r = ""
    for i in result:
        r += SD[i]
    delta = 4 - len(result)
    if delta > 0:
        r += "="*delta
    return r


@log_args_result
def split_3_cell(s):
    result = []
    for i in range(0, len(s), 3):
        result.append(s[i: i+3])
    return result



if "__main__" == __name__:
    input_str = sys.argv[1]
    group_3 = split_3_cell(input_str)
    base64str = ""
    for index, g in enumerate(group_3):
        r = process_3_cell(g)
        base64str += r
    print(f"{input_str=}\n{base64str=}")



