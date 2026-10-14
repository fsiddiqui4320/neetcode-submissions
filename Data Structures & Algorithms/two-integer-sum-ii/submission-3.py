class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        left pointer = 0
        right pointer = len(nums) - 1
        while (l < r):
            sum = left + right
            if sum == target:
                return [left, right]
            elif sum < target:
                increment left
            else:
                decrement right
        return -1
        '''
        l, r = 0, len(numbers) - 1
        while (l < r):
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                l += 1
            else:
                r -= 1
        return []