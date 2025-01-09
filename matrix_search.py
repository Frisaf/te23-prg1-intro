matrix = [
    [0, 0, 0],
    [0, 0, 17],
    [0, 0, 0],
]
column = 0
run = 0
check = False

while run < len(matrix):
    for row in matrix:
        if row[column] != 0:
            print(f"Found the anomaly! It was {row[column]}.")
            check = True
            run = len(matrix) + 1

    column += 1
    run += 1

if check == False:
    print("No anomaly found in the matrix.")