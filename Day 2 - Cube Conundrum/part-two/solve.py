def read_file(file_path: str) -> list[str]:
    with open(file_path) as file:
        return [line[:-1] for line in file.readlines()]


class Game:
    def __init__(self) -> None:
        self.blue = 0
        self.red = 0
        self.green = 0


def main(input_file: str) -> None:
    lines = read_file(input_file)
    values = []
    for line in lines:
        sub_games = line.split(":")[1].strip(" ").split("; ")
        game = Game()
        for sub_game in sub_games:
            sub_game = sub_game.strip().split(", ")
            for num_color in sub_game:
                num, color = num_color.split(" ")
                if color == "blue":
                    game.blue = max(game.blue, int(num))
                if color == "red":
                    game.red = max(game.red, int(num))
                if color == "green":
                    game.green = max(game.green, int(num))
        values.append(game.blue * game.red * game.green)

    print(f"Sum is {sum(values)}")


if __name__ == "__main__":
    main("../input.txt")

# The answer is 83105
