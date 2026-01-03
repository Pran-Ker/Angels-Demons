import pygame
from pygame.locals import QUIT

import time

import sys

## Initialize Pygame
pygame.init()

board = [['  ' for i in range(8)] for i in range(8)]

## Creates a chess piece class that shows what team a piece is on, what type of piece it is and whether or not it can be killed by another selected piece.
class Piece:
    def __init__(self, team, type, image, killable=False):
        self.team = team
        self.type = type
        self.killable = killable
        self.image = image


## Creates instances of chess pieces with correct image paths
bp = Piece('b', 'p', 'images/bP.png')
wp = Piece('w', 'p', 'images/wP.png')
bk = Piece('b', 'k', 'images/bK.png')
wk = Piece('w', 'k', 'images/wK.png')
br = Piece('b', 'r', 'images/bR.png')
wr = Piece('w', 'r', 'images/wR.png')
bb = Piece('b', 'b', 'images/bB.png')
wb = Piece('w', 'b', 'images/wB.png')
bq = Piece('b', 'q', 'images/bQ.png')
wq = Piece('w', 'q', 'images/wQ.png')
bkn = Piece('b', 'kn', 'images/bN.png')
wkn = Piece('w', 'kn', 'images/wN.png')


## Angels-Demons starting position
## Demons (Black) on top: 2 Rooks, 2 Knights, 2 Bishops
## Angels (White) on bottom: 1 King only
starting_order = {}
for row in range(8):
    for col in range(8):
        starting_order[(col, row)] = None

## Demons setup (row 0)
starting_order[(0, 0)] = pygame.image.load('images/bR.png')  # Black Rook
starting_order[(1, 0)] = pygame.image.load('images/bN.png')  # Black Knight
starting_order[(2, 0)] = pygame.image.load('images/bB.png')  # Black Bishop
starting_order[(5, 0)] = pygame.image.load('images/bB.png')  # Black Bishop
starting_order[(6, 0)] = pygame.image.load('images/bN.png')  # Black Knight
starting_order[(7, 0)] = pygame.image.load('images/bR.png')  # Black Rook

## Angel setup (row 7, center)
starting_order[(3, 7)] = pygame.image.load('images/wK.png')  # White King


def create_board(board):
    ## Angels-Demons board setup
    ## Row 0: Demons (Black) - 2 Rooks, 2 Knights, 2 Bishops
    board[0] = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    board[0][0] = Piece('b', 'r', 'images/bR.png')  # Black Rook
    board[0][1] = Piece('b', 'kn', 'images/bN.png')  # Black Knight
    board[0][2] = Piece('b', 'b', 'images/bB.png')  # Black Bishop
    board[0][5] = Piece('b', 'b', 'images/bB.png')  # Black Bishop
    board[0][6] = Piece('b', 'kn', 'images/bN.png')  # Black Knight
    board[0][7] = Piece('b', 'r', 'images/bR.png')  # Black Rook

    ## Rows 1-6: Empty
    for i in range(1, 7):
        board[i] = ['  ' for _ in range(8)]

    ## Row 7: Angels (White) - 1 King only
    board[7] = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    board[7][3] = Piece('w', 'k', 'images/wK.png')  # White King

    return board


## returns the input if the input is within the boundaries of the board
def on_board(position):
    if position[0] > -1 and position[1] > -1 and position[0] < 8 and position[1] < 8:
        return True


## returns a string that places the rows and columns of the board in a readable manner
def convert_to_readable(board):
    output = ''

    for i in board:
        for j in i:
            try:
                output += j.team + j.type + ', '
            except:
                output += j + ', '
        output += '\n'
    return output


## resets "x's" and killable pieces
def deselect():
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 'x ':
                board[row][column] = '  '
            else:
                try:
                    board[row][column].killable = False
                except:
                    pass
    return convert_to_readable(board)


## Takes in board as argument then returns 2d array containing positions of valid moves
def highlight(board):
    highlighted = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'x ':
                highlighted.append((i, j))
            else:
                try:
                    if board[i][j].killable:
                        highlighted.append((i, j))
                except:
                    pass
    return highlighted

def check_team(moves, index):
    row, col = index
    if moves%2 == 0:
        if board[row][col].team == 'w':
            return True
    else:
        if board[row][col].team == 'b':
            return True

## This takes in a piece object and its index then runs then checks where that piece can move using separately defined functions for each type of piece.
def select_moves(piece, index, moves):
    if check_team(moves, index):
        if piece.type == 'p':
            if piece.team == 'b':
                return highlight(pawn_moves_b(index))
            else:
                return highlight(pawn_moves_w(index))

        if piece.type == 'k':
            return highlight(king_moves(index))

        if piece.type == 'r':
            return highlight(rook_moves(index))

        if piece.type == 'b':
            return highlight(bishop_moves(index))

        if piece.type == 'q':
            return highlight(queen_moves(index))

        if piece.type == 'kn':
            return highlight(knight_moves(index))


## Basically, check black and white pawns separately and checks the square above them. If its free that space gets an "x" and if it is occupied by a piece of the opposite team then that piece becomes killable.
def pawn_moves_b(index):
    if index[0] == 1:
        if board[index[0] + 2][index[1]] == '  ' and board[index[0] + 1][index[1]] == '  ':
            board[index[0] + 2][index[1]] = 'x '
    bottom3 = [[index[0] + 1, index[1] + i] for i in range(-1, 2)]

    for positions in bottom3:
        if on_board(positions):
            if bottom3.index(positions) % 2 == 0:
                try:
                    if board[positions[0]][positions[1]].team != 'b':
                        board[positions[0]][positions[1]].killable = True
                except:
                    pass
            else:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
    return board

def pawn_moves_w(index):
    if index[0] == 6:
        if board[index[0] - 2][index[1]] == '  ' and board[index[0] - 1][index[1]] == '  ':
            board[index[0] - 2][index[1]] = 'x '
    top3 = [[index[0] - 1, index[1] + i] for i in range(-1, 2)]

    for positions in top3:
        if on_board(positions):
            if top3.index(positions) % 2 == 0:
                try:
                    if board[positions[0]][positions[1]].team != 'w':
                        board[positions[0]][positions[1]].killable = True
                except:
                    pass
            else:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
    return board


## This just checks a 3x3 tile surrounding the king. Empty spots get an "x" and pieces of the opposite team become killable.
def king_moves(index):
    for y in range(3):
        for x in range(3):
            if on_board((index[0] - 1 + y, index[1] - 1 + x)):
                if board[index[0] - 1 + y][index[1] - 1 + x] == '  ':
                    board[index[0] - 1 + y][index[1] - 1 + x] = 'x '
                else:
                    if board[index[0] - 1 + y][index[1] - 1 + x].team != board[index[0]][index[1]].team:
                        board[index[0] - 1 + y][index[1] - 1 + x].killable = True
    return board


## This creates 4 lists for up, down, left and right and checks all those spaces for pieces of the opposite team. The list comprehension is pretty long so if you don't get it just msg me.
def rook_moves(index):
    cross = [[[index[0] + i, index[1]] for i in range(1, 8 - index[0])],
             [[index[0] - i, index[1]] for i in range(1, index[0] + 1)],
             [[index[0], index[1] + i] for i in range(1, 8 - index[1])],
             [[index[0], index[1] - i] for i in range(1, index[1] + 1)]]

    for direction in cross:
        for positions in direction:
            if on_board(positions):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                        board[positions[0]][positions[1]].killable = True
                    break
    return board


## Same as the rook but this time it creates 4 lists for the diagonal directions and so the list comprehension is a little bit trickier.
def bishop_moves(index):
    diagonals = [[[index[0] + i, index[1] + i] for i in range(1, 8)],
                 [[index[0] + i, index[1] - i] for i in range(1, 8)],
                 [[index[0] - i, index[1] + i] for i in range(1, 8)],
                 [[index[0] - i, index[1] - i] for i in range(1, 8)]]

    for direction in diagonals:
        for positions in direction:
            if on_board(positions):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                        board[positions[0]][positions[1]].killable = True
                    break
    return board


## applies the rook moves to the board then the bishop moves because a queen is basically a rook and bishop in the same position.
def queen_moves(index):
    board = rook_moves(index)
    board = bishop_moves(index)
    return board


## Checks a 5x5 grid around the piece and uses pythagoras to see if if a move is valid. Valid moves will be a distance of sqrt(5) from centre
def knight_moves(index):
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i ** 2 + j ** 2 == 5:
                if on_board((index[0] + i, index[1] + j)):
                    if board[index[0] + i][index[1] + j] == '  ':
                        board[index[0] + i][index[1] + j] = 'x '
                    else:
                        if board[index[0] + i][index[1] + j].team != board[index[0]][index[1]].team:
                            board[index[0] + i][index[1] + j].killable = True
    return board


WIDTH = 800

WIN = pygame.display.set_mode((WIDTH, WIDTH))

""" This is creating the window that we are playing on, it takes a tuple argument which is the dimensions of the window so in this case 800 x 800px
"""

pygame.display.set_caption("Angels & Demons")
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
DARK_RED = (139, 0, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_GREY = (64, 64, 64)
GREEN = (0, 200, 0)


class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = WHITE
        self.occupied = None

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, WIDTH / 8, WIDTH / 8))

    def setup(self, WIN):
        if starting_order[(self.row, self.col)]:
            if starting_order[(self.row, self.col)] == None:
                pass
            else:
                WIN.blit(starting_order[(self.row, self.col)], (self.x, self.y))

        """
        For now it is drawing a rectangle but eventually we are going to need it
        to use blit to draw the chess pieces instead
        """


def make_grid(rows, width):
    grid = []
    gap = WIDTH // rows
    print(gap)
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)
            if (i+j)%2 ==1:
                grid[i][j].colour = GREY
    return grid
"""
This is creating the nodes thats are on the board(so the chess tiles)
I've put them into a 2d array which is identical to the dimesions of the chessboard
"""


def draw_grid(win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))

    """
    The nodes are all white so this we need to draw the grey lines that separate all the chess tiles
    from each other and that is what this function does"""


def update_display(win, grid, rows, width, moves=0, game_over=False, winner=None):
    for row in grid:
        for spot in row:
            spot.draw(win)
            spot.setup(win)
    draw_grid(win, rows, width)

    ## Draw UI elements
    if not game_over:
        draw_turn_indicator(win, width, moves)
        draw_instructions(win, width)

    pygame.display.update()

    ## Draw game over screen if game ended
    if game_over and winner:
        draw_game_over_screen(win, width, winner)


def Find_Node(pos, WIDTH):
    interval = WIDTH / 8
    y, x = pos
    rows = y // interval
    columns = x // interval
    return int(rows), int(columns)


def display_potential_moves(positions, grid):
    for i in positions:
        x, y = i
        grid[x][y].colour = BLUE
        """
        Displays all the potential moves
        """


def Do_Move(OriginalPos, FinalPosition, WIN):
    starting_order[FinalPosition] = starting_order[OriginalPos]
    starting_order[OriginalPos] = None


def spawn_pawn(position, board):
    """Spawns a white pawn at the given position when the King moves"""
    row, col = position
    board[row][col] = Piece('w', 'p', 'images/wP.png')
    starting_order[(col, row)] = pygame.image.load('images/wP.png')
    return board


def remove_highlight(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i+j)%2 == 0:
                grid[i][j].colour = WHITE
            else:
                grid[i][j].colour = GREY
    return grid
"""this takes in 2 co-ordinate parameters which you can get as the position of the piece and then the position of the node it is moving to
you can get those co-ordinates using my old function for swap"""


def check_angel_win(board):
    """Check if White King reached row 0 (top of board)"""
    for col in range(8):
        try:
            if board[0][col].team == 'w' and board[0][col].type == 'k':
                return True
        except:
            pass
    return False


def check_demon_win(board):
    """Check if White King has been captured (no longer on board)"""
    for row in range(8):
        for col in range(8):
            try:
                if board[row][col].team == 'w' and board[row][col].type == 'k':
                    return False  ## King still alive
            except:
                pass
    return True  ## King not found, Demons win


def draw_text(text, font_size, color, surface, x, y, center=True):
    """Helper function to draw text on screen"""
    font = pygame.font.Font(None, font_size)
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
    return text_rect


def draw_game_over_screen(WIN, WIDTH, winner):
    """Draw beautiful game over screen"""
    ## Semi-transparent overlay
    overlay = pygame.Surface((WIDTH, WIDTH))
    overlay.set_alpha(200)
    overlay.fill(BLACK)
    WIN.blit(overlay, (0, 0))

    ## Winner colors
    if winner == "Angels":
        title_color = GOLD
        subtitle = "The King reached the other side!"
        bg_color = LIGHT_BLUE
    else:
        title_color = DARK_RED
        subtitle = "The King has been captured!"
        bg_color = DARK_GREY

    ## Draw winner box
    box_width = 600
    box_height = 300
    box_x = (WIDTH - box_width) // 2
    box_y = (WIDTH - box_height) // 2

    pygame.draw.rect(WIN, bg_color, (box_x, box_y, box_width, box_height), border_radius=20)
    pygame.draw.rect(WIN, title_color, (box_x, box_y, box_width, box_height), 5, border_radius=20)

    ## Draw text
    draw_text(f"{winner.upper()} WIN!", 80, title_color, WIN, WIDTH // 2, WIDTH // 2 - 60)
    draw_text(subtitle, 40, WHITE, WIN, WIDTH // 2, WIDTH // 2)
    draw_text("Press R to Restart | ESC to Quit", 30, YELLOW, WIN, WIDTH // 2, WIDTH // 2 + 80)

    pygame.display.update()


def draw_turn_indicator(WIN, WIDTH, moves):
    """Draw turn indicator at the top of the screen"""
    if moves % 2 == 0:
        turn_text = "Angels' Turn (White)"
        turn_color = GOLD
    else:
        turn_text = "Demons' Turn (Black)"
        turn_color = DARK_RED

    ## Draw background bar
    pygame.draw.rect(WIN, DARK_GREY, (0, 0, WIDTH, 40))
    pygame.draw.rect(WIN, turn_color, (0, 0, WIDTH, 40), 3)

    ## Draw turn text
    draw_text(turn_text, 32, turn_color, WIN, WIDTH // 2, 20)


def draw_instructions(WIN, WIDTH):
    """Draw instructions at the bottom"""
    instructions = "Right-click to remove pawns | Angels win by reaching top row"
    draw_text(instructions, 20, LIGHT_BLUE, WIN, WIDTH // 2, WIDTH - 15)


create_board(board)


def main(WIN, WIDTH):
    moves = 0
    selected = False
    piece_to_move=[]
    grid = make_grid(8, WIDTH)
    game_over = False
    winner = None

    while True:
        pygame.time.delay(50) ##stops cpu dying
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            """This quits the program if the player closes the window"""

            ## Keyboard controls for game over
            if event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_r:  ## Restart
                    return main(WIN, WIDTH)  ## Restart the game
                if event.key == pygame.K_ESCAPE:  ## Quit
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not game_over:  ## Right-click
                """Right-click to remove white pawns (Angels' special ability)"""
                pos = pygame.mouse.get_pos()
                y, x = Find_Node(pos, WIDTH)
                try:
                    if board[x][y].team == 'w' and board[x][y].type == 'p':
                        board[x][y] = '  '
                        starting_order[(y, x)] = None
                        deselect()
                        remove_highlight(grid)
                        selected = False
                        print("Pawn removed!")
                except:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:  ## Left-click
                pos = pygame.mouse.get_pos()
                y, x = Find_Node(pos, WIDTH)
                if selected == False:
                    try:
                        possible = select_moves((board[x][y]), (x,y), moves)
                        for positions in possible:
                            row, col = positions
                            grid[row][col].colour = BLUE
                        piece_to_move = x,y
                        selected = True
                    except:
                        piece_to_move = []
                        print('Can\'t select')
                    #print(piece_to_move)

                else:
                    try:
                        if board[x][y].killable == True:
                            row, col = piece_to_move ## coords of original piece
                            moved_piece = board[row][col]
                            board[x][y] = moved_piece
                            board[row][col] = '  '

                            ## Spawn pawn if King moved (Angels special ability)
                            if moved_piece.team == 'w' and moved_piece.type == 'k':
                                spawn_pawn((row, col), board)

                            deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x), WIN)
                            moves += 1
                            print(convert_to_readable(board))

                            ## Check win conditions
                            if check_angel_win(board):
                                game_over = True
                                winner = "Angels"
                                print("ANGELS WIN! The King reached the other side!")
                            elif check_demon_win(board):
                                game_over = True
                                winner = "Demons"
                                print("DEMONS WIN! The King has been captured!")
                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                            print("Deselected")
                    except:
                        if board[x][y] == 'x ':
                            row, col = piece_to_move
                            moved_piece = board[row][col]
                            board[x][y] = moved_piece
                            board[row][col] = '  '

                            ## Spawn pawn if King moved (Angels special ability)
                            if moved_piece.team == 'w' and moved_piece.type == 'k':
                                spawn_pawn((row, col), board)

                            deselect()
                            remove_highlight(grid)
                            Do_Move((col, row), (y, x), WIN)
                            moves += 1
                            print(convert_to_readable(board))

                            ## Check win conditions
                            if check_angel_win(board):
                                game_over = True
                                winner = "Angels"
                                print("ANGELS WIN! The King reached the other side!")
                            elif check_demon_win(board):
                                game_over = True
                                winner = "Demons"
                                print("DEMONS WIN! The King has been captured!")
                        else:
                            deselect()
                            remove_highlight(grid)
                            selected = False
                            print("Invalid move")
                    selected = False

            update_display(WIN, grid, 8, WIDTH, moves, game_over, winner)


main(WIN, WIDTH)