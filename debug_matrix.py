# /c:/Users/yvette.muyirukazi/Documents/DSA-HW01---Sparse-Matrix-1/debug_matrix.py
import sys
from SparseMatrix import *

def debug_matrix_operations():
    try:
        # Load matrices
        print("Loading matrix1.txt...")
        matrix1 = SparseMatrix("matrix1.txt")
        print("Matrix 1 loaded successfully")
        print(matrix1)
        
        print("\nLoading matrix2.txt...")
        matrix2 = SparseMatrix("matrix2.txt")
        print("Matrix 2 loaded successfully")
        print(matrix2)
        
        # Perform operations
        print("\nPerforming addition...")
        result_add = matrix1 + matrix2
        print("Addition result:")
        print(result_add)
        
        print("\nPerforming multiplication...")
        result_mult = matrix1 * matrix2
        print("Multiplication result:")
        print(result_mult)
        
        # Save results
        print("\nSaving results...")
        result_add.save("results_add.txt")
        result_mult.save("results_mult.txt")
        print("Results saved successfully")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print(f"Line number: {sys.exc_info()[2].tb_lineno}")

if __name__ == "__main__":
    debug_matrix_operations()