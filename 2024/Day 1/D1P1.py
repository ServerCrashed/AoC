file_path = 'input.txt'
with open(file_path, 'r') as file:
    column1 = []
    column2 = []
    for line in file:
        values = line.split()
        if len(values) == 2:  # Ensure the line contains exactly two values
            column1.append(int(values[0]))
            column2.append(int(values[1]))

column1.sort()
column2.sort()
print("C1: ", column1)
print("C2: ", column2)

distance=0
for i in range(len(column2)):
    distance+=(abs(column1[i]-column2[i]))

print(distance)