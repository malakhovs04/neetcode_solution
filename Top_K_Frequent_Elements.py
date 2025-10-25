<<<<<<< HEAD
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = dict()
        counter = 0
        ans = []
        
        for i in nums:
            if i in data:
                data[i]+= 1
            else:
                data[i]= 1

        for i in sorted(data, key=lambda x: data[x], reverse=True):
            ans.append(i)
            counter+=1

            if counter == k:
=======
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = dict()
        counter = 0
        ans = []
        
        for i in nums:
            if i in data:
                data[i]+= 1
            else:
                data[i]= 1

        for i in sorted(data, key=lambda x: data[x], reverse=True):
            ans.append(i)
            counter+=1

            if counter == k:
>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
                return ans