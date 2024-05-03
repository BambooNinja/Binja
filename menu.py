import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")


BG = pygame.transform.scale(pygame.image.load("assets/Background.jpg"), (1280, 720))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/small_pixel.ttf", size)
def draw_cross(screen):
    pygame.draw.line(screen, (0, 0, 0), (1270, 10), (1250, 30), 2)
    pygame.draw.line(screen, (0, 0, 0), (1250, 10), (1270, 30), 2)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((163, 201, 209))

        PLAY_TEXT = get_font(125).render("Level", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 120))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 600),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((163, 201, 209))

        OPTIONS_TEXT_1 = get_font(50).render("Thank you for visiting Binja!", True, "Black")
        OPTIONS_TEXT_2 = get_font(35).render("Background : freepik.com ", True, "Black")
        OPTIONS_TEXT_3 = get_font(35).render("Font : All-free-download.com", True, "Black")

        OPTIONS_TEXT_1_RECT = OPTIONS_TEXT_1.get_rect(center=(640, 200))
        OPTIONS_TEXT_2_RECT = OPTIONS_TEXT_2.get_rect(center=(640, 250))
        OPTIONS_TEXT_3_RECT = OPTIONS_TEXT_2.get_rect(center=(590, 300))

        SCREEN.blit(OPTIONS_TEXT_1, OPTIONS_TEXT_1_RECT)
        SCREEN.blit(OPTIONS_TEXT_2, OPTIONS_TEXT_2_RECT)
        SCREEN.blit(OPTIONS_TEXT_3, OPTIONS_TEXT_3_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color=(28,51,56))

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(125).render("MAIN MENU", True, "#1c3338")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 120))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 275),
                             text_input="PLAY", font=get_font(110), base_color="#5bc3d9", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 425),
                                text_input="CREDITS", font=get_font(110), base_color="#5bc3d9", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 575),
                             text_input="QUIT", font=get_font(110), base_color="#5bc3d9", hovering_color="White")

        draw_cross(SCREEN)  # Zeichne das Kreuzsymbol

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Überprüfe, ob das Kreuzsymbol angeklickt wurde
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 1250 <= mouse_x <= 1270 and 10 <= mouse_y <= 30:
                    pygame.quit()
                    sys.exit()
                # Überprüfe, ob die Buttons des Menüs angeklickt wurden
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()