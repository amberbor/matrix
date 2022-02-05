class Matrix:
    # initialize object attributes
    def __init__(self, grid):
        self.grid = grid
        self.row_len = len(grid)
        self.col_len = len(grid[0])

    # function numGroup collects all groups of cells
    # return the amount of group that we found
    def numGroup(self):
        group = 0
        # iterate through each cell
        for r in range(0, self.row_len):
            for c in range(0, self.col_len):
                # Check if we found number 1
                if grid[r][c] == 1:
                    # Begin recursion
                    # trigger find function to find the neighbour cell
                    self.find(r, c)
                    group += 1
        return group

    # function find makes it possible to synchronize blocks
    def find(self, r, c):
        # Reassign to 0 so that we dont go over it again
        self.grid[r][c] = 0
        # Set the possible direction of each cell
        directions = [(1, 0), (- 1, 0), (0, - 1), (0, 1)]
        # Loop through the directions that cell will do
        for dr, dc in directions:
            # Set new row and column of neighbour cell
            row_neigbour = r +dr
            col_neigbour = c +dc
            # Check if the index is inside the bounds and check if the neighbour cell is equal to 1
            if 0 <= row_neigbour < self.row_len and 0 <= col_neigbour < self.col_len and grid[row_neigbour][col_neigbour] == 1:
                # We call recursively function find
                self.find(row_neigbour, col_neigbour)


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
