from display import *
from draw import *
from matrix import *

import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

def rand(x):
    return random.randint(0,x)

# TESTS
id = new_matrix()
ident(id)
print_matrix(id)
m = rand_matrix()
print_matrix(m)
matrix_mult(id, m)
print_matrix(m)

for i in range(50):
    x = rand(500)
    y = rand(500)
    add_edge(matrix, x, y, 0, 250, 500, 0)
    add_edge(matrix, 500-x, y, 0, 250, 500, 0)

draw_lines( matrix, screen, color )
display(screen)
