def my_max(lst):
  if len(lst)==1:
    return lst[0]
  elif lst[0] > max(lst[1:]):
      return lst[0]
  else:
    return my_max(lst[1:])
            