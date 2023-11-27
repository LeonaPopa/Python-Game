from tkinter import *
import ctypes


class Console:
    def __init__(self, service, dimension, validator):
        self.service = service
        self.dimension = dimension
        self.validator = validator
        self.button = [[0] * dimension for i in range(dimension + 1)]
        self.gui = Tk()

    def read_command(self):
        command_row = input("Row (letter from A to " + chr(ord("A") + self.dimension - 2) + ")>>>")
        command_row = command_row.upper()
        command_row = command_row.strip()
        command_column = input("Column (number between(1-%d))>>>" % (self.dimension - 1))
        command_column = int(command_column)
        self.validator.command_input_validator(command_row, command_column, self.dimension)
        if self.service.valid(int(ord(command_row) - ord("A") + 1), command_column):
            return int(ord(command_row) - ord("A") + 1), command_column
        else:
            print("The command is not right")
            return 0, 0

    def press(self, i, j):
        if i == 0 or j == 0 or i >= self.dimension or j >= self.dimension or self.service.game_complete():
            return
        if self.service.valid(i, j) is False:
            ctypes.windll.user32.MessageBoxW(0, "Used", "Try again", 0)
            return
        self.service.add_value_to_grid(i, j, "x")
        self.button[i][j].config(text='X')
        self.service.make_gray_part(i, j)
        self.service.display_game(True, self.button)

        if self.service.game_complete():
            ctypes.windll.user32.MessageBoxW(0, "YOU WON!!!!!!", "BRAVO", 0)
            self.gui.quit()
        else:
            self.service.computer_response(True, self.button)
            self.service.display_game(True, self.button)
            if self.service.game_complete():
                ctypes.windll.user32.MessageBoxW(0, "YOU LOST!!!", "SORRY", 0)
                self.gui.quit()

    def display_gui_game(self):
        self.gui.configure(background="white")
        self.gui.geometry("400x400")
        self.button[0][0] = Button(self.gui, text='', fg='black', bg='white', height=1, width=2)
        self.button[0][0].grid(row=0, column=0)
        for j in range(1, self.dimension):
            self.button[0][j] = Button(self.gui, text=str(j), fg='black', bg='white', height=1, width=2)
            self.button[0][j].grid(row=0, column=j)
        for i in range(1, self.dimension):
            self.button[i][0] = Button(self.gui, text=chr(ord('A') + i - 1), fg='black', bg='white', height=1, width=2)
            self.button[i][0].grid(row=i, column=0)
        for i in range(1, self.dimension):
            for j in range(1, self.dimension):
                self.button[i][j] = Button(self.gui, text='', fg='black', bg='white', command=lambda x=i, y=j: self.press(x, y), height=1, width=2)
                self.button[i][j].grid(row=i, column=j)

    def run_console(self, with_gui):
        if with_gui is False:
            self.service.display_game(False, self.button)
            while True:
                try:
                    command_row, command_column = self.read_command()
                except ValueError:
                    print("wrong value")
                    continue
                if command_column == 0 and command_row == 0:
                    continue
                self.service.add_value_to_grid(command_row, command_column, "x")
                self.service.make_gray_part(command_row, command_column)
                if self.service.game_complete():
                    print("YOU WON!!!")
                    break
                self.service.computer_response(False, self.button)
                self.service.display_game(False, self.button)
                if self.service.game_complete():
                    print("YOU LOST!!!")
                    break
        else:
            self.display_gui_game()
            self.gui.mainloop()
