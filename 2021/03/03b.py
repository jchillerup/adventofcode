from collections import defaultdict
import pprint
import numpy as np

pp = pprint.PrettyPrinter()

fp = open('input', 'r').read().strip().split("\n")

in_numbers = list()

for reading in fp:
    in_numbers.append([x.replace('0', '-1') for x in list(reading)])

def most_ones(bit_position):
    return sum(numbers[:, bit_position]) > 0

def most_zeros(bit_position):
    return sum(numbers[:, bit_position]) < 0

def equal(bit_position):
    return sum(numbers[:, bit_position]) == 0

def constrain(bitvals):
    mask = None
    for idx, value in enumerate(bitvals):
        if mask is None:
            mask = numbers[:,idx]==value
        else:
            mask &= numbers[:,idx]==value

    return mask

def num2dec(num):
    binary = np.where(num == -1, 0, num)
    dec = 0
    for idx, val in enumerate(binary):
        dec += val << len(binary)-1-idx
    return dec

numbers = np.array(in_numbers).astype(int)
width = len(numbers[0])

constraint = list()
for i in range(width):
    if most_zeros(i):
        constraint.append(-1)
    elif most_ones(i):
        constraint.append(1)
    else:
        constraint.append(1)
    numbers = numbers[constrain(constraint)]
    if len(numbers) == 1:
        break

num1 = num2dec(numbers[0])


numbers = np.array(in_numbers).astype(int)
width = len(numbers[0])

constraint = list()
for i in range(width):
    if most_ones(i):
        constraint.append(-1)
    elif most_zeros(i):
        constraint.append(1)
    else:
        constraint.append(-1)

    numbers = numbers[constrain(constraint)]
    if len(numbers) == 1:
        break

num2 = num2dec(numbers[0])

print(num1*num2)
