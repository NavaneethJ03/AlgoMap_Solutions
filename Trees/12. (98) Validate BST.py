class Solution:
    def validateBST(self , root:Optional[TreeNode]) -> bool:
        def valid(root , left , right):
            if not root:
                return True 
            if not(right > node.val and left < node.val):
                return False 
            return (valid(root.right , root.val , right) and 
                    valid(root.left , left , root.val))
        return valid(root , float(-inf) , float(inf))

# Time Complexity - O(N)
# Space Complexity - O(N)
