def flood_fill(grid, i, j):
    if grid[i][j] == "#":
        return 0

    count = [0]
    total = dfs(grid, i, j, count)

    return total[0]


def dfs(grid, i, j, count):
    m = len(grid)
    n = len(grid[0])

    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "+" or grid[i][j] == "#":
        return

    if grid[i][j] == "D":
        count[0] += 1

    grid[i][j] = "+"
    dfs(grid, i + 1, j, count)
    dfs(grid, i - 1, j, count)
    dfs(grid, i, j + 1, count)
    dfs(grid, i, j - 1, count)

    return count


def create_new_matrix(grid):
    m = len(grid)
    n = len(grid[0])

    matrix = [[0 for x in range(n)] for y in range(m)]
    for i in range(m):
        for j in range(n):
            matrix[i][j] = grid[i][j]

    return matrix

read_list = [["input6a.txt", "output6a.txt"], ["input6b.txt", "output6b.txt"], ["input6c.txt", "output6c.txt"], ["input6d.txt", "output6d.txt"], ["input6e.txt", "output6e.txt"], ["input6f.txt", "output6f.txt"], ["input6g.txt", "output6g.txt"]]

for num in read_list:
    r = open(num[0], 'r')
    w = open(num[1], 'w')

    first = r.readline().split()
    matrix = []

    for x in range(int(first[0])):
        second = r.readline()
        store = []
        for y in second:
            if y != "\n":
                store.append(y)
        matrix.append(store)

    total_diamond = 0
    for i in range(int(first[0])):
        for j in range(int(first[1])):
            matrix1 = create_new_matrix(matrix)
            total = flood_fill(matrix1, i, j)
            if total > total_diamond:
                total_diamond = total

    w.write(str(total_diamond))
    w.close()






