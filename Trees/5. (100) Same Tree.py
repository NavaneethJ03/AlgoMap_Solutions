class Solution:
    def sameTree(self , p: Optional[TreeNode] , q: Optional[TreeNode]) -> bool:
        def Same(p , q):
            if not p and not q:
                return True 
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return Same(p.left , q.left) and Same(p.right , q.right)

        return Same(p , q)

# Time Complexity - O(N) 
# Space Complexity - O(N)
