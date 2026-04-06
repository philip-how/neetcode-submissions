class Solution:
    def cycle(self, visited, parent, node, adj_list):
        if visited[node]:
            return True

        visited[node] = True
        
        for neighbour in adj_list[node]:
            if neighbour == parent:
                continue
            if neighbour == node:
                return True
            elif self.cycle(visited, node, neighbour, adj_list):
                return True
        
        return False


    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = []
        for i in range(n):
            adj_list.append([])

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        visited = [False] * n

        if self.cycle(visited, None, 0, adj_list):
            return False

        for visit in visited:
            if not visit:
                return False

        return True
