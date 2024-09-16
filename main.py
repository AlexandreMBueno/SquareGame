import pygame, random

pygame.init()
size = (1600, 1200)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class Square:
    def __init__(self, speed):
        self.x = random.randint(0, 1580)
        self.y = random.randint(0, 1180)
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.color = [random.randint(0, 255) for _ in range(3)]
        self.speed = speed
        self.size = 30

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        collided = False

        # colisao dos quadrados com as paredes
        if self.x < 0:
            self.x = 0
            self.dx = -self.dx
            collided = True
        elif self.x > 1580 - self.size:
            self.x = 1580 - self.size
            self.dx = -self.dx
            collided = True

        if self.y < 0:
            self.y = 0
            self.dy = -self.dy
            collided = True
        elif self.y > 1180 - self.size:
            self.y = 1180 - self.size
            self.dy = -self.dy
            collided = True

        return collided

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))

# funcao q exibe texto na tela
def show_message(text, x, y, font_size=50):
    font = pygame.font.SysFont(None, font_size)
    message = font.render(text, True, (255, 255, 255))
    screen.blit(message, (x, y))

# funcao so centralizazr texto de limite pq tava torto
def show_centered_message(text, font_size=50):
    font = pygame.font.SysFont(None, font_size)
    message = font.render(text, True, (255, 255, 255))
    text_rect = message.get_rect(center=(size[0] // 2, size[1] // 2))
    screen.blit(message, text_rect)

squares = [Square(2)]  # comeca com velocidade 2 (antes, a velocidade aumentava ent podemos deixar so uma speed)
current_speed = 2  # velocidade dos quadrados
max_squares = 1000  # Limite de quadrados

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Atualiza e desenha os quadrados
    screen.fill((0, 0, 0))
    new_square_needed = False

    for square in squares:
        if square.move():
            new_square_needed = True  # Marca que um novo quadrado sera gerado
        square.draw()

    # limite de quadrados atingido
    if len(squares) >= max_squares:
        show_centered_message(f"Limite de {max_squares} quadrados atingido", font_size=50)
    #  # add novo quadrado se colidiu e limite n foi atingido
    elif new_square_needed and len(squares) < max_squares:
        squares.append(Square(current_speed))

    # msg de n de quadrados
    show_message(f"Numero de quadrados: {len(squares)}", 10, size[1] - 50, font_size=50)

    pygame.display.flip()
    clock.tick(60)
