import math

def print_matrix( matrix ):
    for i in matrix:
        for j in matrix:
            print str(j) + " " 
        print "\n"

def ident( matrix ):
    for i in matrix:
        for j in matrix:
            if matrix.index(i) == i.index(j):
                j = 1
            else:
                j = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

mat =  

print_matrix( mat )
ident( mat )
print_matrix( mat )
