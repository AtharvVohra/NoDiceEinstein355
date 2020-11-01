"""
Board representation of No Dice Einstein. 
"""

COLOR = {
    'red': 'R',
    'blue': 'B'
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

    def __str__(self):
        return COLOR[self.color] + VALUE[self.value]


class Board:
    def __init__(self):
        board = []
        pieces = []

    def __str__(self):
        pass

    def movePiece(self):
        pass

    def removePiece(self):
        pass

    def print_board(self):
        pass
