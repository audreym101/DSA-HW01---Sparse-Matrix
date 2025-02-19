class Pair:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

class SparseMatrix:
    def __init__(self, numRows=None, numCols=None, matrixFilePath=None):
        self.numRows = numRows
        self.numCols = numCols
        self.elements = {}
        
        if matrixFilePath is not None:
            self.loadFromFile(matrixFilePath)

    def loadFromFile(self, filePath):
        with open(filePath, 'r') as reader:
            self.numRows = int(reader.readline().split("=")[1])
            self.numCols = int(reader.readline().split("=")[1])
            
            for line in reader:
                line = line.strip()
                if line:
                    if line[0] != '(' or line[-1] != ')':
                        raise ValueError("Input file has wrong format")
                    
                    parts = line[1:-1].split(",")
                    if len(parts) != 3:
                        raise ValueError("Input file has wrong format")
                    
                    row = int(parts[0].strip())
                    col = int(parts[1].strip())
                    value = int(parts[2].strip())
                    
                    self.setElement(row, col, value)

    def getElement(self, row, col):
        return self.elements.get(Pair(row, col), 0)

    def setElement(self, row, col, value):
        key = Pair(row, col)
        if value != 0:
            self.elements[key] = value
        elif key in self.elements:
            del self.elements[key]

    def add(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must be the same for addition")

        result = SparseMatrix(self.numRows, self.numCols)
        for key, value in self.elements.items():
            result.setElement(key.row, key.col, value + other.getElement(key.row, key.col))

        for key, value in other.elements.items():
            if key not in self.elements:
                result.setElement(key.row, key.col, value)

        return result

    def subtract(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must be the same for subtraction")

        result = SparseMatrix(self.numRows, self.numCols)
        for key, value in self.elements.items():
            result.setElement(key.row, key.col, value - other.getElement(key.row, key.col))

        for key, value in other.elements.items():
            if key not in self.elements:
                result.setElement(key.row, key.col, -value)

        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix dimensions are not suitable for multiplication")

        result = SparseMatrix(self.numRows, other.numCols)
        for key, value1 in self.elements.items():
            row1, col1 = key.row, key.col
            for col2 in range(other.numCols):
                value2 = other.getElement(col1, col2)
                if value2 != 0:
                    result.setElement(row1, col2, result.getElement(row1, col2) + value1 * value2)

        return result

    def toFile(self, filePath):
        with open(filePath, 'w') as writer:
            writer.write(f"rows={self.numRows}\n")
            writer.write(f"cols={self.numCols}\n")
            for key, value in self.elements.items():
                writer.write(f"({key.row}, {key.col}, {value})\n")
