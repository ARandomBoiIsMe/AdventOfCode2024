def part_one(first: list, second: list):
    sum_of_distances = 0

    first.sort()
    second.sort()

    for i in range(len(first)):
        sum_of_distances += abs(first[i] - second[i])

    print("Part One:", sum_of_distances)

def part_two(first: list, second: list):
    similarity_score = 0

    for number in first:
        appearances = second.count(number)

        similarity_score += number * appearances

    print("Part Two:", similarity_score)

with open('input.txt', 'r') as file:
    first, second = [], []

    for line in file.readlines():
        numbers = line.split()

        first.append(int(numbers[0].strip()))
        second.append(int(numbers[1].strip()))

    part_one(first, second)
    part_two(first, second)