import time

def print_su(su):
    # Print Your Sudoku:
    print("   1  2  3  4  5  6  7  8  9")
    for i in range(9):
        print(f"{i+1} {su[i]}")

def loc(su):
    for i in range(9):
        for j in range(9):
            if su[i][j] == 0:
                return (i, j)
    return False

def check_num(su, n, row, col):
# Check Row
    for i in range(len(su)):
        if su[row][i] == n and i != col:
            return False

# Check Column
    for i in range(len(su)):
        if su[i][col] == n and i != row:
            return False

# Check Cubes
    for i in range(3):
        for j in range(3):
            r = (row // 3) * 3 + i
            c = (col // 3) * 3 + j
            if su[r][c] == n and r != row and c != col:
                return False
    return True


# solve
def solve(su):
    location = loc(su)
    if location == False:
        print("Solved!")
        return True
    r0, c0 = location

    for num in range(1,10):
        if check_num(su, num, r0, c0):
            su[r0][c0] = num
            if solve(su): # loop until returns True
                return True
            su[r0][c0] = 0
# Split decide the value and put the value to certain cell


# Type in Sud0ku
def enter_su():
    print("Please enter your sudoku:")
    sudoku = []
    for i in range(9):
        line = list(input(">"))
        if len(line) != 9:
            line = []
            print(f"Please re-enter line {i+1}:")
            line = list(input(">"))
        sudoku.append(line)
        for j in range(9):
            sudoku[i][j] = int(sudoku[i][j])

    print_su(sudoku)

    print("\nPlease check your sudoku")
    print("Is it the Sudoku you want to solve?\nInput y for yes:")

    if input() == "y":
        print("\nProcessing:")
    else:
        enter_su()
    return sudoku
    #print_su(sudoku)

sudoku = enter_su()
start = time.time()
solve(sudoku)
end = time.time()
t = round(end - start, 6)
print_su(sudoku)
print(f"\nIt took {t} seconds to solve the Sudoku")
