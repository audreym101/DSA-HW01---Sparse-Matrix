class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.elements = {}  # Dictionary to store non-zero elements

    def set(self, row, col, value):
        if row < 0 or col < 0:
            raise ValueError('Invalid position: row and column must be non-negative')
        if row >= self.rows or col >= self.cols:
            raise ValueError(f'Invalid position: indices ({row},{col}) out of bounds for matrix of size {self.rows}x{self.cols}')
        if value == 0:
            self.elements.pop((row, col), None)
        else:
            self.elements[(row, col)] = value

    def get(self, row, col):
        if row < 0 or col < 0:
            raise ValueError('Invalid position: row and column must be non-negative')
        if row >= self.rows or col >= self.cols:
            raise ValueError(f'Invalid position: indices ({row},{col}) out of bounds for matrix of size {self.rows}x{self.cols}')
        return self.elements.get((row, col), 0)

    def add(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            raise ValueError('Matrix dimensions must match for addition')

        result = SparseMatrix(self.rows, self.cols)
        result.elements = self.elements.copy()

        for (row, col), value in matrix.elements.items():
            result.set(row, col, result.get(row, col) + value)

        return result

    def subtract(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            raise ValueError('Matrix dimensions must match for subtraction')

        result = SparseMatrix(self.rows, self.cols)
        result.elements = self.elements.copy()

        for (row, col), value in matrix.elements.items():
            result.set(row, col, result.get(row, col) - value)

        return result

    def multiply(self, matrix):
        if self.cols != matrix.rows:
            raise ValueError('Number of columns in first matrix must match number of rows in second matrix')

        result = SparseMatrix(self.rows, matrix.cols)
        column_map = {}

        for (row, col), value in matrix.elements.items():
            if row not in column_map:
                column_map[row] = []
            column_map[row].append((col, value))

        for (row1, col1), value1 in self.elements.items():
            for col2, value2 in column_map.get(col1, []):
                result.set(row1, col2, result.get(row1, col2) + value1 * value2)

        return result

    def transpose(self):
        result = SparseMatrix(self.cols, self.rows)

        for (row, col), value in self.elements.items():
            result.set(col, row, value)

        return result

    @staticmethod
    def from_file_content(content):
        lines = [line.strip() for line in content.strip().split('\n')]
        
        # Validate first two lines
        if not lines[0].startswith('rows=') or not lines[1].startswith('cols='):
            raise ValueError("Input file has wrong format")
        
        try:
            rows = int(lines[0].split('=')[1])
            cols = int(lines[1].split('=')[1])
        except:
            raise ValueError("Input file has wrong format")

        if rows <= 0 or cols <= 0:
            raise ValueError('Invalid matrix dimensions')

        matrix = SparseMatrix(rows, cols)

        for line in lines[2:]:
            if not (line.startswith('(') and line.endswith(')')):
                raise ValueError("Input file has wrong format")
                
            # Custom parsing without regex
            try:
                content = line[1:-1].replace(' ', '')
                row, col, value = map(int, content.split(','))
                if 0 <= row < rows and 0 <= col < cols and value != 0:
                    matrix.set(row, col, value)
                else:
                    print(f'Warning: Skipping element at position ({row},{col}) as it is out of bounds or zero')
            except:
                raise ValueError("Input file has wrong format")

        return matrix

    def __str__(self):
        result = f'rows={self.rows}\ncols={self.cols}\n'
        for (row, col), value in self.elements.items():
            result += f'({row}, {col}, {value})\n'
        return result.strip()


import re
