class Connect4Game:

    ROWS = 6
    COLUMNS = 7

    def __init__(self):
        self.reset()


    def reset(self):
        self.board = [
            [0 for column in range(self.COLUMNS)]
            for row in range(self.ROWS)
        ]

        self.current_player = 1


    def is_valid_move(self, column):
        return (
            0 <= column < self.COLUMNS
            and self.board[0][column] == 0
        )


    def get_valid_columns(self):
        return [
            column
            for column in range(self.COLUMNS)
            if self.is_valid_move(column)
        ]


    def drop_piece(self, column):
        """
        Drop the current player's piece into a column.

        Returns the row where the piece landed.
        Returns None if the move is invalid.
        """

        if not self.is_valid_move(column):
            return None

        for row in range(self.ROWS - 1, -1, -1):

            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                return row


    def check_winner(self, player=None):
        """
        Check whether a player has four connected pieces.
        """

        if player is None:
            player = self.current_player

        # Horizontal
        for row in range(self.ROWS):
            for column in range(self.COLUMNS - 3):

                if all(
                    self.board[row][column + i] == player
                    for i in range(4)
                ):
                    return True

        # Vertical
        for row in range(self.ROWS - 3):
            for column in range(self.COLUMNS):

                if all(
                    self.board[row + i][column] == player
                    for i in range(4)
                ):
                    return True

        # Diagonal down-right
        for row in range(self.ROWS - 3):
            for column in range(self.COLUMNS - 3):

                if all(
                    self.board[row + i][column + i] == player
                    for i in range(4)
                ):
                    return True

        # Diagonal up-right
        for row in range(3, self.ROWS):
            for column in range(self.COLUMNS - 3):

                if all(
                    self.board[row - i][column + i] == player
                    for i in range(4)
                ):
                    return True

        return False


    def is_full(self):
        return len(self.get_valid_columns()) == 0


    def next_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1