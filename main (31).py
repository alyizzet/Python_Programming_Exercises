def swap_columns(M, m, n, i, j):
  x = 0
  while x < len(M):
    M[x][i], M[x][j] = M[x][j], M[x][i]
    x = x +1
  return print(M)

