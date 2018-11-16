#!/usr/bin/env python
# encoding: utf-8

def checkIDNumber(num_str):
    str_to_int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                  '6': 6, '7': 7, '8': 8, '9': 9, 'X': 10}
    check_dict = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7',
                  6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    if len(num_str) != 18:
        raise TypeError(u'请输入标准的第二代身份证号码')
    check_num = 0
    for index, num in enumerate(num_str):
        if index == 17:
            right_code = check_dict.get(check_num % 11)
            if num == right_code:
                print(u"身份证号: %s 校验通过" % num_str)
            else:
                print(u"身份证号: %s 校验不通过, 正确尾号应该为：%s" % (num_str, right_code))
        check_num += str_to_int.get(num) * (2 ** (17 - index) % 11)
if __name__ == '__main__':
    num_str1 = '34052419800101001X'
    num_str2 = '340524198001010011'
    checkIDNumber(num_str1)
    checkIDNumber(num_str2)
