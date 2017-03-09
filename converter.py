def convert_n_to_m(x, n, m):
    letters = ['0','1','2','3','4','5','6','7','8','9',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z']
    x = str(x).upper()
    for elem in str(x):
        if elem not in letters[:n]:
            return False
    result1 = int(str(x),n)
    if m == 10:
        result2 = result1
        return result2
    elif m == 1:
        result2 = '0' * result1
        return result2
    elif m == 2:
        result2 = bin(result1)
        return result2[2:]
    elif m == 16:
        result2 = hex(result1)
        result2 = result2.upper()
        return result2[2:]
    elif m == 8:
        result2 = oct(result1)
        return result2[2:]
    elif 2<m<10:
        result2 = ''
        counter = 0
        while result1>0:
            counter+=1
            y = result1 %m
            result2 = str(y) + result2
            result1 = int(result1/m)
        return result2
    elif m>10:
        result2 = ''
        while result1>0:
            y = result1 %m
            if letters[y]:
                result2 = letters[y] + result2
                result1 = int(result1/m)
            else:
                return False
        return result2
    else:
        return False

if __name__ == '__main__':
    print(convert_n_to_m([123], 4, 3))
    print(convert_n_to_m("0123", 5, 6))
    print(convert_n_to_m("123", 3, 5))
    print(convert_n_to_m(123, 4, 1))
    print(convert_n_to_m(-123.0, 11, 16))
    print(convert_n_to_m("A1Z", 36, 16))
    print(convert_n_to_m('ZZZZ', 36, 13))
    print(convert_n_to_m('qweasd', 33, 36))
    print(convert_n_to_m('123123123123123123123', 11, 16))
    print(convert_n_to_m(123123123123123123123, 11, 16))
