# Hash the elements
def de_up_array(nums: list[int]) -> list[int]:
    hashmap = set()
    lst = []

    for i in nums:
        if i not in hashmap:
            lst.append(i)
            hashmap.add(i)

    return lst


print(de_up_array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  # Expected : [1,2,3,4]

print(de_up_array([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]))  # Expected : [0, 1, 4, 5, 8, 9, 10, 11, 15]

print(de_up_array([1, 3, 4, 8, 10, 12]))  # Expected : [1, 3, 4, 8, 10, 12]

# Time Complexity = O(n)
# Space Complexity = O(n)
# Took around 5 minutes
