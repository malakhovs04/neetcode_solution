class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        prefix = strs[0]

        for word in strs[1:]:
            while not word[:len(prefix)] == prefix :
                prefix = prefix[:-1]
        return prefix