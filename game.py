import pygame
from board import Board
from pieces import PieceColor
from ai import AIPlayer

class Game:
    SCREEN_WIDTH = 1500
    SCREEN_HEIGHT = 1080
    SPLASH_DURATION = 1000  # in milliseconds

    def __init__(self):
        self.window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Chess Game")
        self.renderer = pygame.Surface(self.window.get_size())
        self.font = pygame.font.Font("assets/sansserif.ttf", 24)
        self.board = Board(self.renderer, self.font)
        self.is_running = True
        self.showing_splash = True
        self.splash_start_time = pygame.time.get_ticks()
        self.current_player = None  # Will be set after player chooses side
        self.game_over = False
        self.winner = None
        self.player_color = None  # Player's chosen color
        self.ai_player = AIPlayer(depth=3)  # Initialize AI player and difficulty
        self.waiting_for_side_selection = True  # Flag to check if side selection is pending
        self.ai_has_moved = False  # Flag to track if AI has moved this turn


    def initialize(self):
        self.board.initialize()
        self.show_splash()

    def show_splash(self):
        splash = pygame.image.load("assets/chess2d-splash.webp").convert()
        splash = pygame.transform.scale(splash, self.window.get_size())
        self.renderer.blit(splash, (0, 0))
        self.window.blit(self.renderer, (0, 0))
        pygame.display.flip()

    def run(self):
        self.initialize()
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            pygame.time.delay(16)  # Cap frame rate at ~60 FPS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False  # Exit the game

            if self.waiting_for_side_selection:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player_color = PieceColor.WHITE
                        self.current_player = PieceColor.WHITE
                        self.waiting_for_side_selection = False
                    elif event.key == pygame.K_b:
                        self.player_color = PieceColor.BLACK
                        self.current_player = PieceColor.WHITE  # White always starts
                        self.waiting_for_side_selection = False
            elif self.game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                    self.restart_game()
            else:
                if event.type == pygame.KEYDOWN:
                    pass  # Placeholder for any key events during the game

                if self.current_player == self.player_color:
                    self.board.handle_event(event, self.current_player)
                else:
                    pass  # No event handling needed during AI's turn

    def update(self):
        if self.showing_splash:
            if pygame.time.get_ticks() - self.splash_start_time >= self.SPLASH_DURATION:
                self.showing_splash = False
        elif not self.waiting_for_side_selection and not self.game_over:
            if self.current_player == self.player_color:
                self.board.update()
                if self.board.move_made:
                    self.board.move_made = False  # Reset the flag
                    self.check_game_over()
                    if not self.game_over:
                        self.switch_turn()
            else:
                if not self.ai_has_moved:
                    # AI makes a move
                    self.ai_move()
                    self.ai_has_moved = True
                    self.check_game_over()
                    if not self.game_over:
                        self.switch_turn()
                        self.ai_has_moved = False  # Reset for next AI turn


    def render(self):
        self.renderer.fill((50, 50, 50))  # Dark grey background

        if self.showing_splash:
            self.show_splash()
        else:
            self.board.render()
            self._render_info_bar()
            self._render_right_panel()

        self.window.blit(self.renderer, (0, 0))
        pygame.display.flip()

    def _render_info_bar(self):
        square_size = self.renderer.get_height() // 8
        info_bar_height = square_size // 2
        info_bar_rect = pygame.Rect(0, 8 * square_size, self.renderer.get_width(), info_bar_height)
        pygame.draw.rect(self.renderer, (50, 50, 50), info_bar_rect)

    def _render_right_panel(self):
        # Calculate dimensions
        board_size = self.renderer.get_height()  # The board is square and fills the height
        right_panel_x = board_size
        right_panel_width = self.renderer.get_width() - board_size
        if right_panel_width <= 0:
            return  # No space to render right panel

        # Draw dark blue rectangle at the top of the right panel
        rect_height = 60
        dark_blue = (0, 0, 139)  # Dark blue color
        rect = pygame.Rect(right_panel_x, 0, right_panel_width, rect_height)
        pygame.draw.rect(self.renderer, dark_blue, rect)

        # Render the title text
        title_text = "Chess 2D Python game"
        text_color = (255, 255, 255)  # White color
        text_surface = self.font.render(title_text, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (
            right_panel_x + right_panel_width // 2,
            rect_height // 2,
        )
        self.renderer.blit(text_surface, text_rect)

        # Draw dark green rectangle for side selection or player info
        green_rect_height = 100  # Increased height to accommodate multiple lines
        dark_green = (0, 100, 0)  # Dark green color
        green_rect = pygame.Rect(
            right_panel_x, rect_height, right_panel_width, green_rect_height
        )
        pygame.draw.rect(self.renderer, dark_green, green_rect)

        if self.waiting_for_side_selection:
            # Render the side selection question
            question_lines = [
                "What side do you want to play?",
                "Press 'B' for Black or 'W' for White",
            ]
            small_font = pygame.font.Font("assets/sansserif.ttf", 20)  # Smaller font size
            line_spacing = 5  # Spacing between lines
            total_text_height = sum(
                [small_font.size(line)[1] for line in question_lines]
            ) + (len(question_lines) - 1) * line_spacing
            start_y = rect_height + (green_rect_height - total_text_height) // 2

            for line in question_lines:
                line_surface = small_font.render(line, True, (255, 255, 255))
                line_rect = line_surface.get_rect()
                line_rect.center = (
                    right_panel_x + right_panel_width // 2,
                    start_y + line_surface.get_height() // 2,
                )
                self.renderer.blit(line_surface, line_rect)
                start_y += line_surface.get_height() + line_spacing
        else:
            # Render the chosen side
            chosen_text = f"You are playing: {'White' if self.player_color == PieceColor.WHITE else 'Black'}"
            chosen_surface = self.font.render(chosen_text, True, (255, 255, 255))
            chosen_rect = chosen_surface.get_rect()
            chosen_rect.center = (
                right_panel_x + right_panel_width // 2,
                rect_height + green_rect_height // 2,
            )
            self.renderer.blit(chosen_surface, chosen_rect)

            # Draw dark red rectangle for turn info or game over message
            red_rect_height = 60
            dark_red = (139, 0, 0)  # Dark red color
            red_rect_y = rect_height + green_rect_height
            red_rect = pygame.Rect(
                right_panel_x, red_rect_y, right_panel_width, red_rect_height
            )
            pygame.draw.rect(self.renderer, dark_red, red_rect)

            if self.game_over:
                if self.winner is None:
                    result_text = "Stalemate! Press 'N' to restart"
                elif self.winner == self.player_color:
                    result_text = "You win! Press 'N' to restart"
                else:
                    result_text = "You lose! Press 'N' to restart"
                result_surface = self.font.render(result_text, True, (255, 255, 255))
                result_rect = result_surface.get_rect()
                result_rect.center = (
                    right_panel_x + right_panel_width // 2,
                    red_rect_y + red_rect_height // 2,
                )
                self.renderer.blit(result_surface, result_rect)
            else:
                # Render turn info
                turn_desc = (
                    'your' if self.current_player == self.player_color else "computer's"
                )
                turn_text = f"It is {turn_desc} turn"
                turn_surface = self.font.render(turn_text, True, (255, 255, 255))
                turn_rect = turn_surface.get_rect()
                turn_rect.center = (
                    right_panel_x + right_panel_width // 2,
                    red_rect_y + red_rect_height // 2,
                )
                self.renderer.blit(turn_surface, turn_rect)




    def switch_turn(self):
        self.current_player = PieceColor.BLACK if self.current_player == PieceColor.WHITE else PieceColor.WHITE
        self.board.move_made = False  # Reset the move_made flag for the next turn
        # Reset AI move flag if it's now AI's turn
        if self.current_player != self.player_color:
            self.ai_has_moved = False


    def ai_move(self):
        move = self.ai_player.get_best_move(self.board, self.current_player)
        if move:
            self.board.move_piece(move['start'], move['end'])
            self.board.move_made = True
        else:
            # No moves available, game over (checkmate or stalemate)
            self.game_over = True
            self.winner = self.player_color  # Player wins if AI cannot move


    def check_game_over(self):
        if self.board.is_king_captured(PieceColor.WHITE):
            self.game_over = True
            self.winner = PieceColor.BLACK
        elif self.board.is_king_captured(PieceColor.BLACK):
            self.game_over = True
            self.winner = PieceColor.WHITE
        else:
            # Check for checkmate or stalemate
            if not self.has_moves(self.current_player):
                if self.board.is_in_check(self.current_player):
                    # Checkmate
                    self.game_over = True
                    self.winner = PieceColor.BLACK if self.current_player == PieceColor.WHITE else PieceColor.WHITE
                else:
                    # Stalemate
                    self.game_over = True
                    self.winner = None  # Draw

    def has_moves(self, color):
        moves = self.board.generate_all_legal_moves(color)
        return len(moves) > 0


    def restart_game(self):
        self.board.initialize()
        self.game_over = False
        self.winner = None
        self.waiting_for_side_selection = True
        self.player_color = None
        self.current_player = None

