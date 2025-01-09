matrix = [
    [7, 12, 19],
    [20, 5, 12],
    [7, 7, 17],
]
column = 0
run = 0

while run < len(matrix):
    column_sum = 0

    for row in matrix:
        column_sum += row[column]

    print(f"Column {run + 1}: {column_sum}")

    column += 1
    run += 1