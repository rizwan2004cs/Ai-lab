def main():
    m,n = map(int,input("Enter the row size of the matrix in the form m*n : ").split("*"))
    matrix = inpt(m,n)
    print("the given matrix is ")
    print_matrix(matrix)
    trans_mat = transpose(matrix,m,n)
    print("the Transpose of the matrix is ")
    print_matrix(trans_mat)

def inpt(m,n):
    print("Enter the elements of matrix:")
    mat  = [[None for i in range(m)] for _  in range(n)]
    for i in range(m):
        for j in range(n):
            mat[i][j] = int(input())
    return mat

def transpose(mat,m,n):
    print("Enter the elements of matrix:")
    trans_mat  = [[None for i in range(n)] for _  in range(m)]
    for i in range(m):
        for j in range(n):
            trans_mat[i][j] = mat[j][i] 
    return trans_mat

def print_matrix(matrix):
    for row in matrix:
        for ele in row:
            print(ele,end=" ")
        print()
if __name__ == "__main__":
    main()
