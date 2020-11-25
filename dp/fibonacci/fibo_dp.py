def fibonacci(n):
    dp = [0 for _ in range(n+1)]

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]


def main():
    print("5th Fibonacci is ---> " + str(fibonacci(5)))
    print("6th Fibonacci is ---> " + str(fibonacci(6)))
    print("7th Fibonacci is ---> " + str(fibonacci(7)))


main()
