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
        s = "".join(filter(str.isalnum, s))
        left, right = 0, len(s) - 1
        while(left < right):
            left_char = s[left]
            right_char = s[right]
            # if not left_char.isalnum():
            #     left += 1
            # if not right_char.isalnum():
            #     right -= 1
            if right_char != left_char:
                return False
            left += 1
            right -= 1

        return True
            