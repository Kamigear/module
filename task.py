def negapos(a):
    if a > 0:
        return "it is positive number"
    elif a == 0:
        return "it is positve number"
    else:
        return "it is negative number"
def oddeven(a):
    if a % 2 == 0:
        return "it is even number"
    else:
        return "it is odd number"
def factorial(a):
    counter = 1
    for i in range(1,a+1):
        counter *= i
    return counter # return counter = print(counter)
def multiplication(a):
    value = 1
    for i in range(1,11):
        value = i * a
    return value

