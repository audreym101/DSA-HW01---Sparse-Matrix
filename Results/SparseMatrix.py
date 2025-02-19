import os

class SparseMatrix:
    def __init__(self, file_path=None, rows=0, cols=0):
        """Initialize a sparse matrix, either from a file or with given dimensions."""
        self.rows = rows
        self.cols = cols
        self.data = {}  

        if file_path:
            self.load_from_file(file_path)

    def load_from_file(self, file_path):
        """Load a sparse matrix from a file."""
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                self.rows = int(lines[0].split("=")[1].strip())
                self.cols = int(lines[1].split("=")[1].strip())

                for line in lines[2:]:
                    if line.strip():
                        row, col, value = map(int, line.strip("()\n").split(","))
                        self.set_element(row, col, value)
        except Exception as e:
            print(f"Error loading matrix from {file_path}: {e}")

    def set_element(self, row, col, value):
        """Set an element in the matrix."""
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]  

    def get_element(self, row, col):
        """Retrieve an element; default to zero if not found."""
        return self.data.get((row, col), 0)

    def add(self, other):
        """Add two matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition.")
        
        result = SparseMatrix(rows=self.rows, cols=self.cols)
        result.data = self.data.copy()

        for (row, col), value in other.data.items():
            result.set_element(row, col, result.get_element(row, col) + value)

        return result

    def subtract(self, other):
        """Subtract another matrix from this one."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction.")

        result = SparseMatrix(rows=self.rows, cols=self.cols)
        result.data = self.data.copy()

        for (row, col), value in other.data.items():
            result.set_element(row, col, result.get_element(row, col) - value)

        return result

    def multiply(self, other):
        """Multiply two matrices."""
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions are incompatible for multiplication.")

        result = SparseMatrix(rows=self.rows, cols=other.cols)

        for (row, col), value in self.data.items():
            for k in range(other.cols):
                if (col, k) in other.data:
                    result.set_element(row, k, result.get_element(row, k) + value * other.data[(col, k)])

        return result

    def save_to_file(self, file_path):
        """Save the matrix to a file."""
        try:
            with open(file_path, "w") as file:
                file.write(f"rows={self.rows}\n")
                file.write(f"cols={self.cols}\n")
                for (row, col), value in self.data.items():
                    file.write(f"({row}, {col}, {value})\n")
            print(f"Result saved to {file_path}")
        except Exception as e:
            print(f"Error saving matrix: {e}")


def main():
    """Interactive CLI for performing matrix operations."""
    matrix1_path = input("Enter first matrix file path: ").strip()
    matrix2_path = input("Enter second matrix file path: ").strip()
    output_dir = input("Enter output directory: ").strip()

    if not os.path.isdir(output_dir):
        print("Error: Invalid directory.")
        return

    try:
        matrix1 = SparseMatrix(matrix1_path)
        matrix2 = SparseMatrix(matrix2_path)

        while True:
            print("\nChoose an operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Exit")
            choice = input("Enter choice: ").strip()

            if choice in ["1", "2", "3"]:
                filename = input("Enter the output filename (without extension): ").strip()
                output_path = os.path.join(output_dir, f"{filename}.txt")

                if choice == "1":
                    result = matrix1.add(matrix2)
                elif choice == "2":
                    result = matrix1.subtract(matrix2)
                elif choice == "3":
                    result = matrix1.multiply(matrix2)

                result.save_to_file(output_path)

            elif choice == "4":
                print("Exiting.")
                break
            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
