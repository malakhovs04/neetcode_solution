<<<<<<< HEAD
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_s = 0
        
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            s = h * w
            max_s = max(max_s, s)
            

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_s
=======
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_s = 0
        
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            s = h * w
            max_s = max(max_s, s)
            

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_s
>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
