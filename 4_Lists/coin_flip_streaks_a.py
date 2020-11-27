# A first approach to the problem

l = [1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1]
seq = [1,1,,1]


numRep = 0
for i in range(len(l)-2):
    if seq == l[i:i+len(seq)]:
        numRep += 1
print(numRep)