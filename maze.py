    
from time import sleep

from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for col in range(self._num_cols):
            row_cells = []
            for row in range(self._num_rows):
                row_cells.append(Cell(0, 0, 0, 0, self._win))
            self._cells.append(row_cells)
        for i in range (self._num_cols):
            for j in range (self._num_rows):
                self._draw_cell(i, j)
        
    
    def _draw_cell(self, i, j):
        x1 = self._x1 + i * self._cell_size_x
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        y2 = y1 + self._cell_size_y
        self._cells[i][j] = Cell(x1, x2, y1, y2, self._win)
        self._cells[i][j].draw()
        self._animate()
        
    def _animate(self):
        self._win.redraw()
        sleep(0.05)