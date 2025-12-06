# Using the Brute Force Approach 

from collections import deque
class Solution:
    def KthMineleBST(self , root:Optional[TreeNode] , k:int) -> int:
        self.result = []
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            self.result.append(root.val)
            inorder(root.right)
        inorder(root)
        return self.result[k-1]

# Time Complexity - O(N) 
# Space Complexity - O(N)

# Using the Iterative Approach - Optimal approach 

