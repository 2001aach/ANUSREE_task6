# Progaram to calculate the addition of two matrix


X = [[1, 2],
     [3, 4],
     [6, 7]]

Y = [[8,9],
     [10,11],
     [12,13]]

result = [[0, 0],
          [0, 0],
          [0, 0]]

for i in range(len(X)):

    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)