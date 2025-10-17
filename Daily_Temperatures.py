class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = []

        for i in range(len(temperatures)):
            flag = True
            date = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[j] <= temperatures[i]:
                    date +=1
                else:
                    res.append(date)
                    flag = False;
                    break
            if flag:
                res.append(0)
        return res
        