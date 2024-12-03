with open('input.txt','r') as f:
    c1=[]
    c2=[]
    for line in f:
        val=line.split()
        c1.append(int(val[0]))
        c2.append(int(val[1]))

print("C1:", c1)
print("C2:", c2)

sim=0
for i in c1:
    c=0
    for j in c2:
        if i==j:
            c+=1
    sim+=(i*c)
print("Similarity score:", sim)
