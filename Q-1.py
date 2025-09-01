def two_sum(nums, target):
    ans = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                ans.append([i,j])
                # store the pair of indices
    return ans

nums=[3,2,3,1,4]
print(two_sum(nums,7))
