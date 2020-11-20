def stringify(f):
  def F(string):
      l = []   
      for i in range(len(string)):
          ch = f(string[i])
          l.append(ch)
      return ("").join(l)
  return F