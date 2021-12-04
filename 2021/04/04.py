fp = open('input', 'r')

numbers_called = [int(x) for x in fp.readline().strip().split(",")]

def boards(fp_):
    num_lines = 0
    cur_board = list()

    for line in fp.readlines():
        line = line.strip().replace("  ", " ")
        if line == "": continue

        cur_board += [int(x) for x in line.split(" ")]
        num_lines += 1
        
        if num_lines == 5:
            yield cur_board
            num_lines = 0
            cur_board = list()

def has_bingo(board, numbers):
    assert(len(board) == 25)
    # horizontal
    for x in range(0, 25, 5):
        if (board[x+0] in numbers and \
            board[x+1] in numbers and \
            board[x+2] in numbers and \
            board[x+3] in numbers and \
            board[x+4] in numbers):
            return True

    for x in range(0, 5):
        if (board[x+0*5] in numbers and \
            board[x+1*5] in numbers and \
            board[x+2*5] in numbers and \
            board[x+3*5] in numbers and \
            board[x+4*5] in numbers):
            return True
    
    return False

BOARDS = [x for x in boards(fp)]

def solve1():
    for idx, number in enumerate(numbers_called):
        for board in BOARDS:
            if has_bingo(board, numbers_called[:idx]):
                n = set(numbers_called[:idx])
                b = set(board)

                return sum(b-n) * numbers_called[idx-1]

def solve2():
    for idx, number in enumerate(numbers_called):
        pot = numbers_called[0:len(numbers_called)-1-idx]
        for board in BOARDS:
            if not has_bingo(board, pot):
                print("index", idx)
                print("numbers called", numbers_called)
                print("pot", pot)
                print("board", board)
                n = set(pot)
                b = set(board)
                print(b-n)
                print(sum(b-n)-numbers_called[len(pot)])
                print(numbers_called[len(pot)])
                return (sum(b-n)-numbers_called[len(pot)]) * numbers_called[len(pot)]
            
print(solve1())
print(solve2())