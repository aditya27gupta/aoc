import hashlib


def create_and_compare_hex(secret_key: str, num_of_zeros: int = 5) -> int:
    num = 1
    zeros_to_check = '0' * num_of_zeros
    while True:
        unique_str = f'{secret_key}{num}'
        result = hashlib.md5(unique_str.encode())
        hex_result = result.hexdigest()
        if hex_result[:num_of_zeros] == zeros_to_check:
            break
        num += 1

    return num


def main() -> None:
    with open('input.txt', mode='r') as file:
        secret_key = file.read().strip()

    result = create_and_compare_hex(secret_key)
    print(result)

    result = create_and_compare_hex(secret_key, num_of_zeros=6)
    print(result)


if __name__ == '__main__':
    main()
