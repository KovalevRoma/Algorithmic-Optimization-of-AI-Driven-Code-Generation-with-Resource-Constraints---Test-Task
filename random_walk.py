import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import math


class RandomWalk:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.path = []

    def is_center(self, row, col):
        center_rows = [self.A // 2] if self.A % 2 == 1 else [self.A // 2 - 1, self.A // 2]
        center_cols = [self.B // 2] if self.B % 2 == 1 else [self.B // 2 - 1, self.B // 2]
        return row in center_rows and col in center_cols

    def perform_walk(self):
        start_position = random.choice([(0, 0), (0, self.B - 1), (self.A - 1, 0), (self.A - 1, self.B - 1)])
        current_row, current_col = start_position
        self.path = [(current_row, current_col)]

        while not self.is_center(current_row, current_col):
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            move = random.choice(moves)
            current_row = (current_row + move[0]) % self.A
            current_col = (current_col + move[1]) % self.B
            self.path.append((current_row, current_col))

    def get_path(self):
        return self.path


class PathPlotter:
    def __init__(self, walk: RandomWalk):
        self.walk = walk

    def plot(self):
        A, B = self.walk.A, self.walk.B
        path = self.walk.get_path()
        grid = np.zeros((A, B))

        for idx, (row, col) in enumerate(path):
            grid[row, col] = idx + 1

        mpl.rcParams['toolbar'] = 'None'
        plt.figure(figsize=(16, 16), facecolor="#D87093")
        plt.imshow(grid, cmap="Blues", origin="upper")
        plt.colorbar(label="Order of cell visit")
        plt.title("Random Walk Path", fontsize=20)
        plt.figtext(0.1, 0.02, f"Size of matrix: {A}*{B}\nNumber of steps: {len(path)}\nS: {A*B}\nS logS : {A*B*math.log(A*B):.2f}", wrap=True, horizontalalignment='left', fontsize=14)
        plt.show()


if __name__ == "__main__":
    A = int(input("Enter the number of rows (A): "))
    B = int(input("Enter the number of columns (B): "))
    walk = RandomWalk(A, B)
    walk.perform_walk()
    plotter = PathPlotter(walk)
    plotter.plot()
