def pascal(row, col):
    if col == 1:
        return 1
    if row == col:
        return 1
    upLeft = pascal(row-1,col-1)
    upRight = pascal(row-1, col)
    return upLeft + upRight



n = 10
for i in range(1, n):
    for j in range(1, i + 1):
        print (pascal(i,j), end = " ")
    print()