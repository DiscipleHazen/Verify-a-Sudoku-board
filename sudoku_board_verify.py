rows = [input("Input row on Sudoku board: ").strip() for row in range(9)]

rows_verified = 0
columns_verified = 0
squares_verified = 0
ver_example = ['1','2','3','4','5','6','7','8','9']
columns = []
squares = []

for col in range(9):
    strng = ""
    for row in rows:
        strng += row[col]
    columns.append(strng)


for r in range(0, 9, 3):
    for c in range(0, 9, 3):
        sqr = ''
        for i in range(3):
            sqr += rows[r+i][c:c+3]
        squares.append(sqr)

print(squares)


for row in rows:
    if sorted(row) == ver_example:
        rows_verified += 1

for col in columns:
    if sorted(col) == ver_example:
        columns_verified += 1

for square in squares:
    if sorted(square) == ver_example:
        squares_verified += 1



if rows_verified == 9 and squares_verified == 9 and columns_verified == 9:
    print("Valid board.")
else:
    print("Not a valid board.")

