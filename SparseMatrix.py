import sys
import os

class SparseMatrix:
    def __init__(self, filename=None):
        self.rows = 0
        self.cols = 0
        self.elements = {}  # Dictionary to store non-zero elements
        
        if filename:
            self.load(filename)
    
    def load(self, filename):
        with open(filename, 'r') as file:
            # Read dimensions from first line
            self.rows, self.cols = map(int, file.readline().split())
            
            # Read matrix elements
            for line in file:
                row, col, value = map(float, line.split())
                self.elements[(int(row), int(col))] = value
    
    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(f"{self.rows} {self.cols}\n")
            for (row, col), value in self.elements.items():
                file.write(f"{row} {col} {value}\n")
    
    def __str__(self):
        result = f"Matrix {self.rows}x{self.cols}:\n"
        for (row, col), value in sorted(self.elements.items()):
            result += f"({row}, {col}): {value}\n"
        return result
    
    def __add__(self, other):
        if (self.rows, self.cols) != (other.rows, other.cols):
            raise ValueError("Matrices must have same dimensions for addition")
        
        result = SparseMatrix()
        result.rows, result.cols = self.rows, self.cols
        
        # Add elements from both matrices
        for pos, value in self.elements.items():
            result.elements[pos] = value
        for pos, value in other.elements.items():
            if pos in result.elements:
                result.elements[pos] += value
            else:
                result.elements[pos] = value
        return result
    
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in first matrix must match rows in second matrix")
        
        result = SparseMatrix()
        result.rows, result.cols = self.rows, other.cols
        
        # Perform matrix multiplication
        for (i, k), value1 in self.elements.items():
            for (k2, j), value2 in other.elements.items():
                if k == k2:
                    pos = (i, j)
                    result.elements[pos] = result.elements.get(pos, 0) + value1 * value2
        
        return result

def main():
    if len(sys.argv) != 4:
        print("Error: Incorrect number of arguments")
        print("Usage: python SparseMatrix.py <matrix1_file_path> <matrix2_file_path> <result_directory>")
        print("Example: python SparseMatrix.py matrix1.txt matrix2.txt results")
        sys.exit(1)

    matrix1_path = sys.argv[1]
    matrix2_path = sys.argv[2]
    result_dir = sys.argv[3]

    # Create result directory if it doesn't exist
    os.makedirs(result_dir, exist_ok=True)

    # Read matrices
    matrix1 = SparseMatrix(matrix1_path)
    matrix2 = SparseMatrix(matrix2_path)

    # Add matrices
    result = matrix1 + matrix2

    # Save result
    result_path = os.path.join(result_dir, "result.txt")
    result.save(result_path)

if __name__ == "__main__":
    main()