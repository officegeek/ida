# Recursion

def printNumber(number):
    print(number)
    if number == 0:
        return 0
    printNumber(number - 1)  # recursive call

printNumber(5)