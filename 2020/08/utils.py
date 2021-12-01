
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

def load_program_from_file(filename):
    import re
    p = re.compile("([a-z]{3}) ([-+])([0-9]+)")

    raw_instructions = open('input.txt', 'r').read().strip().split("\n")
    instructions = [(p.match(ins).groups()[0], int("%s%s" % (p.match(ins).groups()[1], p.match(ins).groups()[2]))) for ins in raw_instructions]
    
    return instructions
