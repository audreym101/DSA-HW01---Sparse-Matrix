from SparseMatrix import SparseMatrix

def read_matrix_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return SparseMatrix.from_file_content(content)

# Read input matrices
matrix1 = read_matrix_file('matrix1.txt')
matrix2 = read_matrix_file('matrix2.txt')

# Perform multiplication
mult_result = matrix1.multiply(matrix2)
with open('results_mult.txt', 'w') as file:
    file.write(str(mult_result))

# Perform addition
add_result = matrix1.add(matrix2)
with open('results_add.txt', 'w') as file:
    file.write(str(add_result))
