s=set(input().split())

def func(si):
  more_inputs = False 
  count = 1
  while more_inputs == False:
      new_input = input()
    
      if new_input == "END":
        return si
        
      if (count%2 != 0):
          s2=set(new_input.split())
          si = si -s2
      elif (count%2 == 0):
          s3=set(new_input.split())
          si |= s3
      count = count + 1

      
    
print(*sorted(func(s)))

 

"""
def func(s):
  finished = False 
  while finished == False:
      count = 2
      s1 = input()
      if s1 == "END":
        return s 
      elif count%2 != 0:
          s1 = input()
          s2=set(s1.split())
          s = s.difference(s2)
          count = count + 1
      else:
          s1 = input()
          s3=set(s1.split())
          s = s.union(s3)
          count = count + 1
print(*sorted(func(s)))
"""
