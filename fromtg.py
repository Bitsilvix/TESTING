from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QTimer
import pygame
from pygame.locals import *
import sys

# Класс основного окна игры
class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide2 + PyGame Платформер")
        self.setGeometry(100, 100, 800, 600)
        
        # Инициализация PyGame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        
        # Инициализация игровых элементов
        self.player = pygame.Rect(100, 500, 50, 50)
        self.platforms = [
            pygame.Rect(0, 550, 800, 50),  # Пол
            pygame.Rect(200, 450, 150, 20),  # Платформа 1
            pygame.Rect(450, 350, 150, 20)   # Платформа 2
        ]
        
        self.velocity = pygame.Vector2(0, 0)
        self.jumping = False
        
        # Таймер для обновления игры
        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(17)  # ~60 FPS (1000ms / 60 ≈ 17ms)
    
    def game_loop(self):
        self.handle_input()
        self.update_player()
        self.draw_elements()
        self.clock.tick(60)
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.velocity.x = -5
        elif keys[K_RIGHT]:
            self.velocity.x = 5
        else:
            self.velocity.x = 0
        
        if keys[K_SPACE] and not self.jumping:
            self.velocity.y = -15
            self.jumping = True
    
    def update_player(self):
        # Гравитация
        self.velocity.y += 1
        self.player.x += self.velocity.x
        self.player.y += self.velocity.y
        
        # Проверка столкновений с платформами
        for platform in self.platforms:
            if self.player.colliderect(platform):
                if self.velocity.y > 0:  # Падение вниз
                    self.player.bottom = platform.top
                    self.velocity.y = 0
                    self.jumping = False
                elif self.velocity.y < 0:  # Движение вверх
                    self.player.top = platform.bottom
                    self.velocity.y = 0
    
    def draw_elements(self):
        self.screen.fill((0, 0, 0))  # Очистить экран
        
        # Рисование платформ
        for platform in self.platforms:
            pygame.draw.rect(self.screen, (0, 255, 0), platform)
        
        # Рисование игрока
        pygame.draw.rect(self.screen, (0, 0, 255), self.player)
        
        pygame.display.flip()  # Обновление экрана

# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec_())