from collections import defaultdict
in_fishes = [int(x) for x in open('input.txt', 'r').read().strip().split(",")]

fishes = defaultdict(int)
for fish in in_fishes:
    fishes[fish] += 1

def step_fishes(fishes):
    new_fishes = defaultdict(int)

    new_fishes[0] = fishes[1]
    new_fishes[1] = fishes[2]
    new_fishes[2] = fishes[3]
    new_fishes[3] = fishes[4]
    new_fishes[4] = fishes[5]
    new_fishes[5] = fishes[6]
    new_fishes[6] = fishes[7] + fishes[0]
    new_fishes[7] = fishes[8]
    new_fishes[8] = fishes[0]

    return new_fishes
    
def fish_sum(fishes):
    return sum([fishes[x] for x in fishes])

for i in range(256):
    fishes = step_fishes(fishes)

print(fish_sum(fishes))