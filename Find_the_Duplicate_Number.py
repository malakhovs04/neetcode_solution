class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 1, n - 1
        while l < r:
            m = l + (r - l) // 2
            cur = sum(1 for num in nums if num <= m)

            if cur <= m:
                l = m + 1
            else:
                r = m
        return l