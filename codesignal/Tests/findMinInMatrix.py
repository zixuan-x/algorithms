def findMinInMatrix(m, n, query):
    result = []
    row, col = 0, 0
    removedRows, removedColumns = set(), set()
    for q in query:
        if q[0] == 0:
            # get min element from matrix
            result.append([row, col])
        elif q[0] == 1:
            # diable a row
            removedRows.add(q[1])
            while row in removedRows and row < m:
                row += 1
        else:
            # diable a column
            removedColumns.add(q[1])
            while col in removedColumns and col < n:
                col += 1
    return result

# print(findMinInMatrix(5, 5, [[0], []]))
