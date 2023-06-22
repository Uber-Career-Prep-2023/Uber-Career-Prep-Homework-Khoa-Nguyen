#Method: Sorting
#Time took: ~ 5 minutes

# Time complexity: O(nlogn)
# Space complexity: O(n)

def merge_arr(arr):
    new_arr = []

    for i in arr:
        new_arr += i
    
    new_arr.sort()
    return new_arr

print(merge_arr([[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
 #expected: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

print(merge_arr([[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
#expected: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]