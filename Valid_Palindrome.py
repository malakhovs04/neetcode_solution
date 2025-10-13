class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtred = []
        for char in s:
            if char.isalnum():
                filtred.append(char.lower())
        clean = ''.join(filtred)

        left = 0
        right = len(clean) - 1

        while left < right: 
            if clean[left] != clean[right]:
                return False
            left += 1
            right -=1

        return True