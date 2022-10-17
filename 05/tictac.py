"""
hello pylint
"""


class TicTacGame:
    """
    hello pylint
    """

    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.winner = 0

    def show_board(self):
        """
        shows the board
        _ is empty cell
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    print(' _ ', end='')
                if self.board[i][j] == 1:
                    print(' X ', end='')
                if self.board[i][j] == 2:
                    print(' O ', end='')
            print()

    def validate_input(self, inp):
        """
        checking is input correct for board
        """
        if ' ' not in inp:
            return False
        if inp.count(' ') > 1:
            return False
        row_and_column = inp.split()

        if not row_and_column[0].isdecimal() or not row_and_column[1].isdecimal():
            return False

        row, column = map(int, row_and_column)

        if 1 <= row <= 3 and 1 <= column <= 3:
            if self.board[row - 1][column - 1] == 0:
                return True

        return False

    def start_game(self):
        """
        start the game with X go girst
        """
        player = 1
        turns_left = 9
        while self.winner == 0 and turns_left > 0:
            self.show_board()
            print(f"Ход игрока {player}")
            while True:
                inp = input("Введите номер строки и столбца через пробел: ")
                if self.validate_input(inp):
                    break
                print("Некорректный ввод. Вводите числа от 1 до 3")
            turns_left -= 1
            row, column = map(int, inp.split())
            self.board[row - 1][column - 1] = player
            self.check_winner()
            if player == 1:
                player = 2
            else:
                player = 1
        self.show_board()
        if self.winner == 0:
            print("НИЧЬЯ")
        else:
            print(f"ПОБЕДИЛ {self.winner}")

    def check_winner(self):
        """
        checks the winner by looking at
        rows, columns and diag.
        """
        for i in range(len(self.board)):
            result = []
            for j in range(len(self.board[i])):
                result.append(self.board[i][j])
            if result.count(1) == len(self.board[i]):
                self.winner = 1
            elif result.count(2) == len(self.board[i]):
                self.winner = 2

        for j in range(len(self.board[0])):
            result = []
            for i in range(len(self.board)):
                result.append(self.board[i][j])
            if result.count(1) == len(self.board):
                self.winner = 1
            elif result.count(2) == len(self.board):
                self.winner = 2

        result = []
        for i in range(len(self.board)):
            result.append(self.board[i][i])
        if result.count(1) == len(self.board[0]):
            self.winner = 1
        elif result.count(2) == len(self.board[0]):
            self.winner = 2

        result = []
        for i in range(len(self.board)):
            result.append(self.board[i][-(i + 1)])
        if result.count(1) == len(self.board[0]):
            self.winner = 1
        elif result.count(2) == len(self.board[0]):
            self.winner = 2


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
