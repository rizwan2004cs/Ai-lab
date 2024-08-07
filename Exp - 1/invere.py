def main():
    m,n = map(int,input("Enter the row size of the matrix in the form m*n : ").split("*"))
    matrix = inpt(m,n)
    print("the given matrix is ")
    print_matrix(matrix)
    inverse = inverseof(matrix)
    print("the inverse of  matrix is ")
    print_matrix(inverse)
    
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def minor_matrix(matrix,i,j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

def determinants(matrix):
    if(len(matrix) ==2):
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] 
    else:
        determinant = 0
        for c in range(len(matrix)):
            cofactor = ((-1)**c)*matrix[0][c]*determinants(minor_matrix(matrix,0,c))
            determinant += cofactor
    return determinant
def inverseof(matrix):
    determinant = determinants(matrix)
    if(len(matrix) == 2):
        return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]
    cofactor_mat  = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            cofactor_row = []
            minor = minor_matrix(matrix,row,col)
            cofactor = ((-1)**(row+col))*determinants(minor)
            cofactor_row.append(cofactor)
        cofactor_mat.append(cofactor_row)

    trans_cofactor  = transpose(cofactor_mat)
    inverse = []
    for row in range(len(trans_cofactor)):
        inverse_row = []
        for col in range(len(trans_cofactor[0])):
            inverse_row.append((trans_cofactor[row][col]/determinant) if determinant!= 0 else 0)
        inverse.append(inverse_row)
    return inverse
     
def inpt(m,n):
    print("Enter the elements of matrix:")
    mat  = [[None for i in range(n)] for _  in range(m)]
    for i in range(m):
        for j in range(n):
            mat[i][j] = int(input())
    return mat

def print_matrix(matrix):
    for row in matrix:
        for ele in row:
            print(ele,end=" ")
        print()
if __name__ == "__main__":
    main()
