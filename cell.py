
from graphics import Line, Point

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
    