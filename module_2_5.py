def get_matrix(n, m , value):
  matrix = []
  for i in range(n):
    row = []
    matrix.append(row)
    for j in range(m):
      row.append(value)
  print(matrix)
  return matrix

get_matrix(4, 2, 10)