import time
import re
p = re.compile("([a-z]{3}) ([-+])([0-9]+)")

raw_instructions = open('input.txt', 'r').read().strip().split("\n")
instructions = [p.match(ins).groups() for ins in raw_instructions]
visits = [0] * len(instructions)

ip = 0
acc = 0

while ip < len(instructions):
    ins, signum, abs_arg = instructions[ip]
    
    arg = int(abs_arg)
    if signum == '-':
        arg *= -1

    visits[ip] += 1

    # Star 1
    if visits[ip] == 2:
        print(acc)
        break;
    
    if ins == "acc":
        acc += arg
        ip += 1
    elif ins == "jmp":
        ip += arg
    elif ins == "nop":
        ip += 1
    else:
        raise NotImplementedError("Unsupported instruction %s" % ins)

def floyd(history):
    tortoise = 1
    hare = 2

    if len(history) <= 6: return False
    try:
        while history[tortoise] != history[hare]:
            tortoise += 1
            hare += 2

        mu = 0
        tortoise = 0
        while history[tortoise] != history[hare]:
            tortoise += 1
            hare += 1
            mu += 1
        
        lam = 1
        hare = tortoise+1
        while history[tortoise] != history[hare]:
            hare += 1
            lam += 1

        return lam, mu

    except IndexError:
        return False

# Star 2
def run_program(instructions):
    ip = 0
    acc = 0

    visits = [0] * len(instructions)
    history = list()

    while ip < len(instructions):
        ins, signum, abs_arg = instructions[ip]
        
        arg = int(abs_arg)
        if signum == '-':
            arg *= -1

        history.append(ip)
        visits[ip] += 1
        # print("%03d | %s %2d | %8d %8d" % (ip, ins, arg, acc, visits[ip]))
        
        if floyd(history) != False:
            return False

        if ins == "acc":
            acc += arg
            ip += 1
        elif ins == "jmp":
            ip += arg
        elif ins == "nop":
            ip += 1
        else:
            raise NotImplementedError("Unsupported instruction %s" % ins)
    
    return acc

for idx, ins in enumerate(instructions):
    new_instructions = instructions.copy()
    if ins[0] == "jmp":
        new_instructions[idx] = ("nop", ins[1], ins[2])
    elif ins[0] == "nop":
        new_instructions[idx] = ("jmp", ins[1], ins[2])
    else:
        continue

    result = run_program(new_instructions)
    if result != False:
        print("yay changing instruction %d to yield result %d " % (idx, result))
        exit()
    else:
        pass
        #print(idx)