import pygame
import random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GRID_ROWS = 10
GRID_COLS = 10
CELL_WIDTH = WINDOW_WIDTH // GRID_COLS
CELL_HEIGHT = WINDOW_HEIGHT // GRID_ROWS

# Creăm un eveniment personalizat care se va declanșa la fiecare 5 secunde
REGENERATE_COLORS_EVENT = pygame.USEREVENT + 1


def generate_random_color_grid():
    """
    Generează o matrice bidimensională (10x10) cu valori RGB complet aleatoare.
    """
    return [
        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(GRID_COLS)]
        for _ in range(GRID_ROWS)
    ]


def main():
    # Inițializarea modulelor Pygame
    pygame.init()

    # Configurarea ecranului și a titlului
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Procedural Color Grid (Auto-Regenerate 5s)")

    # Obținem prima matrice de culori
    color_grid = generate_random_color_grid()

    # Setăm timer-ul pentru regenerarea automată la 5000 de milisecunde (5 secunde)
    pygame.time.set_timer(REGENERATE_COLORS_EVENT, 5000)

    is_running = True

    # Bucla principală a programului
    while is_running:
        # 1. Curățăm ecranul (fundal negru)
        screen.fill((0, 0, 0))

        # 2. Desenăm grila de culori
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                color = color_grid[row][col]
                rect_x = col * CELL_WIDTH
                rect_y = row * CELL_HEIGHT
                
                # Desenăm pătratul curent pe ecran
                pygame.draw.rect(screen, color, (rect_x, rect_y, CELL_WIDTH, CELL_HEIGHT))

        # 3. Afișăm pe ecran ce am desenat în memorie
        pygame.display.flip()

        # 4. Gestionarea evenimentelor (Input & Timere)
        for event in pygame.event.get():
            # Ieșirea din program
            if event.type == pygame.QUIT:
                is_running = False
                
            # Regenerare manuală apăsând tasta SPACE
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                color_grid = generate_random_color_grid()
                
            # Regenerare automată declanșată de timer-ul de 5 secunde
            elif event.type == REGENERATE_COLORS_EVENT:
                color_grid = generate_random_color_grid()

    # Închidem resursele corect
    pygame.quit()

if __name__ == "__main__":
    main()
