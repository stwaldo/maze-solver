from time import sleep
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def draw(self, canvas, fill_color):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)
        
class Cell:
    def __init__(self, x1, x2, y1, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        
    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")
        
    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"
        start_point_x = self._x1 + (self._x2 - self._x1) / 2
        start_point_y = self._y1 + (self._y2 - self._y1) / 2
        start_point = Point(start_point_x, start_point_y)
        end_point_x = to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2
        end_point_y = to_cell._y1 + (to_cell._y2 - to_cell._y1) / 2
        end_point = Point(end_point_x, end_point_y)
        line = Line(start_point, end_point)
        self._win.draw_line(line, line_color)
        
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
                
def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 50, 50, win)
    win.wait_for_close()
    
if __name__ == "__main__":
    main()