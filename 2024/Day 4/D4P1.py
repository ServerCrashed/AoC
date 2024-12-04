filepath='2024/Day 4/input.txt'
G=[]
cnt=0
with open(filepath,'r') as f:
    for row in f:
        G.append(row.strip('\n'))
r = len(G)
c = len(G[0])

for i in range (r):
    for j in range(c):
        if j+3<c and G[i][j]=='X' and G[i][j+1]=='M' and  G[i][j+2]=='A' and  G[i][j+3]=='S':   #Horizontal
            cnt+=1
        if i+3<r and G[i][j]=='X' and G[i+1][j]=='M' and  G[i+2][j]=='A' and  G[i+3][j]=='S':   #Vertical
            cnt+=1
        if i+3<r and j+3<c and G[i][j]=='X' and G[i+1][j+1]=='M' and  G[i+2][j+2]=='A' and  G[i+3][j+3]=='S':   #Down-right Diagonal
            cnt+=1
        if i+3<r and j-3>=0 and G[i][j]=='X' and G[i+1][j-1]=='M' and  G[i+2][j-2]=='A' and  G[i+3][j-3]=='S':   #Down-left Diagonal
            cnt+=1
        if j-3>=0 and G[i][j]=='X' and G[i][j-1]=='M' and  G[i][j-2]=='A' and  G[i][j-3]=='S':   #Horizontal-Reverse
            cnt+=1
        if i-3>=0 and G[i][j]=='X' and G[i-1][j]=='M' and  G[i-2][j]=='A' and  G[i-3][j]=='S':   #Vertical-Reverse
            cnt+=1
        if i-3>=0 and j-3>=0 and G[i][j]=='X' and G[i-1][j-1]=='M' and  G[i-2][j-2]=='A' and  G[i-3][j-3]=='S':   #Up-left Diagonal
            cnt+=1
        if i-3>=0 and j+3<c and G[i][j]=='X' and G[i-1][j+1]=='M' and  G[i-2][j+2]=='A' and  G[i-3][j+3]=='S':   #Up-right Diagonal
            cnt+=1

print(cnt)