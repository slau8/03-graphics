from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    i = 0
    while i < len(matrix):
        x0 = matrix[i][0]
        y0 = matrix[i][1]
        x1 = matrix[i+1][0]
        y1 = matrix[i+1][1]
        draw_line(x0, y0, x1, y1, screen, color)
        i += 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    point = [x, y, z, 1]
    matrix.append(point)


def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -1 * (x1 - x0)

    # Switch points
    if x > x1:
        draw_line(x1, y1, x0, y0, screen, color)

    # Octant 1
    elif abs(A) <= abs(B) and A * B <= 0:
        d = 2 * A + B
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A

    # Octant 2
    elif abs(A) >= abs(B) and A * B <= 0:
        d = 2 * B + A
        while y <= y1:
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B

    # Octant 7
    elif abs(A) >= abs(B) and A * B >= 0:
        d = A - 2 * B
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B

    # Octant 8
    elif abs(A) <= abs(B) and A * B >= 0:
        d = 2 * A - B
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A
