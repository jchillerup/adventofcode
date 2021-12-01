import tqdm
turns = list(map(int, open('input-little.txt').read().split(",")))

def find_last_occurence(list, needle):
    for j in range(len(list)-2, -1, -1):
        if list[j] == needle:
            return j
    return None


def run_game(turns):
    for i in range(len(turns), 2020):
        lo = find_last_occurence(turns, turns[i-1])
        if lo is None:
            turns.append(0)
        else:
            last_seen_turn = i-(lo+1)
            turns.append(last_seen_turn)

    return turns[-1]

assert(run_game([0,3,6]) == 436)
assert(run_game([1,3,2]) == 1)
assert(run_game([2,1,3]) == 10)
assert(run_game([1,2,3]) == 27)
assert(run_game([2,3,1]) == 78)
assert(run_game([3,2,1]) == 438)
assert(run_game([3,1,2]) == 1836)

print(run_game([7,12,1,0,16,2]))