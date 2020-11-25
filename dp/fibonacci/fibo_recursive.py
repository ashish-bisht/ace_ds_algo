def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print("5th Fibonacci is ---> " + str(fibonacci(5)))
    print("6th Fibonacci is ---> " + str(fibonacci(6)))
    print("7th Fibonacci is ---> " + str(fibonacci(7)))


main()
