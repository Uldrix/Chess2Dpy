'''
/* //////////////////////////////////////////////////////////////////////////////////
// 
// Project :        Chess 2D 
// Description :    2D chess game in Python
// Programmer :     Uldrix | https://github.com/Uldrix
// Licence :        GNU
// 
// 
// 
//     ⠀⠀ ⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⠞⠋⠁⣀⣠⣴⣶⣾⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠆
//     ⠀ ⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⢻⣧⣤⣴⣿⠿⠋⠁⣴⡿⠿⢿⣿⣿⣿⣷⣶⣶⣶⣶⡶⠶⠚⠁⠀⠀⣠⣾⠏⠀
//⠀⠀⠀   ⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⣥⣤⣤⣭⣍⣁⡀⠀⠀⠘⣿⣇⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⢀⣠⣴⣿⠟⠁⠀⠀
//⠀⠀⠀⠀⠀ ⠀   ⠀⠀⠀⢀⣤⡶⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠘⢿⣷⣦⣄⣀⣀⣀⣀⣀⣤⣤⣶⣾⣿⡿⠛⠁⠀⠀⢀⡀
//⠀⠀   ⠀⠀ ⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⣩⣿⠿⠋⠁⠀⠀⣠⣶⠟⠋⠀
//⠀⠀   ⠀ ⠀⠀⢠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⠀⠀⠀⣼⣿⠁⠀⠀⠀⢠⣾⡿⠃⠀⠀⠀
//⠀   ⠀⠀⠀⣠⡟⡡⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠸⣿⣄⠀⢀⣴⣿⣿⠁⠀⠀⠀⠀
//⠀  ⠀⠀⢠⡟⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⢀⣤⠶⠒⠛⠛⠒⠲⢤⡀⠀⠘⣷⠀⠀⠀⠙⠻⠿⠿⢿⣿⠇⠀⠀⠀⠀⠀
//⠀  ⣠⡶⠿⢇⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⢀⡴⢪⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⢄⠀⢹⡄⠀⠀⠀⠀⠀⢀⣿⡟⠀⠀⠀⠀⠀⠀
//⠀  ⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⣦⣤⡞⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⡇⠀⠀⠀⢀⣠⣾⠟⢠⠀⠀⠀⠀⠀⠀
//⠀  ⠀⠀⡟⣿⣆⢀⠀⠀⠀⠀⠀⣠⠾⠕⠉⢉⣉⠀⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠃⠀⣠⣶⣿⠟⠋⢀⣾⠀⠀⠀⠀⠀⠀
//⠀⠀  ⠀⢰⣿⣿⣯⣧⠠⠮⠴⠞⣁⣠⣴⣾⣿⣿⣷⡌⣿⠋⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠉⠀⠀⣠⣾⡏⠀⠀⠀⠀⠀⠀
//  ⠀⣠⠴⢾⣿⣿⣿⣿⠀⠳⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⣤⣴⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀
//  ⢰⠁⠀⠀⠙⣿⣿⣧⠈⡆⢻⢿⣿⣿⣿⣿⣿⠿⠟⣃⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠂⣼⠀⢈⣩⣽⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
//  ⣞⠀⠀⠀⣠⣿⣿⡿⠀⢺⡀⢑⡈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠈⠻⣦⡞⠀⠀⠀⠀⠀⢠⣮⣾⣿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⢻⣦⣄⣴⡿⡿⠷⣿⠠⣀⡨⠥⣞⣳⡄⠀⢀⡀⠀⠀⠀⠀⠀⣀⣿⣇⠀⠀⠀⣀⣴⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⠀⠉⢻⠇⠀⠀⠀⠈⠣⠀⠀⠀⠀⢀⡽⣷⣄⡈⠉⠉⠀⠀⣊⣽⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠉⡴⣫⣿⣿⣒⡢⢄⣠⡾⠋⠉⠉⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⠀⢸⠛⣷⣤⢀⡄⢀⠇⣠⠂⣸⣡⣚⣼⠋⠁⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⠀⠘⣾⡀⡏⠙⡗⠻⠟⢻⠚⢻⢹⠙⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⠀⠀⠈⠓⠧⠴⣇⣴⣄⢼⣤⠟⠚⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
// 
// In Tenebris we code :: Forged by Uldrix :: Be aware of the Matrix :: ~~~~~~~~~~~~
// 
// ////////////////////////////////////////////////////////////////////////////////// */
'''
import pygame
from pieces import PiecePosition, PieceColor, ChessPiece

class Board:
    def __init__(self, renderer, font):
        self.renderer = renderer
        self.font = font
        self.board = [[PiecePosition() for _ in range(8)] for _ in range(8)]
        self.pieces_texture = None
        self.dragging_piece = None
        self.drag_start_pos = None
        self.drag_mouse_pos = None
        self.move_made = False
        self.selected_piece = None
        self.selected_pos = None
        self.move_stack = []  # Stack to keep track of moves for undoing


    def initialize(self):
        self.pieces_texture = pygame.image.load("assets/chessPieces.png").convert_alpha()
        self._setup_board()
        self.move_made = False

    def _setup_board(self):
        # Black pieces on the top rows
        self.board[0] = [
            PiecePosition(ChessPiece.ROOK, PieceColor.BLACK),
            PiecePosition(ChessPiece.KNIGHT, PieceColor.BLACK),
            PiecePosition(ChessPiece.BISHOP, PieceColor.BLACK),
            PiecePosition(ChessPiece.QUEEN, PieceColor.BLACK),
            PiecePosition(ChessPiece.KING, PieceColor.BLACK),
            PiecePosition(ChessPiece.BISHOP, PieceColor.BLACK),
            PiecePosition(ChessPiece.KNIGHT, PieceColor.BLACK),
            PiecePosition(ChessPiece.ROOK, PieceColor.BLACK),
        ]
        self.board[1] = [PiecePosition(ChessPiece.PAWN, PieceColor.BLACK) for _ in range(8)]

        # Empty squares
        for row in range(2, 6):
            self.board[row] = [PiecePosition(ChessPiece.EMPTY, PieceColor.NONE) for _ in range(8)]

        # White pieces on the bottom rows
        self.board[7] = [
            PiecePosition(ChessPiece.ROOK, PieceColor.WHITE),
            PiecePosition(ChessPiece.KNIGHT, PieceColor.WHITE),
            PiecePosition(ChessPiece.BISHOP, PieceColor.WHITE),
            PiecePosition(ChessPiece.QUEEN, PieceColor.WHITE),
            PiecePosition(ChessPiece.KING, PieceColor.WHITE),
            PiecePosition(ChessPiece.BISHOP, PieceColor.WHITE),
            PiecePosition(ChessPiece.KNIGHT, PieceColor.WHITE),
            PiecePosition(ChessPiece.ROOK, PieceColor.WHITE),
        ]
        self.board[6] = [PiecePosition(ChessPiece.PAWN, PieceColor.WHITE) for _ in range(8)]

    def render(self):
        square_size = self.renderer.get_height() // 8
        colors = [(240, 217, 181), (181, 136, 99)]

        # Render the board squares
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
                pygame.draw.rect(self.renderer, color, rect)

                # Render pieces (skip rendering dragged piece in its original position)
                piece = self.board[row][col]
                if piece.piece != ChessPiece.EMPTY and (not self.dragging_piece or (row, col) != self.drag_start_pos):
                    self._render_piece(piece, col * square_size, row * square_size, square_size)

        # Render dragged piece
        if self.dragging_piece and self.drag_mouse_pos:
            self._render_piece(self.dragging_piece, self.drag_mouse_pos[0] - square_size // 2,
                               self.drag_mouse_pos[1] - square_size // 2, square_size)

    def _render_piece(self, piece, x, y, square_size):
        piece_sprites = {
            PieceColor.BLACK: {
                ChessPiece.KING: (0, 0, 124, 290),
                ChessPiece.QUEEN: (124, 0, 120, 290),
                ChessPiece.BISHOP: (244, 0, 120, 290),
                ChessPiece.ROOK: (360, 0, 120, 290),
                ChessPiece.KNIGHT: (480, 0, 146, 290),
                ChessPiece.PAWN: (624, 0, 86, 290),
            },
            PieceColor.WHITE: {
                ChessPiece.KING: (0, 290, 124, 290),
                ChessPiece.QUEEN: (124, 290, 120, 290),
                ChessPiece.BISHOP: (244, 290, 120, 290),
                ChessPiece.ROOK: (360, 290, 120, 290),
                ChessPiece.KNIGHT: (480, 290, 146, 290),
                ChessPiece.PAWN: (624, 290, 86, 290),
            },
        }

        sprite = piece_sprites[piece.color].get(piece.piece)
        if sprite:
            src_rect = pygame.Rect(*sprite)

            piece_width = 80
            piece_height = 140
            dest_rect = pygame.Rect(
                x + (square_size - piece_width) // 2,
                y + (square_size - piece_height) // 2,
                piece_width,
                piece_height,
            )

            self.renderer.blit(pygame.transform.scale(self.pieces_texture.subsurface(src_rect), (piece_width, piece_height)), dest_rect)

    def handle_event(self, event, current_player):
        square_size = self.renderer.get_height() // 8

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            col, row = event.pos[0] // square_size, event.pos[1] // square_size
            if 0 <= row < 8 and 0 <= col < 8:
                piece = self.get_piece_at(row, col)
                if piece.color == current_player:
                    self.dragging_piece = piece
                    self.drag_start_pos = (row, col)
                    self.drag_mouse_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.dragging_piece:
                drop_col, drop_row = event.pos[0] // square_size, event.pos[1] // square_size
                if 0 <= drop_row < 8 and 0 <= drop_col < 8:
                    if self.is_legal_move(self.drag_start_pos, (drop_row, drop_col), self.dragging_piece):
                        self.move_piece(self.drag_start_pos, (drop_row, drop_col))
                    # Else, move is illegal; piece remains in place
                self.dragging_piece = None
                self.drag_start_pos = None
                self.drag_mouse_pos = None

        elif event.type == pygame.MOUSEMOTION and self.dragging_piece:
            self.drag_mouse_pos = event.pos


    def is_legal_move(self, start, end, piece, ignore_check=False):
        start_row, start_col = start
        end_row, end_col = end

        if not (0 <= end_row < 8 and 0 <= end_col < 8):
            return False  # Move is out of bounds

        target_piece = self.get_piece_at(end_row, end_col)
        if target_piece.color == piece.color:
            return False  # Cannot capture own piece

        delta_row = end_row - start_row
        delta_col = end_col - start_col

        # Movement rules as before
        if piece.piece == ChessPiece.PAWN:
            if not self._validate_pawn_move(start, end, piece):
                return False
        elif piece.piece == ChessPiece.KNIGHT:
            if not self._validate_knight_move(delta_row, delta_col):
                return False
        elif piece.piece == ChessPiece.BISHOP:
            if not self._validate_bishop_move(start, end):
                return False
        elif piece.piece == ChessPiece.ROOK:
            if not self._validate_rook_move(start, end):
                return False
        elif piece.piece == ChessPiece.QUEEN:
            if not self._validate_queen_move(start, end):
                return False
        elif piece.piece == ChessPiece.KING:
            if not self._validate_king_move(delta_row, delta_col):
                return False
        else:
            return False  # Unknown piece type

        if ignore_check:
            return True

        # Simulate the move to check for self-check
        original_end_piece = self.board[end_row][end_col]
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = PiecePosition()

        in_check = self.is_in_check(piece.color)

        # Undo the move
        self.board[start_row][start_col] = piece
        self.board[end_row][end_col] = original_end_piece

        return not in_check



    def move_piece(self, start, end):
        move = {'start': start, 'end': end}
        self.make_move(move)
        self.move_made = True  # Indicate that a move was made



    def get_piece_at(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return PiecePosition()

    def update(self):
        pass  # Placeholder for future updates

    def is_king_captured(self, color):
            for row in self.board:
                for piece in row:
                    if piece.piece == ChessPiece.KING and piece.color == color:
                        return False
            return True  # King not found; captured
        
    def _validate_pawn_move(self, start, end, piece):
        start_row, start_col = start
        end_row, end_col = end
        direction = -1 if piece.color == PieceColor.WHITE else 1
        starting_row = 6 if piece.color == PieceColor.WHITE else 1

        delta_row = end_row - start_row
        delta_col = end_col - start_col

        target_piece = self.get_piece_at(end_row, end_col)

        # Normal move forward
        if delta_col == 0:
            if delta_row == direction and target_piece.piece == ChessPiece.EMPTY:
                return True
            # Double move from starting position
            if start_row == starting_row and delta_row == 2 * direction and self.get_piece_at(start_row + direction, start_col).piece == ChessPiece.EMPTY and target_piece.piece == ChessPiece.EMPTY:
                return True
        # Capture
        elif abs(delta_col) == 1 and delta_row == direction and target_piece.piece != ChessPiece.EMPTY and target_piece.color != piece.color:
            return True

        return False

    def _validate_knight_move(self, delta_row, delta_col):
        return (abs(delta_row), abs(delta_col)) in [(2, 1), (1, 2)]

    def _validate_bishop_move(self, start, end):
        delta_row = end[0] - start[0]
        delta_col = end[1] - start[1]
        if abs(delta_row) != abs(delta_col):
            return False

        step_row = 1 if delta_row > 0 else -1
        step_col = 1 if delta_col > 0 else -1

        for i in range(1, abs(delta_row)):
            if self.get_piece_at(start[0] + i * step_row, start[1] + i * step_col).piece != ChessPiece.EMPTY:
                return False
        return True

    def _validate_rook_move(self, start, end):
        if start[0] != end[0] and start[1] != end[1]:
            return False

        if start[0] == end[0]:
            step = 1 if end[1] > start[1] else -1
            for col in range(start[1] + step, end[1], step):
                if self.get_piece_at(start[0], col).piece != ChessPiece.EMPTY:
                    return False
        else:
            step = 1 if end[0] > start[0] else -1
            for row in range(start[0] + step, end[0], step):
                if self.get_piece_at(row, start[1]).piece != ChessPiece.EMPTY:
                    return False
        return True

    def _validate_queen_move(self, start, end):
        return self._validate_bishop_move(start, end) or self._validate_rook_move(start, end)

    def _validate_king_move(self, delta_row, delta_col):
        return max(abs(delta_row), abs(delta_col)) == 1
    
    def is_in_check(self, color):
        king_position = self.find_king(color)
        if king_position is None:
            return True  # King is not on the board, considered as in check
        opponent_color = PieceColor.BLACK if color == PieceColor.WHITE else PieceColor.WHITE
        for row in range(8):
            for col in range(8):
                piece = self.get_piece_at(row, col)
                if piece.color == opponent_color:
                    if self.is_attack_move((row, col), king_position, piece):
                        return True
        return False

    def find_king(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.get_piece_at(row, col)
                if piece.piece == ChessPiece.KING and piece.color == color:
                    return (row, col)
        return None

    def is_attack_move(self, start, end, piece):
        # Similar to is_legal_move but ignores checks and assumes it's the opponent's turn
        return self.is_legal_move(start, end, piece, ignore_check=True)

    def generate_all_legal_moves(self, color):
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.get_piece_at(row, col)
                if piece.color == color:
                    legal_moves = self.get_legal_moves((row, col), piece)
                    for move in legal_moves:
                        moves.append({'start': (row, col), 'end': move})
        return moves

    def get_legal_moves(self, position, piece):
        legal_moves = []
        for row in range(8):
            for col in range(8):
                if self.is_legal_move(position, (row, col), piece):
                    legal_moves.append((row, col))
        return legal_moves

    def make_move(self, move):
        start_row, start_col = move['start']
        end_row, end_col = move['end']
        piece = self.board[start_row][start_col]
        captured_piece = self.board[end_row][end_col]

        # Save the move to the move stack for undoing later
        self.move_stack.append({
            'move': move,
            'piece_moved': piece,
            'piece_captured': captured_piece,
        })

        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = PiecePosition()

    def undo_move(self, move):
        last_move = self.move_stack.pop()
        start_row, start_col = last_move['move']['start']
        end_row, end_col = last_move['move']['end']
        piece_moved = last_move['piece_moved']
        piece_captured = last_move['piece_captured']

        self.board[start_row][start_col] = piece_moved
        self.board[end_row][end_col] = piece_captured

    def is_game_over(self):
        # Check if either king is captured
        if self.is_king_captured(PieceColor.WHITE) or self.is_king_captured(PieceColor.BLACK):
            return True
        return False

    def generate_all_legal_moves(self, color):
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.get_piece_at(row, col)
                if piece.color == color:
                    legal_moves = self.get_legal_moves((row, col), piece)
                    for move in legal_moves:
                        moves.append({'start': (row, col), 'end': move})
        return moves

    def get_legal_moves(self, position, piece):
        legal_moves = []
        for row in range(8):
            for col in range(8):
                if self.is_legal_move(position, (row, col), piece):
                    legal_moves.append((row, col))
        return legal_moves

