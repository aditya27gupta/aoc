def find_for_one(l: int, w: int, h: int) -> int:
    area = 2*l*w + 2*w*h + 2*h*l
    extra = l*w*h/max(l, w, h)
    return area + extra


def find_ribbon_length(l: int, w: int, h: int) -> int:
    ribbon = l*w*h
    wrapper = 2 * (l+w+h - max(l, w, h))
    return ribbon + wrapper


def main() -> None:
    with open('input.txt') as file:
        contents = file.read()

    total_wrap: int = 0
    total_ribbon: int = 0
    for line in contents.split():
        l, w, h = map(int, line.split('x'))
        result = find_for_one(l, w, h)
        total_wrap += result
        result = find_ribbon_length(l, w, h)
        total_ribbon += result

    print(total_wrap)
    print(total_ribbon)


if __name__ == "__main__":
    main()
