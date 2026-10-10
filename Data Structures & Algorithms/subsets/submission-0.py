class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        subset = []
        if not nums:
            return result

        def dfs(i):
            if i >= n:
                result.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
                
        dfs(0)

        return result
