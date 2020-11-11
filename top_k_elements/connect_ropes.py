import heapq


def minimum_cost_to_connect_ropes(ropeLengths):
    heapq.heapify(ropeLengths)
    min_cost = 0

    while len(ropeLengths) >= 2:
        first_part = heapq.heappop(ropeLengths)
        second_part = heapq.heappop(ropeLengths)
        new_part = first_part + second_part
        min_cost += new_part
        heapq.heappush(ropeLengths, new_part)
    return min_cost


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
