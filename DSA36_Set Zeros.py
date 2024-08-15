def setZeroes(matrix: list[list[int]]) -> None:
    # Get the number of rows (m) and columns (n) in the matrix
    m = len(matrix)
    n = len(matrix[0])

    # Initialize two lists to keep track of which rows and columns should be zeroed
    row = [False] * m
    column = [False] * n

    # First pass: Determine which rows and columns need to be zeroed
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    # Second pass: Set the appropriate rows and columns to zero
    for i in range(m):
        for j in range(n):
            if row[i] == True or column[j] == True:
                matrix[i][j] = 0

    # The function modifies the matrix in place, so no return is needed


# Example input
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

# Call the function
setZeroes(matrix)

# Print the modified matrix
print(matrix)

