
fishes = [int(x) for x in open('input.txt', 'r').read().strip().split(",")]

def fish_tick(fish, fishes):
    new_state = fish - 1
    if new_state == -1:
        fishes.append(9)
        return 6

    return new_state

print(fishes)

for i in range(256):
    fishes = [fish_tick(fish, fishes) for fish in fishes]

print(len(fishes))
