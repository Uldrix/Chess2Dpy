from enum import Enum, auto

class ChessPiece(Enum):
    KING = auto()
    QUEEN = auto()
    BISHOP = auto()
    ROOK = auto()
    KNIGHT = auto()
    PAWN = auto()
    EMPTY = auto()

class PieceColor(Enum):
    WHITE = auto()
    BLACK = auto()
    NONE = auto()

class PiecePosition:
    def __init__(self, piece=ChessPiece.EMPTY, color=PieceColor.NONE):
        self.piece = piece
        self.color = color
