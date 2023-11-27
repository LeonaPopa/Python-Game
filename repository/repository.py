class Repository:

    def __init__(self, dimension_of_grid):
        self.grid = [[0] * dimension_of_grid for i in range(dimension_of_grid)]
        self.dimension = dimension_of_grid

    def get_value(self, i, j):
        return self.grid[i][j]

    def add_value_to_grid(self, i, j, player):
        if self.grid[i][j] == 0:
            self.grid[i][j] = player

    def make_gray_part(self, i, j):
        if i > 1:
            if j > 1 and self.grid[i - 1][j - 1] == 0:
                self.add_value_to_grid(i - 1, j - 1, 1)
            if self.grid[i - 1][j] == 0:
                self.add_value_to_grid(i - 1, j, 1)
            if j < self.dimension - 1 and self.grid[i - 1][j + 1] == 0:
                self.add_value_to_grid(i - 1, j + 1, 1)
        if j > 1 and self.grid[i][j - 1] == 0:
            self.add_value_to_grid(i, j - 1, 1)
        if j < self.dimension - 1 and self.grid[i][j + 1] == 0:
            self.add_value_to_grid(i, j + 1, 1)
        if i < self.dimension - 1:
            if j > 1 and self.grid[i + 1][j - 1] == 0:
                self.add_value_to_grid(i + 1, j - 1, 1)
            if self.grid[i + 1][j] == 0:
                self.add_value_to_grid(i + 1, j, 1)
            if j < self.dimension - 1 and self.grid[i + 1][j + 1] == 0:
                self.add_value_to_grid(i + 1, j + 1, 1)
