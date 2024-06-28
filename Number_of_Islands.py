from collections import deque
class Solution:

    def __init__(self):
        pass

    def NumofIslands(self, grid):
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1" and (row,column) not in visited:
                    visited = self.BFS(row, column, visited, rows, columns)
                    islands += 1
        return f'We have {islands} islands!'

    def BFS(self, row, column, visited, rows, columns):
        q = deque()
        if (row, column) not in visited:
            visited.add((row, column))
        q.append((row, column))

        while q:
            r, c = q.popleft()

            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for neighbor in neighbors:
                if (neighbor[0] in range(rows) and neighbor[1] in range(columns) and
                        grid[neighbor[0]][neighbor[1]] == "1" and
                        (neighbor[0], neighbor[1]) not in visited):
                    visited.add((neighbor[0], neighbor[1]))
                    q.append(neighbor)
        return visited


if __name__ == '__main__':
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    s = Solution()
    print(s.NumofIslands(grid))




