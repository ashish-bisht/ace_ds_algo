def count_ways(n):
    if n == 0:
        return 1

    if n == 1:
        return 1

    if n == 2:
        return 2

    return count_ways(n-1)+count_ways(n-2)+count_ways(n-3)


def main():

    print(count_ways(3))
    print(count_ways(4))
    print(count_ways(5))


main()
