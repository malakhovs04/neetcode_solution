class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                k += 1
            else:
                k = 1
            if k <= 2:
                nums[res] = nums[i]
                res += 1
        return res