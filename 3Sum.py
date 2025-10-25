<<<<<<< HEAD
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums: 
            count[num] += 1
        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i -1]:
                continue
            
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                summ = -(nums[i] + nums[j])
                if count[summ] > 0:
                    res.append([nums[i], nums[j], summ])

            for j in range (i+1, len(nums)):
                count[nums[j]] += 1
        return res
            
=======
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums: 
            count[num] += 1
        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i -1]:
                continue
            
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                summ = -(nums[i] + nums[j])
                if count[summ] > 0:
                    res.append([nums[i], nums[j], summ])

            for j in range (i+1, len(nums)):
                count[nums[j]] += 1
        return res
            
>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
        