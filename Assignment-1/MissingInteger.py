#Two arrays two pointer

def missing_integer(arr: list[int], n: int) -> int:
    for i in range(1,n+1):
        if i not in arr:
            return i


print(missing_integer([1, 2, 3, 4, 6, 7], 7)) # expected = 5

print(missing_integer([1], 2)) # expected = 2

print(missing_integer([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12)) # expected = 9

# Time Complexity = O(n)
# Space Complexity = O(n)
# Took around 10 minutes