num = int(input())


summe = 0
length = 0
while (num!= 0):
  summe += num
  length += 1
  num = int(input())
  if(num ==0):
    print(int(summe/length))