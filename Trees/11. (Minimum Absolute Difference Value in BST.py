class Solution:
    def MinAbsDiff(self , root:Optional[TreeNode]) -> int:
        self.prev = None
        self.ans = float(inf)
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            if self.prev != None:
                diff = root.val - self.prev
                self.ans = min(self.ans , diff)
                
            self.prev = root.val 
            inorder(root.right)
        inorder(root)
        return self.ans

# Time Complexity - O(N) since we travel to all the nodes in the BST 
# Space Complexity - O(N) due to recursive stack call space 
