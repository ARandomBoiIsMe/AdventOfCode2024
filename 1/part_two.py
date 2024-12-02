similarity_score = 0

with open('input.txt', 'r') as file:
    first, second = [], []

    for line in file.readlines():
        numbers = line.split()

        first.append(int(numbers[0].strip()))
        second.append(int(numbers[1].strip()))

    for number in first:
        appearances = second.count(number)

        similarity_score += number * appearances

    print(similarity_score)