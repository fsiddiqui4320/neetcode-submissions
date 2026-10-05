# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        given two nodes find common ancestor

        lca = first that sits between p and q

        if current node is less than p or q and greater than the other one, we return that node
        else if it's greater than both, we move to left child and do same check
        else if less than both move to right child and do same check


        '''
        curr = root
        while (curr != None):
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
        return None