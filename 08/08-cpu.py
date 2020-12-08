from cpu import CPU
from utils import floyd, load_program_from_file
import time

program = load_program_from_file("input-little.txt")
cpu = CPU(program)


tic = time.monotonic()
# Star 1
visited = list()
while True:
    cpu.step()
    if cpu.ip not in visited:
        visited.append(cpu.ip)
    else:
        print(cpu.acc)
        break
toc = time.monotonic()

print(toc-tic)


# Star 2
tic = time.monotonic()
for idx, ins in enumerate(program):
    new_program = program.copy()
    if ins[0] == "jmp":
        new_program[idx] = ("nop", ins[1])
    elif ins[0] == "nop":
        new_program[idx] = ("jmp", ins[1])
    else:
        continue

    cpu = CPU(new_program)
    visited = list()
    while cpu.ip < len(new_program):
        # print(cpu.ip, visited)

        cpu.step()
        visited.append(cpu.ip)
        # not the right one if we find a cycle
        if floyd(visited) != False:
            break
    
    if cpu.ip == len(program):
        print(cpu.acc)
        break;
toc = time.monotonic()
print(toc-tic)