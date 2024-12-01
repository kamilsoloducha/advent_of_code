def task1(content):
    points = [(0, 0)]
    dir = {
        "U" : (-1, 0),
        "D" : (1, 0),
        "R" : (0, 1),
        "L" : (0, -1)
    }
    boundry_points_count = 0

    for line in content:
        d, n, _ = line.split()
        dr, dc = dir[d]
        n = int(n)
        boundry_points_count += n
        r, c = points[-1]
        points.append((r + dr * n, c + dc * n))

    A = abs(sum(points[i][0] * (points[(i-1)][1] - points[(i+1) % len(points)][1]) for i in range(len(points)))) // 2

    i = A - boundry_points_count // 2 + 1

    print(i + boundry_points_count)


def task2(content):
    points = [(0, 0)]
    dir = {
        "U" : (-1, 0),
        "D" : (1, 0),
        "R" : (0, 1),
        "L" : (0, -1)
    }
    boundry_points_count = 0

    for line in content:
        _, _, hex = line.strip("\n").split()
        hex = hex[2:-1]
        dr, dc = dir["RDLU"[int(hex[-1])]]
        n = int(hex[:-1], 16)
        boundry_points_count += n
        r, c = points[-1]
        points.append((r + dr * n, c + dc * n))

    A = abs(sum(points[i][0] * (points[(i-1)][1] - points[(i+1) % len(points)][1]) for i in range(len(points)))) // 2

    i = A - boundry_points_count // 2 + 1

    print(i + boundry_points_count)