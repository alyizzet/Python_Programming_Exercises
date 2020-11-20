num = int(input())


count = 0
while num != 0:
  num2 = int(input())
  if num2 > num:
    count = count + 1
  elif num2 ==0:
    break
  num = num2
print(count)