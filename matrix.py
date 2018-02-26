import random

def print_matrix( matrix ):
    output = ""
    for i in matrix:
        for j in i:
            if j < 10:
                output += "   " + str(j)
            elif j < 100:
                output += "  " + str(j)
            else:
                output += " " + str(j)
        output += "\n"
    print output

def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if len(m1[0]) != len(m2):
        print "Matrix multiplication impossible with these 2 matrices."
        return
    mat = new_matrix(len(m1),len(m2[0]))
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for k in range(len(m2)):
                mat[i][j] += m1[i][k] * m2[k][j]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            m2[i][j] = mat[i][j]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def rand(x):
    return random.randint(0,x)

def rand_matrix(rows = 4, cols = 4):
    m = new_matrix()
    for i in range(rows):
        for j in range(cols):
            m[i][j] = rand(20)
    return m
