def binary_map(func_of_2, col1, col2):
  ret = []
  for i in range(len(col1)):
    ret.append(func_of_2(col1[i],col2[i]))

  return iter(ret)