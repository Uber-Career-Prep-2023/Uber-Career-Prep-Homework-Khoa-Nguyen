# sort and solve
# assuming that if it is = it is in the same interval
def merge_intervals(pairs: list[tuple]) -> list[tuple]:
    pairs.sort()
    current = list(pairs[0])
    lst = []
    r = 0

    while r <= len(pairs)-1:

        if pairs[r][0] <= current[1] < pairs[r][1]:
            current = [current[0], pairs[r][1]]
            r += 1

        elif current[1] >= pairs[r][1]:
            r += 1

        else:
            lst.append(current)
            current = [pairs[r][0], pairs[r][1]]
            r += 1

    lst.append(current)

    tuple_convert = [tuple(i) for i in lst]

    return tuple_convert











print(merge_intervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))  # [(4, 8), (1, 3), (9, 12)]

print(merge_intervals([(5, 8), (6, 10), (2, 4), (3, 6)]))  # [(2, 10)]

print(merge_intervals([(10, 12), (5, 6), (7, 9), (1, 3)]))  # [(10, 12), (5, 6), (7, 9), (1, 3)]

# Time Complexity O(n log(n))
# Space Complexity O(n)
# Took about a little over 40 min