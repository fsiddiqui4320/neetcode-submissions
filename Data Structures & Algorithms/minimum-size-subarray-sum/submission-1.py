class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        left pointer = 0
        minLen = len(nums)
        for r in range(len(nums)):
            if sum of current subarray >= target:
                check if curr subarray length < minLen
                if so, set minLen to current length
                l = r
            if sum 
        '''
        l, currSum = 0, 0
        minLen = len(nums) + 1
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minLen = min(minLen, r - l + 1)
                currSum -= nums[l]
                l += 1
            
        return 0 if minLen == len(nums) + 1 else minLen
        