import random


class Service:
    def __init__(self, repository, dimension):
        self.__repository = repository
        self.range = dimension

    def valid(self, i, j):
        if self.__repository.get_value(i, j) == 0:
            return True
        else:
            return False

    def game_complete(self):
        for i in range(1, self.range):
            for j in range(1, self.range):
                if self.__repository.get_value(i, j) == 0:
                    return False
        return True

    def display_game(self, with_button, button):
        if with_button is False:
            display_character_number = 65
            # First row
            print(f" ", end='')
            for j in range(1, self.range):
                print(f"|%s%d" % (' ' if j < 10 else '', j), end='')
            print("| ")
            print(((self.range - 1) * 3 + 4) * "-")

            # Other rows
            for i in range(1, self.range):
                print(f"{chr(display_character_number + i-1)}", end='')
                for j in range(1, self.range):
                    print(f"| {' ' if self.__repository.get_value(i, j) ==0 else self.__repository.get_value(i, j)}", end='')
                print("| ")
                print(((self.range - 1) * 3 + 4) * "-")
        else:
            for i in range(1, self.range):
                for j in range(1, self.range):
                    if self.__repository.get_value(i, j) == 1:
                        button[i][j].config(bg='gray')

    def add_value_to_grid(self, i, j, value):
        self.__repository.add_value_to_grid(i, j, value)

    def make_gray_part(self, i, j):
        self.__repository.make_gray_part(i, j)

    def computer_response(self, with_button,  button):
        while True:
            i = random.randint(1, self.range - 1)
            j = random.randint(1, self.range - 1)
            if self.__repository.get_value(i, j) == 0:
                self.add_value_to_grid(i, j, "o")
                self.make_gray_part(i, j)
                if with_button:
                    button[i][j].config(text='0')
                else:
                    print("Computer moved: (%s %d)" % (chr(ord('A')+i-1), j))
                return True
