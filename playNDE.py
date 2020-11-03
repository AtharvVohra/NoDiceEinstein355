import setup
import sys


def play():
    board = setup.init()
    # print(board)
    blueToPlay = True

    while True:
        """
        Check if game is over
        """
        redCorner = board.board[0][0]
        blueCorner = board.board[4][4]
        if redCorner and blueCorner:
            if redCorner.color == "blue" and blueCorner.color == "red":
                break

    if blueToPlay:
        pass
    elif not blueToPlay:
        pass

    board.print_board()


if __name__ == "__main__":
    play()
