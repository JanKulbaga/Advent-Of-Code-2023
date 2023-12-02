def read_file(file_path: str) -> list[str]:
    with open(file_path) as file:
        return [line[:-1] for line in file.readlines()]


def main(input_file: str) -> None:
    lines = read_file(input_file)
    total = 0
    for line in lines:
        left = right = -1
        for index, char in enumerate(line):
            if char.isdigit():
                if left == -1:
                    left = char
                right = char
            else:
                for val, num in enumerate(
                    [
                        "one",
                        "two",
                        "three",
                        "four",
                        "five",
                        "six",
                        "seven",
                        "eight",
                        "nine",
                    ],
                    start=1,
                ):
                    if line[index:].startswith(num):
                        if left == -1:
                            left = val
                        right = val
        num = int(f"{left}{right}")
        total += num
    print(f"Sum is {total}")


if __name__ == "__main__":
    main("../input.txt")

# The answer is 55701
