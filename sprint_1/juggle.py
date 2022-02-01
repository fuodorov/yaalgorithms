def max_points(*, keys):
    points = 0
    counter = [0] * 10
    for row in range(4):
        for value in input():
            if value != '.':
                counter[int(value)] += 1
    for value in counter:
        points += 1 if 0 < value <= 2 * keys else 0
    return points


keys = int(input())

print(max_points(keys=keys))
