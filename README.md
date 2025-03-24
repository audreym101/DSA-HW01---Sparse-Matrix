# Sparse Matrix Operations

This project implements basic sparse matrix operations including addition, subtraction, and multiplication using a space-efficient representation.

## File Structure

- `SparseMatrix.py` - Main class implementing sparse matrix operations
- `main.py` - Interactive CLI program to perform matrix operations
- `generate_results.py` - Script to generate sample results
- `matrix1.txt`, `matrix2.txt` - Sample input matrix files
- `results_add.txt`, `results_mult.txt` - Sample output files

## Matrix File Format

Matrix files should follow this format:

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
- Multiplication: O(n*m) where n,m are non-zero elements in
