class Solution:
  def isSymmetric(self , root:Optional[TreeNode]): -> bool:
    def Same(root1 , root2):
      if not root1 and root2:
        return True 
      if not root1 or root2:
        return False
      if root1.val != root2.val:
        return False
      return (
        Same(root1.right , root2.left) and 
        Same(root2.right , root1.left))
    return Same(root , root)
# Time Complexity - O(n)
# Space Complexity - O(n)
