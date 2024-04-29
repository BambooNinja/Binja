
# Funktion zum Zeichnen des Kreuzsymbols
def draw_cross():
    pygame.draw.line(screen, BLACK, (SCREEN_WIDTH - 20, 20), (SCREEN_WIDTH - 40, 40), 2)
    pygame.draw.line(screen, BLACK, (SCREEN_WIDTH - 40, 20), (SCREEN_WIDTH - 20, 40), 2)

# Hauptschleife des Spiels
def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Überprüfe, ob auf das Kreuzsymbol geklickt wurde
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if SCREEN_WIDTH - 40 <= mouse_x <= SCREEN_WIDTH - 20 and 20 <= mouse_y <= 40:
                    pygame.quit()
                    sys.exit()

        # Fülle den Bildschirm mit Weiß
        screen.fill(WHITE)

        # Zeichne das Kreuzsymbol
        draw_cross()

        # Aktualisiere den Bildschirm
        pygame.display.flip()

main_menu()
