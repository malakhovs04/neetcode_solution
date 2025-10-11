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
                return ans