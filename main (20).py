Xstrs = input().split()
X = [int(x) for x in Xstrs]

Ystrs = input().split()
Y = [int(x) for x in Ystrs]

Z = [(x,y) for x in X for y in Y if x < y] 

for pair in Z: 
  print(pair[0], pair[1])