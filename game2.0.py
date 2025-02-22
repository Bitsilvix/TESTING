import pygame
import random
import math

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Танчики")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Настройки танка
TANK_WIDTH, TANK_HEIGHT = 40, 40
TANK_SPEED = 2
BULLET_SPEED = 5
BULLET_COOLDOWN = 3000  # 3 секунды

# Настройки бонусов
BONUS_SIZE = 20
BONUS_TYPES = ["explosive_bullet", "shield", "invulnerability"]

# Класс танка
class Tank:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.hp = 15
        self.bullets = 5
        self.last_shot = pygame.time.get_ticks()
        self.shield = False
        self.invulnerable = False
        self.invulnerable_start_time = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, TANK_WIDTH, TANK_HEIGHT))

    def move(self, dx, dy):
        self.x += dx * TANK_SPEED
        self.y += dy * TANK_SPEED

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > BULLET_COOLDOWN and self.bullets > 0:
            self.bullets -= 1
            self.last_shot = current_time
            return Bullet(self.x + TANK_WIDTH // 2, self.y + TANK_HEIGHT // 2)
        return None

    def recharge(self):
        current_time = pygame.time.get_ticks()
        if self.bullets < 5 and current_time - self.last_shot > BULLET_COOLDOWN:
            self.bullets += 1
            self.last_shot = current_time

    def take_damage(self, damage):
        if not self.invulnerable:
            if self.shield:
                self.shield = False
            else:
                self.hp -= damage

    def activate_shield(self):
        self.shield = True

    def activate_invulnerability(self):
        self.invulnerable = True
        self.invulnerable_start_time = pygame.time.get_ticks()

    def update_invulnerability(self):
        if self.invulnerable and pygame.time.get_ticks() - self.invulnerable_start_time > 10000:
            self.invulnerable = False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, TANK_WIDTH, TANK_HEIGHT)

# Класс пули
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.color = RED

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self, dx, dy):
        self.x += dx * BULLET_SPEED
        self.y += dy * BULLET_SPEED

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

# Класс бонуса
class Bonus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(BONUS_TYPES)
        self.color = GREEN if self.type == "shield" else BLUE if self.type == "invulnerability" else RED

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, BONUS_SIZE, BONUS_SIZE))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BONUS_SIZE, BONUS_SIZE)

# Класс противника
class EnemyTank(Tank):
    def __init__(self, x, y, color, target):
        super().__init__(x, y, color)
        self.target = target  # Цель (игрок)
        self.move_timer = pygame.time.get_ticks()
        self.shoot_timer = pygame.time.get_ticks()

    def update(self):
        # Движение к цели
        current_time = pygame.time.get_ticks()
        if current_time - self.move_timer > 1000:  # Обновляем направление каждую секунду
            self.move_timer = current_time
            dx = self.target.x - self.x
            dy = self.target.y - self.y
            distance = math.hypot(dx, dy)
            if distance != 0:
                dx /= distance
                dy /= distance
            self.move(dx, dy)

        # Стрельба в цель
        if current_time - self.shoot_timer > 2000:  # Стреляем каждые 2 секунды
            self.shoot_timer = current_time
            return self.shoot()
        return None

# Основная функция игры
def main():
    run = True
    clock = pygame.time.Clock()

    # Создание танков
    tank1 = Tank(100, 100, RED)
    enemies = [EnemyTank(random.randint(0, WIDTH - TANK_WIDTH), random.randint(0, HEIGHT - TANK_HEIGHT), YELLOW, tank1) for _ in range(3)]  # 3 противника

    bullets = []
    enemy_bullets = []
    bonuses = []

    # Создание бонусов
    for _ in range(5):
        bonuses.append(Bonus(random.randint(0, WIDTH - BONUS_SIZE), random.randint(0, HEIGHT - BONUS_SIZE)))

    while run:
        clock.tick(60)
        WIN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Управление танком игрока
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            tank1.move(0, -1)
        if keys[pygame.K_s]:
            tank1.move(0, 1)
        if keys[pygame.K_a]:
            tank1.move(-1, 0)
        if keys[pygame.K_d]:
            tank1.move(1, 0)
        if keys[pygame.K_SPACE]:
            bullet = tank1.shoot()
            if bullet:
                bullets.append(bullet)

        # Обновление противников
        for enemy in enemies:
            enemy_bullet = enemy.update()
            if enemy_bullet:
                enemy_bullets.append(enemy_bullet)

        # Обновление пуль игрока
        for bullet in bullets[:]:
            bullet.move(0, -1)
            bullet.draw(WIN)
            # Проверка столкновений пуль игрока с противниками
            for enemy in enemies[:]:
                if bullet.get_rect().colliderect(enemy.get_rect()):
                    enemy.take_damage(1)
                    if enemy.hp <= 0:
                        enemies.remove(enemy)
                    if bullet in bullets:
                        bullets.remove(bullet)
                    break

        # Обновление пуль противников
        for bullet in enemy_bullets[:]:
            bullet.move(0, -1)
            bullet.draw(WIN)
            # Проверка столкновений пуль противников с игроком
            if bullet.get_rect().colliderect(tank1.get_rect()):
                tank1.take_damage(1)
                if bullet in enemy_bullets:
                    enemy_bullets.remove(bullet)

        # Обновление танков
        tank1.draw(WIN)
        for enemy in enemies:
            enemy.draw(WIN)

        # Обновление бонусов
        for bonus in bonuses[:]:
            bonus.draw(WIN)
            # Проверка столкновений с бонусами
            if tank1.get_rect().colliderect(bonus.get_rect()):
                if bonus.type == "shield":
                    tank1.activate_shield()
                elif bonus.type == "invulnerability":
                    tank1.activate_invulnerability()
                bonuses.remove(bonus)

        # Обновление неуязвимости
        tank1.update_invulnerability()

        # Перезарядка пуль
        tank1.recharge()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()