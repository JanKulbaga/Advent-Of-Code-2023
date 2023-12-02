def read_file(file_path: str) -> list[str]:
    with open(file_path) as file:
        return [line[:-1] for line in file.readlines()]


class Game:
    def __init__(self, id: int) -> None:
        self.id = id
        self.blue = 0
        self.red = 0
        self.green = 0


def main(input_file: str) -> None:
    lines = read_file(input_file)
    ids = []
    for id, line in enumerate(lines, start=1):
        sub_games = line.split(":")[1].strip(" ").split("; ")
        game = Game(id)
        correct = True
        for sub_game in sub_games:
            sub_game = sub_game.strip().split(", ")
            for num_color in sub_game:
                num, color = num_color.split(" ")
                if color == "blue":
                    game.blue = int(num)
                if color == "red":
                    game.red = int(num)
                if color == "green":
                    game.green = int(num)
            if game.red > 12 or game.green > 13 or game.blue > 14:
                correct = False
                break
        if correct:
            ids.append(game.id)

    print(f"Sum is {sum(ids)}")


if __name__ == "__main__":
    main("../input.txt")

# The answer is 1931
