num = int(input())

seq = []
while (num!= 0):
  seq.append(num)
  num = int(input())
  if(num == 0):
    print(max(seq))