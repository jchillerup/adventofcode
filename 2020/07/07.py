rules = [x[0:-1] for x in open('input.txt', 'r').read().replace("bags", "bag").strip().split("\n")]

rules_dict = dict()

for rule in rules:
    container, joined_contents = rule.split(" contain ")
    contents = joined_contents.split(", ")

    container_dict = dict()
    for content in contents:
        numeral, description = content.split(" ")[0], " ".join(content.split(" ")[1:])

        if content == "no other bag":
            container_dict = dict()
            break
        else:
            container_dict[description] = int(numeral)
    
    rules_dict[container] = container_dict


def lookup1(wanted_color):
    ret = list()
    for color in rules_dict:
        if rules_dict[color].get(wanted_color) is not None:
            ret.append(color)
            ret.extend(lookup1(color))
    
    return ret

def lookup2(wanted_color):
    adder = 1
    for needed_color in rules_dict[wanted_color]:
        multiplier = rules_dict[wanted_color][needed_color]
        adder += multiplier * lookup2(needed_color)

    return adder

result1 = len(set(lookup1("shiny gold bag")))
print(result1)

result = lookup2("shiny gold bag")-1
print(result)