class Solution:
    def diameterofTree(self , root:Optional[TreeNode]) -> int:
        self.diameter = float(-inf)
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            self.diameter = max(self.diameter , right + left)
            return max(left , right) + 1
        height(root)
        return self.diameter

# Hint - To find the diameter of a binary tree the answer is sum of left and right height of a node
# Time Complexity - O(n) - since we travel through all the nodes in the tree from bottom to top 
# Space Complexity - O(n) - recursion stack space memory 
            
