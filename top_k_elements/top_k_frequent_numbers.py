import heapq
import collections


def find_k_frequent_numbers(nums, k):

    top_k_numbers = []

    count_dict = collections.Counter(nums)
    heap = []
    for key, val in count_dict.items():
        heapq.heappush(heap, (-val, key))

    for _ in range(k):
        top_k_numbers.append(heapq.heappop(heap)[1])

    return top_k_numbers


def main():

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
