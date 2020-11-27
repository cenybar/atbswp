# A second approach to the problem (using string methods)

l = ['t','h','t','h','t','t','t','h','t','h','h']
seq = ['h','t','h']


#numRep = 0
#seq_str = ''.join(x for x in seq)
#l_str = seq_str in ''.join(y for y in l)
#
#if seq_str in l_str:
#    numRep += 1
#
#print(numRep)

def in_ist(l1, l2):
    return ''.join(str(x) for x in l1) in ''.join(str(y) for y in l2)

