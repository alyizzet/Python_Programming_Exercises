import numpy as np 

import numpy as np 


def matrix_max_index(M,m,n):
  max_val = np.max(M)

  for row in range(0,m):
  #  x = 0 
    for col in range(0,n):
   #   y = 0 
      if M[row][col] != max_val:
        col = col + 1
      else: 
        return row,col 
      

