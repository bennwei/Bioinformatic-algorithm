import collections

in_file = open('findClump_example.txt','r')
ou_file = open('data_set_out.txt', 'w')

line = 1
genome = "";
k=0
l=0
t=0

for in_data in in_file:
    if (line==1):
        genome = in_data.strip(' \t\n\r')
    elif (line==2):
        in_line2 = (in_data.strip(' \t\n\r')).split()
        k = int(in_line2[0])
        l = int(in_line2[1])
        t = int(in_line2[2])
        line+=1

#print in_genome
print k, l, t

clumps=[]
for j in xrange(len(genome)):
    kstr = genome[j:j+l]
    if (len(kstr)==l):
        patterns = collections.defaultdict(list)
for i in range(0, len(kstr)-k+1):
    c =  kstr[i:i+k]
    if c  not in clumps:
        if c in patterns:
            patterns[c] += 1
            if patterns[c] == t:
                clumps.append(c)
            else:
                patterns[c] = 1
            print clumps