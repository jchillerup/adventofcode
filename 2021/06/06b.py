from collections import defaultdict
in_fishes = [int(x) for x in open('input.txt', 'r').read().strip().split(",")]

fishes = defaultdict(int)
for fish in in_fishes:
    fishes[fish] += 1

def step_fishes(fishes):
    new_fishes = defaultdict(int)

    for i in range(9):
        new_fishes[i] = fishes[(i+1) % 9]
    
    new_fishes[6] += fishes[0]
    
    return new_fishes
    
def fish_sum(fishes):
    return sum([fishes[x] for x in fishes])

for i in range(256):
    fishes = step_fishes(fishes)

print(fish_sum(fishes))