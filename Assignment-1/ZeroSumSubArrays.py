# Growing / Shrinking sliding window

def zero_sum_sub_arrays(arr: list[int]) -> int:
    counter = 0

    for i in range(0, len(arr)):
        for n in range(0, len(arr) - i):
            test = [x for x in arr[n:len(arr) - i]]
            if sum(test) == 0:
                counter += 1

    return counter


input1 = [4, 5, 2, -1, -3, -3, 4, 6, -7]
print(zero_sum_sub_arrays(input1))  # Expected = 2
    
input2 = [1, 8, 7, 3, 11, 9]
print(zero_sum_sub_arrays(input2))  # Expected = 0

input3 = [8, -5, 0, -2, 3, -4]
print(zero_sum_sub_arrays(input3))  # Expected = 2

# Time Complexity = O(n^2)
# Time Complexity = O(n)
# Took around 25 minutes
