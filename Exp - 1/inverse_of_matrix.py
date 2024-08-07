def transpose_matrix(matrix):
    # Transpose the matrix by switching rows and columns
    return [list(row) for row in zip(*matrix)]

def get_matrix_minor(matrix, i, j):
    # Remove the i-th row and j-th column from the matrix to get the minor
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def get_matrix_determinant(matrix):
    # Base case: calculate the determinant for a 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case: calculate the determinant for matrices larger than 2x2
    determinant = 0
    for c in range(len(matrix)):
        # Compute the cofactor for each element in the first row
        minor = get_matrix_minor(matrix, 0, c)
        cofactor = ((-1) ** c) * matrix[0][c] * get_matrix_determinant(minor)
        determinant += cofactor
    return determinant

def get_matrix_inverse(matrix):
    # Compute the determinant of the matrix
    determinant = get_matrix_determinant(matrix)
    
    # Special case: calculate the inverse for a 2x2 matrix
    if len(matrix) == 2:
        return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]

    # Calculate the cofactor matrix
    cofactors = []
    for r in range(len(matrix)):
        cofactor_row = []
        for c in range(len(matrix)):
            # Compute the minor for each element
            minor = get_matrix_minor(matrix, r, c)
            # Compute the cofactor for each element
            cofactor_row.append(((-1) ** (r + c)) * get_matrix_determinant(minor))
        cofactors.append(cofactor_row)
    
    # Transpose the cofactor matrix
    cofactors = transpose_matrix(cofactors)
    
    # Divide each element by the determinant to get the inverse
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    
    return cofactors

# Example usage
matrix = [
    [4, 7],
    [2, 6]
]

# Compute the inverse of the matrix
inverse = get_matrix_inverse(matrix)

# Print the inverse matrix
for row in inverse:
    print(row)
