class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]

        for num in nums[1:]:
            if curr_sum < 0 and curr_sum < num:
                curr_sum = num

            else:
                curr_sum += num
            
            max_sum = max(curr_sum, max_sum)
        
        return max_sum