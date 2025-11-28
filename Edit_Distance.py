class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m
        
        dp = [n - j for j in range(n + 1)]
        
        for i in range(m - 1, -1, -1):
            next_dp = dp[n] 
            dp[n] = m - i    
            for j in range(n - 1, -1, -1):
                temp = dp[j] 
                if word1[i] == word2[j]:
                    dp[j] = next_dp
                else:
                    dp[j] = 1 + min(dp[j],  
                                  dp[j + 1], 
                                  next_dp)    
                next_dp = temp  
        
        return dp[0]