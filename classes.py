"""
<<<<<<< HEAD
Board representation of No Dice Einstein. 
=======
Board representation of No Dice Einstein.
>>>>>>> fad59d8da4a619a67ed398f90ce56c40c30edaae
"""

COLOR = {
    "red": 'R',
    "blue": 'B'
}

VALUE = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6'
}


class Piece:
    def __init__(self, row, col, color, value):
        self.row = row
        self.col = col
        self.color = color
        self.value = value
<<<<<<< HEAD
        self.string = COLOR[self.color] + VALUE[self.value]
=======

    def __str__(self):
        return COLOR[self.color] + VALUE[self.value]
>>>>>>> fad59d8da4a619a67ed398f90ce56c40c30edaae


class Board:
    def __init__(self):
        self.board = []
        for _ in range(5):
            newRow = [None] * 5
            self.board.append(newRow)

    def print_board(self):
<<<<<<< HEAD
        for r in range(5):
            for c in range(5):
                print(self.board[r][c])
            print('/n')
=======
        print()
        for r in range(5):
            for c in range(5):
                print(self.board[r][c], end = " ")
            print()
        print()
>>>>>>> fad59d8da4a619a67ed398f90ce56c40c30edaae

    def __str__(self):
        s = ""
        for r in range(5):
            for c in range(5):
                if self.board[r][c]:
<<<<<<< HEAD
                    s = s + self.board[r][c].string + ' '
=======
                    s = s + str(self.board[r][c]) + ' '
>>>>>>> fad59d8da4a619a67ed398f90ce56c40c30edaae
                else:
                    s = s + "." + '  '
            s = s + '\n'
        return s

    def addPiece(self, piece):
        self.board[piece.row][piece.col] = piece

    def movePiece(self, piece, row, col):
        self.board[piece.row][piece.col] = None
        piece.row = row
        piece.col = col

    def removePiece(self, piece):
        self.board[piece.row][piece.col] = None
        del piece
