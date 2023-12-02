def read_file(file_path: str) -> list[str]:
    with open(file_path) as file:
        return [line[:-1] for line in file.readlines()]


def main(input_file: str) -> None:
    lines = read_file(input_file)
    total = 0
    for line in lines:
        left = 0
        right = len(line) - 1
        while not line[left].isdigit() or not line[right].isdigit():
            if not line[left].isdigit():
                left += 1
            if not line[right].isdigit():
                right -= 1
        num = int(f"{line[left]}{line[right]}")
        total += num
    print(f"Sum is {total}")


if __name__ == "__main__":
    main("../input.txt")

# The answer is 56397
