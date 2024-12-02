def part_one(lines: list[str]):
    safe_reports = 0

    for line in lines:
        nums = [int(num) for num in line.split()]

        sign = None
        safe = None
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            currSign = 'neg' if diff < 0 else 'pos'

            if sign is None:
                sign = currSign

            if currSign != sign or abs(diff) not in range(1, 4):
                safe = False
                break

            safe = True

        safe_reports += 1 if safe is True else 0

    print("Part One:", safe_reports)

with open('input.txt', 'r') as file:
    lines = file.readlines()

    part_one(lines)