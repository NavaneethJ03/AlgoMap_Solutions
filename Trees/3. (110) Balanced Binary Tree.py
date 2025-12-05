class Solution:
    def balanceTree(self, root:Optional[TreeNode]) -> bool:
        self.balanced = True 
        """ What we do in here is that we perform the height of a tree from the bottom to the top
            and then we check for all the node levels such that whether they are balanced or not 
            if it is not balanced , then we update the global var to false and then we return it.
        """
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            if self.balanced == False: # These are for the purpose of efficient code execution 
                return 0
            right = dfs(root.right)
            if abs(left - right) > 1:
                self.balanced = False
                return 0 # for code efficiency 
                
            return max(left , right) + 1 
        dfs(root)
        return self.balanced
# Hint - Use dfs to find the height of a node and find the abs difference 
# Time Complexity - O(N) since we visit all the nodes one time 
# Space Complexity - O(N) since we use recursion and it takes n space to store the nodes
