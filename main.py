from connect4_ui import Connect4UI
from connect4_game import Connect4Game

import random


game = Connect4Game()


def choose_computer_move():
    """
    Choose which column the computer should play.

    STARTING VERSION:
    Choose randomly from the available columns.

    STUDENT TASK:
    Improve this strategy.
    """

    valid_columns = game.get_valid_columns()

    return random.choice(valid_columns)


def player_move(column):

    # Only allow the human to move on Player 1's turn
    if game.current_player != 1:
        return

    if not game.is_valid_move(column):
        ui.set_status("That column is full.")
        return

    game.drop_piece(column)
    ui.update_board(game.board)

    # Later:
    # robot_drop_piece(column)

    if game.check_winner():
        ui.set_status("You win!")
        return

    if game.is_full():
        ui.set_status("Draw!")
        return

    game.next_player()

    computer_move()


def computer_move():

    column = choose_computer_move()

    game.drop_piece(column)
    ui.update_board(game.board)

    print("Computer chose column:", column + 1)

    # Later:
    # robot_drop_piece(column)

    if game.check_winner():
        ui.set_status("Computer wins!")
        return

    if game.is_full():
        ui.set_status("Draw!")
        return

    game.next_player()

    ui.set_status("Your turn")


ui = Connect4UI(
    on_column=player_move
)

ui.update_board(game.board)
ui.set_status("Your turn")

ui.run()