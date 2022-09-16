import math
from pty import slave_open
from re import A

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class linesegment:
    def __init__(self, p, q):
        self.p = p
        self.q = q

class Polygon:
    def __init__(self, lslist):
        if len(lslist) < 3:
            raise Exception("Side count must be 3 or more.")
        self.lslist = lslist

def dist_2_points(p, q):
    return ((p.x - q.x)**2 + (p.y - q.y)**2)**0.5

def line_2_points(p, q):
    return line(q.y - p.y, p.x - q.x, (q.x - p.x)*p.y - (q.y - p.y)*p.x)

def dist_line_point(l, p):
    return abs(l.a*p.x + l.b*p.y + l.c)/(l.a**2 + l.b**2)**0.5

