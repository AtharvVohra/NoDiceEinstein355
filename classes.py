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

MOVE = {
    "U": "up",
    "D": "down",
    "L": "left",
    "R": "right",
    "X": "diagonal"
}

class Piece:
    def __init__(self, row, col, color, value):
        self.row = row # the piece's Y-coordinate on the board
        self.col = col # the piece's X-coordinate on the board
        self.color = color
        self.value = value

    def __str__(self):
        return COLOR[self.color] + VALUE[self.value]

class Board:
    def __init__(self, num_of_rows, num_of_cols):
        self.NUM_OF_ROWS = num_of_rows
        self.NUM_OF_COLS = num_of_cols
        self.board = []
        for _ in range(self.NUM_OF_ROWS):
            newRow = [None] * self.NUM_OF_COLS
            self.board.append(newRow)

    def print_board(self):
        print()
        for r in range(self.NUM_OF_ROWS):
            for c in range(self.NUM_OF_COLS):
                print(self.board[r][c], end = " ")
            print()
        print()

    def __str__(self):
        s = ""
        for r in range(self.NUM_OF_ROWS):
            for c in range(self.NUM_OF_COLS):
                if self.board[r][c]:
                    s = s + str(self.board[r][c]) + ' '
                else:
                    s = s + "." + '  '
            s = s + '\n'
        return s

    def addPiece(self, piece):
        self.board[piece.row][piece.col] = piece

    def movePiece(self, piece, row, col):
        oldRow = piece.row
        oldCol = piece.col
        self.board[row][col] = self.board[piece.row][piece.col]
        self.board[oldRow][oldCol] = None
        piece.row = row
        piece.col = col

    def removePiece(self, piece):
        self.board[piece.row][piece.col] = None
        del piece

    def get_piece(self, row, col):
        return self.board[row][col]

    def getRedPieces(self):
        numberofpieces = 0
        for r in range(self.NUM_OF_ROWS):
            for c in range(self.NUM_OF_COLS):
                if self.board[r][c]:
                    if self.board[r][c].color == "red":
                        numberofpieces += 1
        return numberofpieces

    def getBluePieces(self):
        numberofpieces = 0
        for r in range(self.NUM_OF_ROWS):
            for c in range(self.NUM_OF_COLS):
                if self.board[r][c]:
                    if self.board[r][c].color == "blue":
                        numberofpieces += 1
        return numberofpieces
    
    def getColorFromCoords(self, row, col):
        if row>=self.NUM_OF_ROWS or row<0 or col>=self.NUM_OF_COLS or col<0:
            return None # (checking boundaries!)
        if self.board[row][col] != None:
            return self.board[row][col].color
        return None
