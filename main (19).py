X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]

it_squared_mapping = zip((x**2 for x in X),Y) 

for x in it_squared_mapping: 
  print(x[0], x[1])