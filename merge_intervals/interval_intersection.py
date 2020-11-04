def merge(intervals_a, intervals_b):
    result = []

    interval_a_index, interval_b_index = 0, 0

    while interval_a_index < len(intervals_a) and interval_b_index < len(intervals_b):
        start_a, end_a = intervals_a[interval_a_index]
        start_b, end_b = intervals_b[interval_b_index]

        if start_a<=end_b and start_b<=end_a: #### cris cross lock
            result.append([max(start_a, start_b), min(end_a, end_b)]) 

        if end_a <= end_b:
            interval_a_index +=1

        else:
            interval_b_index +=1

    return result


print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))
