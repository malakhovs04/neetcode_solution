class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()

        res = [intervals[0]]

        for current in intervals[1:]:
            last = res[-1]

            if current[0] <= last[1]:
                res[-1][1] = max(last[1], current[1])

            else:
                res.append(current)
        return res