import heapq


def find_k_largest_numbers(nums, k):
    result = []
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)

    for _ in range(k):
        result.append(- heapq.heappop(heap))

    return result


print("Here are the top 3 numbers: " +
      str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

print("Here are the top 3 numbers: " +
      str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))
