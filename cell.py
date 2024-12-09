
from graphics import Line, Point

class Cell:
    def __init__(self, win =  None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, "white")
        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, "white")
        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, "white")
                 
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
    