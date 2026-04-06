class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        length = len(matrix[0])
        height = len(matrix)
        min_quantity = min(len(matrix), len(matrix[0]))

        layers = min_quantity // 2

        output = []

        for layer in range(layers):
            for x in range(layer, length - layer):
                output.append(matrix[layer][x])
            
            for y in range(layer + 1, height - layer):
                output.append(matrix[y][length - layer - 1])
            
            for x in range(length - layer - 2, layer - 1, -1):
                output.append(matrix[height - layer - 1][x])
            
            for y in range(height - layer - 2, layer, -1):
                output.append(matrix[y][layer])
        
        print(output)

        if min_quantity % 2 == 1:
            layer = layers
            if height <= length: 
                for x in range(layer, length - layer):
                    output.append(matrix[layer][x])
            else: 
                for y in range(layer, height - layer):
                    output.append(matrix[y][layer])

        return output
