"""
Board representation of No Dice Einstein. 
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
        self.string = COLOR[self.color] + VALUE[self.value]


class Board:
    def __init__(self):
        self.board = []
        for _ in range(5):
            newRow = [None] * 5
            self.board.append(newRow)

    def print_board(self):
        for r in range(5):
            for c in range(5):
                print(self.board[r][c])
            print('/n')

    def __str__(self):
        s = ""
        for r in range(5):
            for c in range(5):
                if self.board[r][c]:
                    s = s + self.board[r][c].string + ' '
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
