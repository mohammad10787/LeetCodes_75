from collections import deque
class Graph:

    def countPaths(self, grid):

        rows = len(grid)
        cols = len(grid[0])
        mod = 10 ** 9 + 7

        def DFS(r, c):

            res = 1
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for dir in directions:
                if r + dir[0] in range(rows) and c + dir[1] in range(cols) and \
                        grid[r + dir[0]][c + dir[1]] > grid[r][c]:
                    res += DFS(r+dir[0], c+dir[1])

            return res




        paths = 0
        for i in range(rows):
            for j in range(cols):
                paths += DFS(i,j)

        return paths%mod






if __name__ == '__main__':
    grid = [[1], [3]]
    s = Graph()
    print(s.countPaths(grid))
