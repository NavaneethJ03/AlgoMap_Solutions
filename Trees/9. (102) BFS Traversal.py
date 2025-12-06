from collections import deque
class Solution:
    def BFS(self , root:Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            ele = []
            for _ in range(len(q)):
                node = q.popleft()
                ele.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(ele)
        return ans

# Time Complexity - O(N) since we are travelling through all the nodes 
# Space Complexity - O(N) since we use the ans array to return the answer
