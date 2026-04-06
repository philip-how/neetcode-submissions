class Solution:
    def cycle_detect(self, visited, curr_visited, edges, node):
        if curr_visited[node]:
            return True
        
        if visited[node]:
            return False
        
        visited[node] = True
        curr_visited[node] = True
        
        for neighbour in edges[node]:
            if self.cycle_detect(visited, curr_visited, edges, neighbour):
                
                return True

        curr_visited[node] = False
        
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = []
        for i in range(numCourses):
            edges.append([])
        
        for edge in prerequisites:
            edges[edge[0]].append(edge[1])

        visited = [False] * numCourses
        curr_visited = [False] * numCourses

        for i in range(numCourses):
            if self.cycle_detect(visited, curr_visited, edges, i):
                return False
        
        return True
