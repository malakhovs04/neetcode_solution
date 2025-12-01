class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_a = max_b = max_c = 0
        x, y, z = target
    
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                max_a = max(max_a, a)
                max_b = max(max_b, b)
                max_c = max(max_c, c)
    
        return (max_a, max_b, max_c) == (x, y, z)