import re
passports = open('input.txt','r').read().strip().replace("\n\n", "ØØØ").replace("\n", " ").split("ØØØ")

def validate(passport):
    fields = passport.split(" ")
    keys = set([x.split(":")[0] for x in fields])

    if "byr" in keys and "iyr" in keys and "eyr" in keys and "hgt" in keys and "hcl" in keys and "ecl" in keys and "pid" in keys:
        return True

    return False

def validate2(passport):
    fields = passport.split(" ")
    values = dict()             
    for field in fields:
        x = field.split(":")
        values[x[0]] = x[1]
    
    # Birth year
    if len(values["byr"]) != 4:
        return False
    if int(values["byr"]) < 1920:
        return False
    if int(values["byr"]) > 2002:
        return False

    # Issue year
    if len(values["iyr"]) != 4:
        return False
    if int(values["iyr"]) < 2010:
        return False
    if int(values["iyr"]) > 2020:
        return False

    # Expiration year
    if len(values["eyr"]) != 4:
        return False
    if int(values["eyr"]) < 2020:
        return False
    if int(values["eyr"]) > 2030:
        return False

    # Height
    if not(values["hgt"][-2:] == "cm" or values["hgt"][-2:] == "in"):
        return False

    height = int(values["hgt"][0:-2])
    if values["hgt"][-2:] == "cm":
        if height < 150:
            return False
        if height > 193:
            return False
    else:
        if height < 59:
            return False
        if height > 76:
            return False

    # Hair color
    hair_pattern = re.compile("#[0-9a-f]{6}")
    if hair_pattern.match(values["hcl"]) is None:
        return False

    # Eye color
    allowed_ecl = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth",])
    if values["ecl"] not in allowed_ecl:
        return False

    # Passport number
    pid_pattern = re.compile("^[0-9]{9}$")
    if pid_pattern.match(values["pid"]) is None:
        return False

    return True

good = 0
good2 = 0
for passport in passports:
    if validate(passport):
        good += 1

        if validate2(passport):
            good2 += 1

print(good)
print(good2)