import sys

from ModelMain import  Fibonacci

if __name__ == "__main__":
    f = Fibonacci(10)
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()
