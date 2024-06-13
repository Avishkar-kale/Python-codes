rows = 8

for i in range(1, 5 + 1):
    # Print spaces for the left alignment
    for j in range(rows, i, -1):
        print(" ", end="")

    # Print asterisks for the right alignment
    for k in range(1, i + 1):
        print("*", end="")

    # Move to the next line after each row
    print()
