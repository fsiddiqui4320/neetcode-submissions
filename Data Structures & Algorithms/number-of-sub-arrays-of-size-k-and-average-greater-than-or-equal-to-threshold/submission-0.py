class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        left pointer, right pointer = 0, k - 1
        currSum = sum of subarray nums[l,r]
        count = 0
        while(r < len(nums)):
            if currSum/k > threshold:
                count += 1
            currSum -= nums[l]
            l += 1
            r += 1
            currSum += nums[r]
        return count
        '''
        currSum = sum(arr[:k-1]) 
        
        count = 0
        for l in range(0,len(arr) - k + 1):
            currSum += arr[l + k - 1]
            if currSum/k >= threshold:
                count += 1
            currSum -= arr[l]
            
            
        return count