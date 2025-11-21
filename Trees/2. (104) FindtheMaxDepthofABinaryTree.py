# Solution - 1 Using Recursive Depth First Search 

class Solution:
  def maxDepth(self , root:Optional[Treenode]) -> int:
    if not root:
      return 0 
    right = self.maxDepth(root.right) # this function calling enables the recursive calling of the right nodes 
    left = self.maxDepth(root.left) # Likewise this function enables the recursive calling of left nodes untill it reaches till the leaf nodes 
    # Basically both the variables keep on incrementing by 1 on reaching another level in the deep
    return max(right , left) + 1  # this is where the increments are being added

# Time Complexity - O(n) since it travels through all the 'n' nodes in the tree 
# Space Complexity - O(n) since we use recursion to solve this problem , the recursion stack space the values of O(n)

# Solution - 2 Using Breadth First Search 

class Solution:
  def maxDepth(self , root: Optional[TreeNode]) -> int:
    if not root:
      return 0 
    q = deque([root]) # here we use [] to surround the root because root is not just a single value it is a collection values , that is it is an object.
    level = 0 
    while q:
      for i in range(len(q)): # Here we parse the range as len of q because to not attend the potential next level nodes which are to be evaluated in the next iteration.
        node = q.popleft() # Firstly we will pop the left most value i.e ,. the first inserted values 
        if node.right # then we check whether they have a right child or not and if they do have a right child then append it to the queue
          q.append(node.right)
        if node.left: # similarly then we check whether they have a left child or not and if they have a left child then append it to the queue 
          q.append(node.left)
      level += 1  # once the for loop is over it signifies that a level is over and the value of increment for that level is incremented in here 
    return level # Then finally we return the level of the Binary Tree 

# Time Complexity - O(n) - since it takes into account of all the tree nodes going in level order 
# Space Complexity - O(n) - since we use a double ended queue to implement the BFS 

# Solution - 3 Using Iterative Depth First Search 

class Solution:
  def maxDepth(self , root : Optional[TreeNode]) -> int:
    if not root:
      return 0
    stk = [[root , 1]] # Here in the iterative approach , use a stack data structure to implement the DFS 
    res = 0 # also we take a level as int in the stack object to track the depth 
    while stk: 
      node , depth = stk.pop() # Intially we pop the top node and then get the value elements of that particular node that is their children in the stack.
      res = max(res , depth) 
      if node.right: # We check is there's an right node to that particular node and if present we add it to the stack and simultaneously increase the depth by e1
        stk.append([node.right , depth + 1])
      if node.left: # Similarly what we did to the right nodes , we do the same to the left nodes also 
        stk.append([node.left , depth + 1])
        
    return res 


# Time Complexity - O(n) 
# Space Complexity - O(n)












    
