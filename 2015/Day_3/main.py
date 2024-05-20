def find_unique_homes(contents: str) -> int:
    mapping = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
    curr_loc = (0, 0)
    uniques = set()
    for direction in contents:
        if direction not in mapping:
            continue
        uniques.add(curr_loc)
        curr_loc = (curr_loc[0] + mapping[direction][0],
                    curr_loc[1] + mapping[direction][1])

    return len(uniques)


def find_unique_homes_with_robo(contents: str) -> int:
    mapping = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
    santa_loc, robo_loc = (0, 0), (0, 0)
    santa_curr_loc = set()
    robo_curr_loc = set()

    for idx, content in enumerate(contents):
        if content not in mapping:
            continue

        if idx % 2 == 0:
            santa_loc = (santa_loc[0] + mapping[content][0],
                         santa_loc[1] + mapping[content][1])
        else:
            robo_loc = (robo_loc[0] + mapping[content][0],
                        robo_loc[1] + mapping[content][1])

        santa_curr_loc.add(santa_loc)
        robo_curr_loc.add(robo_loc)

    total_loc = santa_curr_loc.union(robo_curr_loc)
    return len(total_loc)


def main():
    with open('input.txt', mode='r') as file:
        contents = file.read()

    result = find_unique_homes(contents)
    print(result)

    result = find_unique_homes_with_robo(contents)
    print(result)


if __name__ == "__main__":
    main()
