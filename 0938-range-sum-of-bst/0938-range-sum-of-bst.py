# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res=[]
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        #print(res)
        lowind=res.index(low)
        higind=res.index(high)
        if higind>lowind:
            return sum(res[lowind:higind+1])
        else:
            return sum(res[higind:lowind+1])