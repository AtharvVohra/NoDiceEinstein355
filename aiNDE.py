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


def weighDistance(piece, move, board, currentWeight): # weighs minimized distance to goal for each move a piece can make
    updatedRow = piece.row
    updatedCol = piece.col
    if move == "D":
        updatedRow = piece.row + 1
    elif move == "R":
        updatedCol = piece.col + 1
    elif move == "X":
        updatedRow = piece.row + 1
        updatedCol = piece.col + 1
    # honestly, this just checks if it made a diagonal move but...
    distance = ((5 - piece.row) + (5 - piece.col))
    updatedDistance = ((5 - updatedRow) + (5 - updatedCol)) 
    if updatedDistance - distance > 1:
        currentWeight += 2
    return currentWeight


def weighTake(piece, move, board, currentWeight): # assigns weights for taking an opponent's piece and taking your own pieces
    updatedRow = piece.row
    updatedCol = piece.col
    if move == "D":
        updatedRow = piece.row + 1
    elif move == "R":
        updatedCol = piece.col + 1
    elif move == "X":
        updatedRow = piece.row + 1
        updatedCol = piece.col + 1
    # check if an ally piece is to the right, down or diagonal
    if updatedCol < 4:
        if board.board[updatedRow][updatedCol + 1] and board.board[updatedRow][updatedCol + 1].color == "red": # to the right
            if board.board[updatedRow][updatedCol + 1].val != 1 and board.board[updatedRow][updatedCol + 1].val != 6:
                currentWeight -= 1
    if updatedRow < 4:
        if board.board[updatedRow + 1][updatedCol] and board.board[updatedRow + 1][updatedCol].color == "red": # to the right
            if board.board[updatedRow + 1][updatedCol].val != 1 and board.board[updatedRow + 1][updatedCol].val != 6:
                currentWeight -= 1
    if updatedRow < 4 and updatedCol < 4:
        if board.board[updatedRow + 1][updatedCol + 1] and board.board[updatedRow + 1][updatedCol + 1].color == "red": # to the right
            if board.board[updatedRow + 1][updatedCol + 1].val != 1 and board.board[updatedRow + 1][updatedCol + 1].val != 6:
                currentWeight -= 1
    return currentWeight


def weighDefense(pieceToMove:classes.Piece, move:str, board:classes.Board, currentWeight:float) -> float:
    """
    Moves that put a one-space buffer between our piece and the opponent's are
    highly coveted. Call it "area control". Assumes the AI is playing red.
    """ 
    print(pieceToMove, move)
    print(board)
    # First get the current "area" we control.
    options = []
    for adj in [(0,1),(1,1),(1,0)]: # (x,y): down, diag, right respectively
        adjCol = pieceToMove.col + adj[0]
        adjRow = pieceToMove.row + adj[1]
        # If there's an adjacent enemy, obviously area control means nothing.
        #if board.getColorFromCoords(adjRow, adjCol) == "blue": # TODO: see paper note
        #    # Enemy piece; we're done here
        #    continue
        # Check to see if any enemies can move INTO this adjacent space
        numEnemies = 0
        if adj == (1,1):
            for farAdj in [(0,1),(1,1),(1,0)]:
                farCol = adjCol + farAdj[0]
                farRow = adjRow + farAdj[1]
                if board.getColorFromCoords(farRow, farCol) == "blue":
                    numEnemies += 1
        elif adj == (0,1):
            # Do not overlap checking neighbours with (1,1)
            if board.getColorFromCoords(adjRow+1, adjCol) == "blue":
                numEnemies += 1
        elif adj == (1,0):
            # Same thing; don't look at the same neighbouring spaces as (1,1)
            if board.getColorFromCoords(adjRow, adjCol+1) == "blue":
                numEnemies += 1
        options.append( (adj, numEnemies) )
    for o in options:
        print(o)
    print()
    
    # Now see if we could increase our area control by making this move.
    #print(pieceToMove.col, pieceToMove.row)
    return currentWeight
    
    
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
        
        for move in ("D", "R", "X"):
            currentWeight = weighDefense(piece, move, board, currentWeight)
        print("currentWeight", currentWeight)
        sys.exit()
        
        if playNDE.isMoveValid(piece, "D"):
            # evaluate move and return weight
            currentWeight = weighTake(piece, "D", board, currentWeight)
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
                bestMove = "E" # ??
                bestPiece = piece
    print([bestPiece, bestMove])
    return bestPiece, bestMove
            

# if __name__ == "__main__":
#     evaluateMoves()
