class Solution:
    def LCA(self , root: Optional[TreeNode] ,p:Optional[TreeNode] , q:Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root , p , q):
            if p.val < root.val and q.val < root.val:
                return helper(root.left , p , q)
            elif p.val > root.val and q.val > root.val:
                return helper(root.right , p , q)
            return root 
        return helper(root , p , q) 

# Time Complexity - O(N)
# Space Complexity - O(N)
