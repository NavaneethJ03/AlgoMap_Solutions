class Solution:
    def pathSum(self , Optional[TreeNode] , target: int) -> bool:
        def dfs(root , currsum):
            if not root:
                return False
            currsum += root.val
            if not root.right and not root.left:
                return currsum == target
            return dfs(root.left , currsum) or dfs(root.right , currsum)
         return dfs(root , 0)
# Time Complexity - O(N) since we traverse through all the nodes
# Space Complexity - O(N) due to the recursion stack space
        
