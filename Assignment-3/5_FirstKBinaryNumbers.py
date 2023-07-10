# Used basic python bin() function to convert to binary
# This problem took 5 minutes
# Space Complexity: O(n)
# Time Complexity: O(n)

num = 10
def FirstKBinaryNumbers(k):

    arr = []
    for i in range(k):
        arr.append(f"{bin(i)[2::]}")

    return arr

print(FirstKBinaryNumbers(5))
#expected: ["0", "1", "10", "11", "100"]

print(FirstKBinaryNumbers(10))
#expected: ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]