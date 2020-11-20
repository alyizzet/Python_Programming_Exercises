
number_of_lines = int(input())

d = {}
for i in range(0,number_of_lines,1):
    data = input().split(' ')
    key = data[0]
    value = data[1]
    d[value] = key #reversed to get over non duplicate keys. 
    
last = input()

print(list(d.values()).count(d[last]))