class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        loop through nums and find product of all elements
        loop through again and set output[i] to product/nums[i]
        '''
        
        output = [1] * len(nums)
        prefix = 1
        suffix = 1
        product_no_zero = 1
        for i, num in enumerate(nums):
            output[i] *= prefix
            prefix *= num

            output[-i-1] *= suffix
            suffix *= nums[-i-1]

    

        return output