class Solution:
    def dfs_visiting(self, root, visited, adj_list):
        if visited[root]:
            return

        visited[root] = True
        
        for neighbour in adj_list[root]:
            self.dfs_visiting(neighbour, visited, adj_list)

        return

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = []
        for i in range(n):
            adj_list.append([])

        for edge in edges:
            adj_list[edge[0]].append(edge[1]) 
            adj_list[edge[1]].append(edge[0]) 

        visited = [False] * n

        cycles = 0
        
        for i in range(n):
            if visited[i]: 
                continue
            self.dfs_visiting(i, visited, adj_list)
            cycles += 1
        
        return cycles
            
            