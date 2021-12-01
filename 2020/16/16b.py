import re
import numpy as np

fieldrule = re.compile("([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)")

def value_satisfies_at_least_one_rule(fields, value):
    for field in fields:
        if value >= field[1] and value <= field[2] or value >= field[3] and value <= field[4]:
            return True

    return False

def find_probable_field(fields, column_vector):
    probable_fields = list()
    for field in fields:
        checks_out = True
        for value in column_vector:
            if not (value >= field[1] and value <= field[2] or value >= field[3] and value <= field[4]):
                checks_out = False
                break    
        if checks_out == True:
            probable_fields.append(field)

    return probable_fields


def parse(filename):
    raw_fieldrules, raw_myticket, raw_nearbytickets = open(filename, 'r').read().strip().split("\n\n")

    fields = list()
    for field in raw_fieldrules.split("\n"):
        g = fieldrule.match(field).groups()
        g = (g[0], int(g[1]), int(g[2]), int(g[3]), int(g[4]))
        fields.append(g)
        # name, range1_lb, range1_ub, range2_lb, range2_up 


    filtered_nearby = list()
    for line in raw_nearbytickets.split("\n"):
        if line == "nearby tickets:": continue
        # print(line)
        values = list(map(int, line.split(",")))

        ticket_valid = True
        for value in values:
            if not value_satisfies_at_least_one_rule(fields, value):
                ticket_valid = False
    
        if ticket_valid:
            filtered_nearby.append(values)

    filtered_nearby = np.array(filtered_nearby)
    probable_fields = list()
    for column in range(len(filtered_nearby[0])):
        f = [x[0] for x in find_probable_field(fields, filtered_nearby[:,column])]
        probable_fields.append( (len(f), column, set(f)) )
    
    probable_fields.sort(key=lambda x: x[0])

    last = set()
    my_ticket_vals = [int(x) for x in raw_myticket.split("\n")[1].split(",")]
    mult = 1
    for f in probable_fields:
        description = list(f[2] - last)[0]
        if "departure" == description.split(" ")[0]: 
            print(f[1], description, my_ticket_vals[f[1]])
            mult *= my_ticket_vals[f[1]]
        last = f[2]

    print(mult)

    return 0,0,0


if __name__=='__main__':
    fields, myticket, nearby = parse('input.txt')

