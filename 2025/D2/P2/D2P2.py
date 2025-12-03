INPUT_PATH = "/home/akshat/repos/AoC/2025/D2/input.txt"

def findRanges(input_path):
    with open(input_path, 'r') as f:
        data = f.read()
        ranges = data.split(',')
        rangeList = []
        for Range in ranges:
            i, j = Range.split('-')
            rangeList.append((i, j))
    return rangeList

def invalid(Id):
        Id_str = str(Id)
        n = len(str(Id))
        for k in range(1, n//2 + 1):
            if n%k == 0:
                p = Id_str[:k]
                if p * (n//k) == Id_str:
                    return True, Id
        return False, None

def findInvalidIDS(rangeList, invalid_id_list):
    for rng in rangeList:
        i, j = int(rng[0]), int(rng[1])
        for Id in range(i, j+1):
            b, v = invalid(Id)
            if b:
                invalid_id_list.append(v)
        
            

def main():
    rngs = findRanges(INPUT_PATH)
    invalidIDS = []
    findInvalidIDS(rngs, invalidIDS)                
    print(sum(invalidIDS))
        

if __name__ == "__main__":
    main()
