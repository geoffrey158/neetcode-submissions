# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):

            if root is None:
                #boolean and height 
                return [True,0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            #left[0] and right[0] - checks if root is balanced 
            #abs(left[1] - right[1]) <=1 - check if left and right node of root is balanced
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 

            #checks if tree is balanced root,right and left subtree is balanced all 3 conditions 
            return [balanced, 1 + max(left[1],right[1])]
    
        #return the boolean of root 
        return dfs(root)[0] 
