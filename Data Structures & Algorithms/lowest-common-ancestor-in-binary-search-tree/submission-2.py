# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #ancestor is allowed to be a descendent of itself 
        #two nodes p and q 
        #if any input node is empty return None 
        if not root or not p or not q:
            return None

        #root is between p and q which means it's the lowest ancestor 
        if(max(p.val,q.val) < root.val): 
            return self.lowestCommonAncestor(root.left,p,q)
        elif(min(p.val,q.val) > root.val):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root

            

