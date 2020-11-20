text = input()

arr = text.split()

last_list =[]
for i in range(0,len(arr)):
  if (i%2 ==0):
    last_list.append(arr[i])

print(*last_list)
