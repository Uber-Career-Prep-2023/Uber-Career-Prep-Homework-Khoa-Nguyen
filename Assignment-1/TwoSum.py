#One-directional running computation/total hashing
def two_sum(nums: list[int], k: int) -> int:
    hashmap = set()
    counter = 0

    for i in nums:
        target = k - i

        if target in hashmap:
            counter += 1

        else:
            hashmap.add(i)

    return counter


print(two_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10))  # 3

print(two_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 8))  # 3

print(two_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6))  # 5

print(two_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1))  # 0

# 40 min limit - could not get it to add the same number