<<<<<<< HEAD
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

=======
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

>>>>>>> 9dda5c45882b8ba8978b316d89ef05360b56d51d
        return True