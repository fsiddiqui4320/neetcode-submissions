# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        run dfs with a good node counter
        track max node val seen for each path
        for each node visited
            if node none:
                    return 0
            if pathMax <= curr node val:
                increment count or return 1
            return dfs left + dfs right

        return dfs(root, root.val)
        '''
        def dfs(node, pathMax):
            if not node:
                return 0
            if node.val >= pathMax:
                result = 1
            else:
                result = 0
            
            pathMax = max(node.val,pathMax)
            
            return result + dfs(node.left, pathMax) + dfs(node.right, pathMax)
        return dfs(root, -101)
