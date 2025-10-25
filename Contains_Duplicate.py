<<<<<<< HEAD
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        used = [False] * len(strs)
        
        for i in range(len(strs)):
            if used[i]:
                continue
            
            group = [strs[i]]
            used[i] = True
             
            for j in range(i + 1, len(strs)):
                if used[j]:
                    continue

                if len(strs[i]) == len(strs[j]):
                    count_i = {}
                    count_j = {}

                    for char in strs[i]:
                        count_i[char] = count_i.get(char,0) + 1
                    for char in strs[j]:
                        count_j[char] = count_j.get(char, 0) + 1

                    if count_i == count_j:
                        group.append(strs[j])
                        used[j] = True

        
            result.append(group)
    
        return result
=======
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False
>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
