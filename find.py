def find_path(map, start, end):  # возврат пути
    fill_path(map, start, end, 0)
    return backward(map, end, start)  # end - точка, в которую мы придем


def backward(map, start, end):  # ищем обратный путь
    x1, y1 = end  # куда мы идем
    x2, y2 = start
    row = len(map)
    col = len(map[0])

    path = []  # координаты обратного пути в виде кортеджей [y][x]

    while True:
        path.append((y2, x2))
        if x1 == x2 and y1 == y2:
            break
        list_range = []
        if x2 - 1 >= 0 and type(map[y2][x2 - 1]) == int:
            list_range.append((map[y2][x2 - 1], (y2, x2 - 1)))
        if x2 + 1 < col and type(map[y2][x2 + 1]) == int:
            list_range.append((map[y2][x2 + 1], (y2, x2 + 1)))
        if y2 - 1 >= 0 and type(map[y2 - 1][x2]) == int:
            list_range.append((map[y2 - 1][x2], (y2 - 1, x2)))
        if y2 + 1 < row and type(map[y2 + 1][x2]) == int:
            list_range.append((map[y2 + 1][x2], (y2 + 1, x2)))

        list_range = sorted(list_range, key=lambda item: item[0])

        y2, x2 = list_range[0][1]  # презаписываем значения самой дешовой соседней клетки

    path.reverse()  # разворачивает список
    return path


def fill_path(map, start, end, cost):  # заполняем поля препядствиями
    x1, y1 = start
    x2, y2 = end
    if start == end:
        if map[y1][x1] == "e" or map[y1][x1] > cost:
            map[y1][x1] = cost
        return

    row = len(map)
    col = len(map[0])

    if x1 < 0 or y1 < 0 or x1 >= col or y1 >= row:
        return
    if map[y1][x1] == "b":
        return

    if map[y1][x1] != "e" and cost >= map[y1][x1]:
        return

    if map[y1][x1] == "e" or map[y1][x1] > cost:
        map[y1][x1] = cost

    fill_path(map, (x1 + 1, y1), end, cost + 1)
    fill_path(map, (x1 - 1, y1), end, cost + 1)
    fill_path(map, (x1, y1 + 1), end, cost + 1)
    fill_path(map, (x1, y1 - 1), end, cost + 1)


if __name__ == "__main__":
    map = [["e"] * 10 for i in range(10)]
    map[0][1] = "b"
    map[2][0] = "b"

    start = (0, 0)
    end = (5, 5)
    print(*map, sep="\n")
    path = find_path(map, start, end)
    print()

    print(*map, sep="\n")
    print()
    print(path, sep="\n")


