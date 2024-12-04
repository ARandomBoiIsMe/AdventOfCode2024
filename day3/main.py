import re

def parse_instructions(corrupted_instructions: str) -> list:
    return re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", corrupted_instructions)

def execute_instructions(values):
    output = 0

    for val in values:
        output += int(val[0]) * int(val[1])

    return output

def part_one(corrupted_instructions: str):
    values = parse_instructions(corrupted_instructions)
    result = execute_instructions(values)

    print("Part One:", result)

with open('input.txt', 'r') as file:
    corrupted_instructions = file.read()

part_one(corrupted_instructions)