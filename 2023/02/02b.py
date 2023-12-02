gamestrings = open('input.txt').read().split("\n")

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def parse(gs):
    game_id, drawingsetstrings = gs.split(": ")

    game_id = int(game_id.replace("Game ", ""))
    
    maxes = dict()
    for dset in drawingsetstrings.split("; "):
        drawings = dset.split(", ")

        for drawing in drawings:
            quantity, identifier = drawing.split(" ")
            quantity = int(quantity)

            if maxes.get(identifier) is None:
                maxes[identifier] = quantity
            else:
                if maxes[identifier] < quantity:
                    maxes[identifier] = quantity

    product = 1
    for v in maxes.values():
        product *= v
    return product, game_id
    # print(game_id)
sum = 0
for gs in gamestrings:
    prod, id = parse(gs)

    sum += prod

print(sum)