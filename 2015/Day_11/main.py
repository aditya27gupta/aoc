import re


def check_password_validity(password: str) -> bool:
    if any([True if char in password else False for char in ["i", "o", "l"]]):
        return False

    matches = re.findall(r"([a-z])\1", password)
    if len(matches) < 2:
        return False

    for idx in range(len(password) - 2):
        if (ord(password[idx]) == ord(password[idx + 1]) - 1) and (
            ord(password[idx]) == ord(password[idx + 2]) - 2
        ):
            return True

    return False


def next_password(current_password: str) -> str:
    idx = len(current_password) - 1
    current_password = list(current_password)
    while True:
        if ord(current_password[idx]) == 122:
            current_password[idx] = "a"
            idx = idx - 1
        else:
            current_password[idx] = chr(ord(current_password[idx]) + 1)
            break

    return "".join(current_password)


def main() -> None:
    current_password = "vzbxxyzz"

    while True:
        new_password = next_password(current_password)
        result = check_password_validity(new_password)
        if result:
            break
        current_password = new_password

    print(new_password)


if __name__ == "__main__":
    main()
