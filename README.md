## Supported Operations

- Addition: Add two sparse matrices
- Subtraction: Subtract two sparse matrices 
- Multiplication: Multiply two sparse matrices
- Display: Print matrix in dense format
- Export: Save matrix to file

## Usage

1. Prepare input matrix files in the correct format
2. Run the program: `python main.py`
3. Choose operation from menu
4. Enter input file paths when prompted
5. View results or check output files

## Performance

This implementation is optimized for matrices where the number of non-zero elements is much smaller than the total number of elements. Time complexity varies by operation:

- Addition/Subtraction: O(n) where n is number of non-zero elements
- Multiplication: O(n*m) where n,m are non-zero elements in each matrix
