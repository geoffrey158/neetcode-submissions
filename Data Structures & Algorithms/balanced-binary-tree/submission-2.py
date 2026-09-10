# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            #Base case: an empty tree is balanced, with a height of 0
            if root is None:
                #boolean and height 
                return [True,0]
                
            # Recursively check the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # A node is balanced if:
            # 1. both its left and right subtrees are balanced (left[0] and right[0])
            # 2. the difference in height between left and right is at most 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 

            #checks if tree is balanced root,right and left subtree is balanced all 3 conditions 
            return [balanced, 1 + max(left[1],right[1])]
    
        #return the boolean of root 
        return dfs(root)[0] 
