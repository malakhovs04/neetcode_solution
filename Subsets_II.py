class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def back(i, subset):
            res.append(subset[::])
        
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                back(j + 1, subset)
                subset.pop()

        back(0, [])
        return res
            