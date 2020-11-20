num  = int(input())

output = ""
for i in range(1,num+1):
  if i**2 <= num:
    output = output + str(i**2)
    
print(output)