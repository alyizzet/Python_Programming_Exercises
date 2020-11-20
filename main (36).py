many = int(input())
d = {}
for i in range(0,many):
  key_value = input().split(' ')
  d[key_value[0]] = key_value[1]

word = input()
print(d[word])