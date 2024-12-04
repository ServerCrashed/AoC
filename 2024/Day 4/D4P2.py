filepath='2024/Day 4/input.txt'
G=[]
cnt=0
with open(filepath,'r') as f:
    for row in f:
        G.append(row.strip('\n'))
r = len(G)
c = len(G[0])

def DRD(i,j):   #Down-right Diagonal
    if i+2<r and j+2<c and G[i][j]=='M' and  G[i+1][j+1]=='A' and  G[i+2][j+2]=='S':
        return 1
def DLD(i,j):       #Down-left Diagonal
    if i+2<r and j-2>=0 and G[i][j]=='M' and  G[i+1][j-1]=='A' and  G[i+2][j-2]=='S':
        return 1
def ULD(i,j):   #Up-left Diagonal
    if i-2>=0 and j-2>=0 and G[i][j]=='M' and  G[i-1][j-1]=='A' and  G[i-2][j-2]=='S':
        return 1
def URD(i,j):   #Up-right Diagonal
    if i-2>=0 and j+2<c and G[i][j]=='M' and  G[i-1][j+1]=='A' and  G[i-2][j+2]=='S':
        return 1


for i in range (r):
    for j in range(c):
        if DRD(i,j) and DLD(i,j+2):
            cnt+=1
        if DRD(i,j) and URD(i+2,j):
            cnt+=1
        if DLD(i,j) and ULD(i+2,j):
            cnt+=1
        if URD(i,j) and ULD(i,j+2):
            cnt+=1

print(cnt)