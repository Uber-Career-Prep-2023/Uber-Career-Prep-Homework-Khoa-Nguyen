def max_mean_sub_array(nums: list[int], chunk: int) -> int:
    largest = (sum(nums[0:0+chunk]))/chunk

    for i in range(1,len(nums)-chunk+1):
        if (sum(nums[i:i+chunk]))/chunk > largest:
            largest = (sum(nums[i:i+chunk]))/chunk

    return largest


nums1 = [4, 5, -3, 2, 6, 1]
chunk1 = 2
print(max_mean_sub_array(nums1, chunk1)) #expected = 4.5

nums2 = [4, 5, -3, 2, 6, 1]
chunk2 = 3
print(max_mean_sub_array(nums2, chunk2)) #expected = 3

nums3 = [1, 1, 1, 1, -1, -1, 2, -1, -1]
chunk3 = 3
print(max_mean_sub_array(nums3, chunk3)) #expected = 1

nums4 = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
chunk4 = 5
print(max_mean_sub_array(nums4, chunk4)) #expected = 1

# Time Complexity = O(n)
# Space Complexity = O(n)
