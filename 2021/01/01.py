numbers = [int(x) for x in open('input').read().strip().split("\n")]

incr = 0

for i in range(len(numbers)):
    if i == 0: continue

    if numbers[i] > numbers[i-1]:
        incr += 1

print(incr)