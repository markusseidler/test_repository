from utils import *

if __name__ == '__main__':
    a = 5
    b = 10

    # print (sum(a, b))
    # print(sub(a, b))

    operations = [sum, sub, div]

    for op in operations:
        print(f"{a} {op.__name__} {b} = {op(a, b)}")

