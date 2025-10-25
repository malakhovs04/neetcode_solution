<<<<<<< HEAD
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        total = 1
            
        for num in nums:
            total *= num

        result = []    

        for i in range(n):
            if nums[i] != 0:
                result.append(total//nums[i])
            else:
                total_0 = 1
                for j in range(n):
                    if j != i:
                        total_0 *= nums[j]
                result.append(total_0)

=======
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        total = 1
            
        for num in nums:
            total *= num

        result = []    

        for i in range(n):
            if nums[i] != 0:
                result.append(total//nums[i])
            else:
                total_0 = 1
                for j in range(n):
                    if j != i:
                        total_0 *= nums[j]
                result.append(total_0)

>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
        return(result)