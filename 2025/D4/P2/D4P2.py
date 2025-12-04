INPUT_PATH = "/home/akshat/repos/AoC/2025/D4/input.txt"

# Helpers
def check_up(grid, r, c, h, w):
    if r == 0:
        return False
    return grid[r-1][c] == '@'
def check_diagonal_up_right(grid, r, c, h, w):
    if r == 0 or c == w-1:
        return False
    return grid[r-1][c+1] == '@'
def check_right(grid, r, c, h, w):
    if c == w-1:
        return False
    return grid[r][c+1] == '@'
def check_diagonal_down_right(grid, r, c, h, w):
    if r == h-1 or c == w-1:
        return False
    return grid[r+1][c+1] == '@'
def check_down(grid, r, c, h, w):
    if r == h-1:
        return False
    return grid[r+1][c] == '@'
def check_diagonal_down_left(grid, r, c, h, w):
    if r == h-1 or c == 0:
        return False
    return grid[r+1][c-1] == '@'
def check_left(grid, r, c, h, w):
    if c == 0:
        return False
    return grid[r][c-1] == '@'
def check_diagonal_up_left(grid, r, c, h, w):
    if r == 0 or c == 0:
        return False
    return grid[r-1][c-1] == '@'

helpers = [check_up, check_diagonal_up_right, check_right, check_diagonal_down_right, check_down, check_diagonal_down_left, check_left, check_diagonal_up_left]

def remove_paper_rolls(grid, paper_roll_list):
    for roll in paper_roll_list:
        i = roll[0]
        j = roll[1]
        new_row = grid[i][:j]
        new_row += '.'
        new_row += grid[i][j+1:]
        grid[i] = new_row

def removal_round(rows):
    count_of_accessable_paper_rolls = 0
    list_of_paper_rolls_to_be_removed = []

    for i in range(len(rows)):
        height = len(rows)
        for j in range(len(rows[i])):
            if rows[i][j] != '@':
                continue
            width = len(rows[0])
            # neighbour_count keeps track of adjacent paper rolls
            neighbour_count = 0
            # flag determines whether the paper roll can be accessed
            flag = True

            for helper in helpers:
                neighbour_count += helper(rows, i, j, height, width)
                if neighbour_count > 3:
                    flag = False
                    break
            if flag:
                list_of_paper_rolls_to_be_removed.append((i, j))
                count_of_accessable_paper_rolls += 1
    
    remove_paper_rolls(rows, list_of_paper_rolls_to_be_removed)
    return count_of_accessable_paper_rolls
            

with open(INPUT_PATH, 'r') as f:
    lines = f.readlines()

rows = []
final_count_of_accessable_paper_rolls = 0

for line in lines:
    rows.append(line.strip())

while True:
    round_count = removal_round(rows)
    final_count_of_accessable_paper_rolls += round_count
    if round_count == 0:
        break

print(f"Number of accessable paper rolls: {final_count_of_accessable_paper_rolls}")
