<<<<<<< HEAD
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set_nums = set(nums)
        long = 0 

        for num in set_nums:
            if num - 1 not in set_nums:
                current = num
                con = 1

                while current + 1 in set_nums:
                    current += 1
                    con +=1
                long = max(long, con)
        return long
=======
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set_nums = set(nums)
        long = 0 

        for num in set_nums:
            if num - 1 not in set_nums:
                current = num
                con = 1

                while current + 1 in set_nums:
                    current += 1
                    con +=1
                long = max(long, con)
        return long
>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
