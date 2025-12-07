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

class Solution:
    def KthMineleBST(self , root:Optional[TreeNode] , k:int) -> int:
        n = 0 
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left 
            curr = stack.pop()
            n += 1 
            if n == k:
                return curr.val
            curr = curr.right 

# Time Complexity - O(H + k) where H is the height of the tree , In worst case (skewed tree): O(N)
# Space Complexity - O(H) for the stack space 


    

