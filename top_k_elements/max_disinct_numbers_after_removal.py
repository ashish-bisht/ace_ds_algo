import heapq
import collections


def find_maximum_distinct_elements(nums, k):

    heap = []

    nums_counter = collections.Counter(nums)
    max_distinct_elements = 0

    for key, val in nums_counter.items():
        if val > 1:
            heapq.heappush(heap, (val, key))
        else:
            max_distinct_elements += 1

    while k > 0 and heap:
        val, char = heapq.heappop(heap)

        if val == 1:
            max_distinct_elements += 1
        else:
            heapq.heappush(heap, (val-1, char))
        k -= 1

    if k == 0:
        return max_distinct_elements
    else:
        return max_distinct_elements - k-1


def main():

    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
