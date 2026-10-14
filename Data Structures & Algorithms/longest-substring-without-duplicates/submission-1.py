class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        left pointer = 0
        window = set that tracks the chars in the current subarray we're viewing
        longest = 0
        for r in range(nums):
            if nums[r] is in window:
                while nums[r] in window:
                    remove nums[l] from window
                    increment l
            add nums[r] to window
            longest is the max longest and len(window)
        return longest
        '''
        l, longest = 0, 0
        window = set()
        
        for r in range(len(s)):
            if s[r] in window:
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
            window.add(s[r])
            longest = max(longest, len(window))
        return longest