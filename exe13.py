row1 = ['😀', '😀', '😀']
row2 = ['😀', '😀', '😀']
row3 = ['😀', '😀', '😀']

print(f"{row1}\n{row2}\n{row3}")

matrix = (row1, row2, row3)
position = input("enter your position where you want to hide your money:")
row_position = int(position[0])
column_position = int(position[1])

row_selected = matrix[row_position - 1]
row_selected[column_position - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
