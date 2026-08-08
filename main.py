# import pygame
# import sys

# # Initialize pygame
# pygame.init()

# # Window settings
# WIDTH, HEIGHT = 600, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Tic Tac Toe")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Game variables
# board = [["" for _ in range(3)] for _ in range(3)]
# current_player = "X"

# winner = None
# game_over = False

# # Fill background
# screen.fill(WHITE)

# # Draw grid
# pygame.draw.line(screen, BLACK, (200, 0), (200, 600), 5)
# pygame.draw.line(screen, BLACK, (400, 0), (400, 600), 5)

# pygame.draw.line(screen, BLACK, (0, 200), (600, 200), 5)
# pygame.draw.line(screen, BLACK, (0, 400), (600, 400), 5)

# pygame.display.update()

# def draw_marks():
#     font = pygame.font.SysFont(None, 120)

#     for row in range(3):
#         for col in range(3):

#             if board[row][col] != "":
#                 text = font.render(board[row][col], True, BLACK)

#                 x = col * 200 + 60
#                 y = row * 200 + 35

#                 screen.blit(text, (x, y))

# # Game loop
# running = True

# while running:

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             running = False

#         elif event.type == pygame.MOUSEBUTTONDOWN:

#             x, y = pygame.mouse.get_pos()

#             row = y // 200
#             col = x // 200

#             if board[row][col] == "":

#                 board[row][col] = current_player

#                 if current_player == "X":
#                     current_player = "O"
#                 else:
#                     current_player = "X"

#     screen.fill(WHITE)

#     # Draw grid
#     pygame.draw.line(screen, BLACK, (200, 0), (200, 600), 5)
#     pygame.draw.line(screen, BLACK, (400, 0), (400, 600), 5)

#     pygame.draw.line(screen, BLACK, (0, 200), (600, 200), 5)
#     pygame.draw.line(screen, BLACK, (0, 400), (600, 400), 5)

#     draw_marks()

#     pygame.display.update()

# pygame.quit()
# sys.exit()