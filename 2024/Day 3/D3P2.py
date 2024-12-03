import re
file_path = '2024/Day 3/input.txt'
t=[]
n=[]
s=0
pattern = r"(?:mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"


def extract(text):
    matches=re.findall(pattern,text)
    for i in matches:
        t.append(i)

def c(x):
    x=x[4:-1]
    x=x.split(',')
    return x

def execute(p):
    a,b=p
    return int(a)*int(b)

with open(file_path, 'r') as file:
    for row in file:
        extract(row)

    do=True
    for x in t:
        if x=="do()":
            do=True
            continue
        elif x=="don't()":
            do=False
        if do:
            n.append(c(x))

    for i in n:
        s+=execute(i)

print(s)
