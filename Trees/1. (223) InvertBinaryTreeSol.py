class Solution:
  def invertTree(self , root:Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return None
      
    root.right , root.left = root.left , root.right
    # so what happens is that we swap the nodes in preorder 
    # then we recursively call all the right nodes of the root so that each and every node calls its right nodes recursively and swap their childs in pre-order 
    # once the call stack reaches the leaf node it returns none and then finally all the functions return their stack value and we end up in swapping all the right
    # nodes of the tree and then we similarly apply this to the left nodes too so that all the nodes in the tree is covered in whole .
    self.invertTree(root.right)
    self.invertTree(root.left)
    # root.right , root.left = root.left , root.right 
    # the swapping is possible even in here 
    
  return root

# Time Complexity - O(n) since we are travesing to all the n nodes in the entire tree 
# Space Complexity - O(n) since the stack space could even go upto storing all the n nodes in worst case or O(log n) if the tree is balanced.
