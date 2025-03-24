from SparseMatrix import SparseMatrix

def read_matrix_from_file(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        return SparseMatrix.from_file_content(content)
    except FileNotFoundError:
        print(f"Error: File {filepath} not found")
        return None
    except ValueError as e:
        print(f"Error: {str(e)}")
        return None

def main():
    print("Sparse Matrix Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    
    try:
        choice = int(input("Enter your choice (1-3): "))
        if choice not in [1, 2, 3]:
            print("Invalid choice")
            return

        file1 = input("Enter path to first matrix file: ")
        file2 = input("Enter path to second matrix file: ")

        matrix1 = read_matrix_from_file(file1)
        matrix2 = read_matrix_from_file(file2)

        if not matrix1 or not matrix2:
            return

        result = None
        if choice == 1:
            try:
                result = matrix1.add(matrix2)
                output_file = "results_add.txt"
            except ValueError as e:
                print(f"Error during addition: {str(e)}")
                return
        elif choice == 2:
            try:
                result = matrix1.subtract(matrix2)
                output_file = "results_subtract.txt"
            except ValueError as e:
                print(f"Error during subtraction: {str(e)}")
                return
        else:
            try:
                result = matrix1.multiply(matrix2)
                output_file = "results_mult.txt"
            except ValueError as e:
                print(f"Error during multiplication: {str(e)}")
                return

        with open(output_file, 'w') as file:
            file.write(str(result))
        print(f"Result saved to {output_file}")

    except ValueError:
        print("Invalid input")
        return

if __name__ == "__main__":
    main()
