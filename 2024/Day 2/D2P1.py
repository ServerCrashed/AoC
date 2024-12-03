safe=0
order=False
file_path = 'input.txt'
with open(file_path, 'r') as file:
    for report in file:
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

        if order==1 and c!=0:
            safe+=1

print(safe)
        
