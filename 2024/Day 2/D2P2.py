safe=0

def is_safe(report):
    order=False
    c=0
    previous=None
    temp=[]
    for n in report.split():
        temp.append(int(n))
    report=temp
    
    if report == sorted(report) or report == sorted(report, reverse=True):
        order=True
        for level in report:
                if previous is not None:
                    if abs(int(level)-int(previous))>=1 and abs(int(level)-int(previous))<=3:
                        c+=1
                    else:
                        c=0
                        break
                    previous=level
                else:
                    previous=level
    if order==True and c!=0:
        return True

def is_kinda_safe(report):
    order=False
    c=0
    previous=None
    if report == sorted(report) or report == sorted(report, reverse=True):
        order=True
        for level in report:
                if previous is not None:
                    if abs(int(level)-int(previous))>=1 and abs(int(level)-int(previous))<=3:
                        c+=1
                    else:
                        c=0
                        break
                    previous=level
                else:
                    previous=level
    if order==True and c!=0:
        return True

file_path = 'input.txt'
with open(file_path, 'r') as file:
    for row in file:
        if is_safe(row): #Safe
                safe+=1
        else: #Unsafe
            temp=[]
            for n in row.strip().split():
                temp.append(int(n))
            row=temp
            for i in range(len(row)):   
                mod_rep=row[:i]+row[i+1:]
                if is_kinda_safe(mod_rep):
                    safe+=1
                    break

print(safe)
        
