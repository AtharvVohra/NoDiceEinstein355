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
        piecesToPick.append(pieceList[0])
        return piecesToPick

def weighDistance(pieceToMove, move, board, currentWeight): # weighs minimized distance to goal for each move a piece can make
    return

def weighTake(pieceToMove, move, board, currentWeight): # assigns weights for taking an opponent's piece and taking your own pieces
    return

def weighDefense(pieceToMove, move, board, currentWeight): # weighs defensiveness of each move a piece can make
    return
    
def weighRisk(pieceToMove, move, board, currentWeight): # weighs risk of each move a piece can make
    return

def evaluateMoves(board, weightTotal, possibleMoves, pieceList):
    piecesToPick = evaluateMoves(pieceList)
    bestPiece = piecesToPick[0]
    bestWeight = 0
    bestMove = None
    for piece in piecesToPick:
        # go through all the pieces and evaluate all the moves they can make, updating bestMove and bestPiece in the process
        # possible moves for red, run weight checks and record new weight
        if playNDE.isMoveValid(piece, "D"):
            # evaluate move and return weight
            # compare weights and change bestMove/bestWeight

        if playNDE.isMoveValid(piece, "R"):
            # evaluate move and return weight
            # compare weights and change bestMove/bestWeight

        if playNDE.isMoveValid(piece, "X"):
            # evaluate move and return weight
            # compare weights and change bestMove/bestWeight
            

if __name__ == "__main__":
    evaluateMoves()