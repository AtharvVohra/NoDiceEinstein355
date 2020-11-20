import classes
import sys
import random
import playNDE

"""
AI move selector for NDE. Move evaluation by maximizing weights.
"""

def getMovablePieces(pieceList): # similar to choosePiece function in playNDE but finding moves starts evaluation
    piecesToPick = [] # a list of pieces to evaluate moves for
    if len(pieceList) > 1:
        diceRoll = random.randint(1, 6)
        print("Dice Roll:", diceRoll)
        if not any(piece for piece in pieceList if piece.value == diceRoll):
            # Piece is dead, finds next highest/lowest
            nextUp = diceRoll
            nextDown = diceRoll
            i = diceRoll
            while not any(piece for piece in pieceList if piece.value == i):
                i = (i + 1) % 7
                if i == 0:
                    i = 1
            nextUp = i
            i = diceRoll
            while not any(piece for piece in pieceList if piece.value == i):
                i = i - 1
                if i == 0:
                    i = 6
            nextDown = i
            for piece in pieceList:
                if piece.value == nextUp or piece.value == nextDown:
                    piecesToPick.append(piece)
            return piecesToPick
        else:
            print("pog")
            for piece in pieceList:
                if piece.value == diceRoll:
                    piecesToPick.append(piece)
            return piecesToPick
    else:
        piecesToPick.append(pieceList[0])
        return piecesToPick

def weighDistance(pieceToMove, move, board, currentWeight): # weighs minimized distance to goal for each move a piece can make
    return

def weighTake(pieceToMove, move, board, currentWeight): # assigns weights for taking an opponent's piece and taking your own pieces
    return

def weighDefense(pieceToMove, move, board, currentWeight): # weighs defensiveness of each move a piece can make
    return
    
def weighRisk(piece, move, board, currentWeight): # weighs risk of each move a piece can make
    updatedRow = piece.row
    updatedCol = piece.col
    if move == "D":
        updatedRow = piece.row + 1
    elif move == "R":
        updatedCol = piece.col + 1
    elif move == "X":
        updatedRow = piece.row + 1
        updatedCol = piece.col + 1
    # check if there's an opp piece to the right, to the bottom, and diagonal
    if updatedCol < 4:
        if board.board[updatedRow][updatedCol + 1] and board.board[updatedRow][updatedCol + 1].color == "blue": # to the right
            currentWeight -= 0.5
    if updatedRow < 4:
        if board.board[updatedRow + 1][updatedCol] and board.board[updatedRow + 1][updatedCol].color == "blue": # to the bottom
            currentWeight -= 0.5
    if updatedRow < 4 and updatedCol < 4:
        if board.board[updatedRow + 1][updatedCol + 1] and board.board[updatedRow + 1][updatedCol + 1].color == "blue": # to the diagonal rightbottom
            currentWeight  -= 0.5
    return currentWeight

def evaluateMoves(board, pieceList):
    piecesToPick = getMovablePieces(pieceList)
    bestPiece = piecesToPick[0] # update bestX vars simultaneously in eval switches
    bestWeight = -100
    bestMove = None
    for piece in piecesToPick:
        currentWeight = 0
        # go through all the pieces and evaluate all the moves they can make, updating bestMove and bestPiece in the process
        # possible moves for red, run weight checks and record new weight
        if playNDE.isMoveValid(piece, "D"):
            # evaluate move and return weight
            currentWeight = weighRisk(piece, "D", board, currentWeight)
            # compare weights and change bestMove/bestWeight
            if currentWeight >= bestWeight:
                bestWeight = currentWeight
                bestMove = "D"
                bestPiece = piece

        if playNDE.isMoveValid(piece, "R"):
            # evaluate move and return weight
            currentWeight = weighRisk(piece, "R", board, currentWeight)
            # compare weights and change bestMove/bestWeight
            if currentWeight >= bestWeight:
                bestWeight = currentWeight
                bestMove = "R"
                bestPiece = piece

        if playNDE.isMoveValid(piece, "X"):
            # evaluate move and return weight
            currentWeight = weighRisk(piece, "X", board, currentWeight)
            # compare weights and change bestMove/bestWeight
            if currentWeight >= bestWeight:
                bestWeight = currentWeight
                bestMove = "E"
                bestPiece = piece
    print([bestPiece, bestMove])
    return bestPiece, bestMove
            

if __name__ == "__main__":
    evaluateMoves()