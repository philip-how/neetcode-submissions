class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        children = {}
        parents = {}

        for char in words[0]:
            if char not in parents:
                parents[char] = set()
                children[char] = set()

        for i in range(1, len(words)):
            j = 0
            while j < len(words[i-1]) and j < len(words[i]) and words[i][j] == words[i-1][j]:
                j += 1

            if j >= len(words[i-1]):
                continue

            if j >= len(words[i]):
                return ""
            
            if words[i][j] in children:
                if words[i-1][j] not in children[words[i][j]]:
                    children[words[i][j]].add(words[i-1][j])
            else:
                children[words[i][j]] = {words[i-1][j]}
                parents[words[i][j]] = set()
            
            if words[i-1][j] in parents:
                if words[i][j] not in parents[words[i-1][j]]:
                    parents[words[i-1][j]].add(words[i][j])
            else:
                parents[words[i-1][j]] = {words[i][j]}
                children[words[i-1][j]] = set()
            
            for char in words[i]:
                if char not in parents:
                    parents[char] = set()
                    children[char] = set()
        
        parents_needed = {}
        visited = {}
        active = []
        for key, value in parents.items():
            parents_needed[key] = len(value)
            visited[key] = False
            if len(value) == 0:
                active.append(key)
        
        output = []

        while active:
            curr = active.pop()
            visited[curr] = True
            output.append(curr)
            for child in children[curr]:
                parents_needed[child] -= 1
                if parents_needed[child] <= 0 and not visited[child]:
                    active.append(child)
        
        if len(output) < len(visited):
            return ""

        return "".join(reversed(output))


        # parents needed dict

        #bfs, if parents_needed not fulfilled just postpone until later

