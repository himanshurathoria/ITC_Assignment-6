from math import factorial
def pascaltriangle(numRows):
    for i in range(numRows):
        for j in range(numRows - i + 1):
            print(end = " ")
        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end = " ")

        print("\n")
pascaltriangle(5)