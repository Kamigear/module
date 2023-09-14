import task
print("1 = odd even")
print("2 = negative/postive number")
print("3 = multiplication")
print("4 = factorial")
answer = int(input("What is your number : "))
value = int(input("what is the value : "))
if answer == 1:
    print(task.oddeven(value))
elif answer == 2:
    print(task.negapos(value))
elif answer == 3:
    print(task.multiplication(value))
elif answer == 4:
    print(task.factorial(value))