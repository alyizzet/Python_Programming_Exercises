def my_sum(lst):
  if len(lst) == 1:
    return lst[0]
  else:
    return lst[-1] + my_sum(lst[:-1])