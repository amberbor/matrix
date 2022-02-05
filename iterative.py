from collections import deque

class Matrix:

    # initialize object attributes
    def __init__(self, grid):
        self.grid = grid
        self.row_len = len(grid)
        self.col_len = len(grid[0])

    # function numGroup collects all groups of cells
    # return the amount of group that we found
    def numGroup(self):
        q = deque()
        group = 0
        # iterate through each cell
        for r in range(self.row_len):
            for c in range(self.col_len):
                # Check if we found number 1 and then
                if grid[r][c] == 1:
                    group += 1
                    # Set the cells that we already found as 0 to not call them again
                    grid[r][c] = 0
                    self.find(q, r, c)

        return group

    def find(self, q, r, c):
        # Adding in Queue the cells with value 1 we found
        q.append([r, c])
        # While Loop until Queue is not empty
        while len(q):
            # We delete the current cell from Queue
            current = q.popleft()
            # Find the current row, col of the current cell
            row = current[0]
            col = current[1]
            # Set the possible direction of each cell
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            # Loop through directions that cell will do
            for dr, dc in directions:
                # Set new row and column of neighbour cell
                row_neighbour = row + dr
                col_neighbour = col + dc
                # Check if the index is inside the bounds and check if the neighbour cell is equal to 1
                if 0 <= row_neighbour < self.row_len and 0 <= col_neighbour < self.col_len and grid[row_neighbour][
                    col_neighbour] == 1:
                    # Adding in Queue the neighbours cells with value 1 we found
                    q.append([row_neighbour, col_neighbour])
                    # Set the neighbour cell as 0
                    grid[row_neighbour][col_neighbour] = 0

if __name__ == '__main__':
    grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]

    res = Matrix(grid).numGroup()
    print("We have", res, "connected group on this Matrix")
