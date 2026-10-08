'''
left and right pointer
strip spaces from string and make lowercase
while (left < right):
    if string left or string right:
        increment the pointer
    if string left = string right:

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # s = "".join(filter(str.isalnum, s))
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[right] != s[left]:
                return False
            left += 1
            right -= 1

        return True
            