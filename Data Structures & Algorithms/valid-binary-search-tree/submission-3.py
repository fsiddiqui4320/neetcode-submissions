# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        run dfs
            dfs return min of that subtree, max of that subtree, bool whether subtree is valid or not

        '''
        # if not root:
        #     return False
        # result = True
        # if root.left:
        #     if not root.val > root.left.val or not self.isValidBST(root.left):
        #         return False 
        # if root.right:
        #     if not root.val < root.right.val or not self.isValidBST(root.right):
        #         return False

        # def dfs(node, prev):
        #     if node.left:
        #         dfs(node.left, array)
        #     if len(array) <= 1 and not array[-1] < node.val:
        #         return False
        #     array.append(node.val)
        #     if node.right:
        #         dfs(node.right, array)
        #     return True
        # return dfs(root, float("-inf"))

        def dfs(node, array):
            if node.left:
                if not dfs(node.left, array):
                    return False
            array.append(node.val)
            if len(array) > 1 and array[-1] <= array[-2]:
                return False
            if node.right:
                if not dfs(node.right, array):
                    return False
            return True
        nums = []
        return dfs(root,nums)

        '''
            1
        2       3
        array: [2, 1]
        stack: []
        '''
