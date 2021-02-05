def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a/b


if __name__ == '__main__':
    a = int(input('a: '))
    b = int(input('b: '))
    print('a + b = ' + str(addition(a, b)))
    print('a - b = ' + str(subtraction(a, b)))
    print('a * b = ' + str(multiplication(a, b)))
    print('a / b = ' + str(division(a, b)))
    
