
import heapq


def find_closest_elements(nums, k, X):
    result = []
    heap = []

    for num in nums:
        heapq.heappush(heap, (abs(X-num), num))

    for _ in range(k):
        result.append(heapq.heappop(heap)[1])

    return result


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
