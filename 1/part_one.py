sum_of_distances = 0

with open('input.txt', 'r') as file:
    first, second = [], []

    for line in file.readlines():
        numbers = line.split()

        first.append(int(numbers[0].strip()))
        second.append(int(numbers[1].strip()))

    first.sort()
    second.sort()

    for i in range(len(first)):
        sum_of_distances += abs(first[i] - second[i])

    print(sum_of_distances)