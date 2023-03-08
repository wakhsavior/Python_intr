input = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":" S005 "},{"V":" S009 "},{"VIII":" S007 "}]

for dict in input:
    print(list(dict.values())[0].strip())

print(set([list(dict.values())[0].strip() for dict in input]))