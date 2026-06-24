class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

nums = [2, 7, 11, 15]
target = 9
obj = Solution()
print(obj.twoSum(nums, target))   