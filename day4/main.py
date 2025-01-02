def generate_puzzle(input: str):
    return [[l for l in line] for line in input.split('\n')]

def part_one(puzzle: list[list[str]]):
    directions = [
        (0, 1), # East
        (0, -1), # West
        (1, 0), # South
        (-1, 0), # North
        (1, 1), # South East
        (-1, 1), # North East
        (1, -1), # South West
        (-1, -1) # North West
    ]
    count = 0

    for line_index, line in enumerate(puzzle):
        for letter_index, letter in enumerate(line):
            if letter != 'X':
                continue

            for direction in directions:
                start = [line_index, letter_index]
                word = puzzle[start[0]][start[1]] # Parses X

                for _ in range(3):
                    start[0] += direction[0]
                    start[1] += direction[1]

                    # Attempts to parse 'MAS'
                    # It would be better to check for each letter of the expected word, for performance
                    # But I really don't care about that right now
                    if 0 <= start[0] < len(puzzle) and 0 <= start[1] < len(puzzle[start[0]]):
                        word += puzzle[start[0]][start[1]]
                    else:
                        break

                if word == 'XMAS':
                    count += 1

    return count

with open('input.txt', 'r') as file:
    input = file.read().strip()

    puzzle = generate_puzzle(input)

    print(part_one(puzzle))