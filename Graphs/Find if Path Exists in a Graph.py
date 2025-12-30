class Solution:
    def function(self , source:int , destination:int , n:int , edges:List[List[int]]) -> bool:
        if source == destination:
            return True 
        graph = defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set() # Visited Set 
        seen.add(source)
        stack = [source] 
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei_node in graph(node):
                if nei_node not in seen:
                    seen.add(nei_node)
                    stack.append(nei_node)

        return False

# Time Complexity - O(N + E) since we perform a dfs covering all the nodes and the edges
# Space Complexity - O(N + E since we store all the nodes and the edges in the adjacency list 

