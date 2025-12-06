class Solution:
    def subTree(self , root:Optional[TreeNode] , subroot:Optional[TreeNode]) -> bool:
        if not subroot and root:
            return True
        if not root and subroot:
            return False
        if not subroot:
            return True
        if self.Same(root , subroot): # This condition checks for the root of the main tree if not then we check on to the next right and left subtrees
            return True

        return self.Same(root.left , subroot) or self.Same(root.right , subroot)
        
    def Same(self , root1 , root2):
        if not root1 and not root2:
            return True 
        if not root1 or not root2:
            return False 
        if root1.val != root2.val:
            return False
        return self.Same(root1.right , root2.right) and self.Same(root1.left , root2.left)

# Time Complexity - O(N * M) where n is the no of nodes in the main tree and m is no of the nodes in the subtree 
# Space Complexity - O(N + M) due to the recursion stack space 
