INPUT_PATH = "/home/akshat/repos/AoC/2025/D2/input.txt"

def findRanges(input_path):
    with open(input_path, 'r') as f:
        data = f.read()
        ranges = data.split(',')
        rangeList = []
        for Range in ranges:
            temp = Range.split('-')
            rangeList.append((temp[0], temp[1]))
    return rangeList

def findInvalidIDS(rangeList, invalid_id_list):
    for rng in rangeList:
        for i in range(int(rng[0]), int(rng[1])+1):
            if len(str(i))%2 != 0:
                if int(rng[1])%2 == 0:
                    power = len(rng[1]) - 1
                    difference = 10**power - i
                    i += difference
                    continue
                break

            halfIndex = int(len(str(i)) / 2)
            if str(i)[:halfIndex] == str(i)[halfIndex:]:
                invalid_id_list.append(i)

def main():
    rngs = findRanges(INPUT_PATH)
    invalidIDS = []
    findInvalidIDS(rngs, invalidIDS)                
    print(sum(invalidIDS))
        

if __name__ == "__main__":
    main()
