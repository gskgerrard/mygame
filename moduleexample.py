import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def check_collide(self, gameObkect):
        return self.rect.colliderect(gameObkect.rect)

class make_display():
    def __init__(self, width, height, bg, caption):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.bg = pygame.image.load(bg)
        self.bg = pygame.transform.scale(self.bg, (width, height))
        self.window.blit(self.bg, (0, 0))
    def update_background(self):
        self.window.blit(self.bg, (0, 0))
    def add_sprite(self, image, rect):
        self.window.blit(image, rect)
    def update_frame(self):
        pygame.display.update()

    def create_rect(self, x, y, w, h, c):
        self.rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(self.window, c, self.rect)
        return self.rect
        

class TextArea():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def set_text(self, text, fsize, txt_color=(0, 0, 0)):
        return pygame.font.SysFont('verdana', fsize).render(text, True, txt_color)
    


