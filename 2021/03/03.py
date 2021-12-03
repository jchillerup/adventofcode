from collections import defaultdict


fp = open('input', 'r').read().strip().split("\n")

accumulator = defaultdict(int)

for reading in fp:
    bits = list(reading)
    for idx, val in enumerate(bits):
        if val == "0":
            accumulator[idx] -= 1
            # accumulator.set(idx, accumulator.get(idx, 0) - 1)
        elif val == "1":
            accumulator[idx] += 1
            # accumulator.set(idx, accumulator.get(idx, 0) + 1)
        else:
            raise ValueError()

gamma_rate = 0
epsilon_rate = 0

for idx in accumulator:
    gamma_rate += int(accumulator[idx] > 0)  << (len(accumulator)-1-idx)
    epsilon_rate += int(accumulator[idx] < 0)  << (len(accumulator)-1-idx)

print(gamma_rate * epsilon_rate)