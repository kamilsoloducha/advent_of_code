import util


def task1(lines):
    line_with_no_galaxy = []
    columns_with_no_galaxy = []
    galaxies = []

    table = util.to_2_dim_array(lines)

    for y in range(len(table)):
        has_galaxy = False
        for x in range(len(table[y])):
            if table[y][x] == '#':
                has_galaxy = True
                galaxies.append(util.Point(x, y))

        if not has_galaxy:
            line_with_no_galaxy.append(y)

    for x in range(len(table[0])-1):
        has_galaxy = False
        for y in range(len(table)):
            char = table[y][x]
            if char == '#':
                has_galaxy = True
                break

        if not has_galaxy:
            columns_with_no_galaxy.append(x)

    print(galaxies)

    for galaxy in galaxies:
        move_galaxy(galaxy, line_with_no_galaxy, columns_with_no_galaxy)

    print(galaxies)

    distance_sum = 0

    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            distance_sum += abs(galaxies[i].x - galaxies[j].x)
            distance_sum += abs(galaxies[i].y - galaxies[j].y)

    print(distance_sum)

    return


def move_galaxy(point: util.Point, rows, columns):

    delta_x = len([y for y in columns if y < point.x]) * (1000000 - 1)
    delta_y = len([y for y in rows if y < point.y]) * (1000000 - 1)

    point.x += (delta_x)
    point.y += (delta_y)
