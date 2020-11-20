import copy 
def scale_matrix(M, m, n, c): 
  N= copy.deepcopy(M)
  arr = []
  for row in range(0,m): #foreach row
      arr.append([])  # append a list inside a list thus creating a list of lists
      for col in range(0,n): #foreach column
          arr[row].append(M[row][col]*c) #append the times c version
  return arr
