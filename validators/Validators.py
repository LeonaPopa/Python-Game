class Validators:
    def command_input_validator(self, command_row, command_column, dimension):
        if not ("A" <= command_row <= "J" and 1 <= command_column < dimension and len(command_row) == 1):
            raise ValueError("The command is not right")