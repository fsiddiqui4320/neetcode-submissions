class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(i, cache):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = climb(i+1, cache) + climb(i+2, cache)
            return cache[i]
        return climb(0,{})
