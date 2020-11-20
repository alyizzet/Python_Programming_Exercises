from collections import Counter

seq =input().split(' ')

for i in range(0,len(seq)):
    count= Counter(seq[:i])
    print(count[seq[i]])