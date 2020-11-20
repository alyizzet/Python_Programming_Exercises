column = int(input())
row = int(input())

for j in range(1,column+1):
  for i in range(1,row+1):
    print(i*j,end=" ")
  print("")