import re

fieldrule = re.compile("([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)")

def value_satisfies_at_least_one_rule(fields, value):
    for field in fields:
        if value >= field[1] and value <= field[2] or value >= field[3] and value <= field[4]:
            return True

    return False

def parse(filename):
    raw_fieldrules, raw_myticket, raw_nearbytickets = open(filename, 'r').read().strip().split("\n\n")

    fields = list()
    for field in raw_fieldrules.split("\n"):
        g = fieldrule.match(field).groups()
        g = (g[0], int(g[1]), int(g[2]), int(g[3]), int(g[4]))
        fields.append(g)
        # name, range1_lb, range1_ub, range2_lb, range2_up 


    not_valid_value_sum = 0
    for line in raw_nearbytickets.split("\n"):
        if line == "nearby tickets:": continue
        print(line)
        values = map(int, line.split(","))

        ticket_valid = True
        for value in values:
            if not value_satisfies_at_least_one_rule(fields, value):
                not_valid_value_sum += value
                ticket_valid = False
    
        print(ticket_valid)

    print(not_valid_value_sum)

    return 0,0,0


if __name__=='__main__':
    fields, myticket, nearby = parse('input.txt')

