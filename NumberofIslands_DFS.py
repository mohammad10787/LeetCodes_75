from collections import deque
class Solution:

    def numIslands(self, grid):
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        s = deque()
        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    s.append((row, col))
                    visited.add((row, col))
                    self.DFS(grid, visited,rows, cols, s)
                    islands += 1

        return islands

    def DFS(self, grid, visited, rows, cols, s):
        while s:
            r, c = s.pop()
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for neighbor in neighbors:
                if (neighbor[0] in range(rows) and neighbor[1] in range(cols) and\
                        grid[neighbor[0]][neighbor[1]] == "1" and\
                        (neighbor[0], neighbor[1]) not in visited):
                    visited.add((neighbor[0], neighbor[1]))
                    s.append((neighbor[0], neighbor[1]))
            self.DFS(grid, visited, rows, cols, s)

            return






if __name__ == '__main__':
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    obj = Solution()
    print(obj.numIslands(grid))