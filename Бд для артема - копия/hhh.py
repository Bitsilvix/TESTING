import pygame
import os
import random
import math
import time
import sqlite3

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World of Tanks Nintendo Switch edition")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CANYON = (139, 69, 19)  # Коричневый цвет для препятствий
DARK_GRAY = (50, 50, 50)  # Темно-серый для Underground_Storage
LIGHT_GRAY = (180, 180, 180)  # Светло-серый для Castle_Lawn
FOUNTAIN_COLOR = (200, 200, 200)  # Цвет фонтана/статуи

# Настройки танка
TANK_WIDTH, TANK_HEIGHT = 40, 40
TANK_SPEED = 2
BULLET_SPEED = 5
BULLET_COOLDOWN = 2000

# Настройки бонусов
BONUS_SIZE = 20
BONUS_TYPES = ["explosive_bullet", "shield", "invulnerability"]

# Настройки препятствий
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 80, 80

# Загрузка изображений
def load_image(path, width, height):
    if not os.path.exists(path):
        # Если файл не найден, создаем заглушку
        surf = pygame.Surface((width, height))
        surf.fill(RED)
        return surf
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (width, height))
    return image

# Запрос цвета танка
def get_player_color():  # Добавляем функцию для выбора цвета танка
    pygame.display.set_caption("Введите цвет танка (например, 'green', 'blue', 'red')")
    color = ""
    font = pygame.font.SysFont("Arial", 40)
    input_active = True
    
    while input_active:
        WIN.fill(WHITE)
        text_surface = font.render("Введите цвет танка:", True, BLACK)
        color_surface = font.render(color, True, BLACK)
        
        WIN.blit(text_surface, (WIDTH//2 - text_surface.get_width()//2, HEIGHT//2 - 50))
        WIN.blit(color_surface, (WIDTH//2 - color_surface.get_width()//2, HEIGHT//2 + 10))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    color = color[:-1]
                else:
                    color += event.unicode
    
    pygame.display.set_caption("World of Tanks Nintendo Switch edition")
    return color if color else "green"  # Установка цвета по умолчанию

# Загрузка изображений танка
def load_tank_image():
    return load_image(os.path.join("Sprites", "tank.png"), TANK_WIDTH, TANK_HEIGHT)

# Загрузка изображений врагов
def load_enemy_images():
    return [load_image(os.path.join("Sprites", f"bot.png"), TANK_WIDTH, TANK_HEIGHT) for i in range(1, 4)]

# Загрузка фонового изображения
def load_background(map_name):
    if map_name == "map1":
        return load_image(os.path.join("Sprites", "Underground_Storage.jpg"), WIDTH, HEIGHT)
    elif map_name == "map2":
        return load_image(os.path.join("Sprites", "Castle_Lawn.jpg"), WIDTH, HEIGHT)
    elif map_name == "map3":
        return load_image(os.path.join("Sprites", "Besieged_City.jpg"), WIDTH, HEIGHT)
    else:
        return load_image(os.path.join("Sprites", "background.jpg"), WIDTH, HEIGHT)

# Функция для ввода имени игрока
def get_player_name():
    pygame.display.set_caption("Введите ваше имя")
    name = ""
    font = pygame.font.SysFont("Arial", 40)
    input_active = True
    
    while input_active:
        WIN.fill(WHITE)
        text_surface = font.render("Введите ваше имя:", True, BLACK)
        name_surface = font.render(name, True, BLACK)
        
        WIN.blit(text_surface, (WIDTH//2 - text_surface.get_width()//2, HEIGHT//2 - 50))
        WIN.blit(name_surface, (WIDTH//2 - name_surface.get_width()//2, HEIGHT//2 + 10))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
    
    pygame.display.set_caption("World of Tanks Nintendo Switch edition")
    return name

# Функция для отображения результатов и сохранения в БД
def show_results(win, time_elapsed, bonuses_collected, score, victory, player_name, map_name, tank_color): # Добавили tank_color в параметры
    # Подключение к базе данных
    con = sqlite3.connect("tanks.db")
    cur = con.cursor()
    
    # Сохранение результатов в БД
    try:
        player_id = cur.execute(
            f"SELECT id_player FROM players WHERE name = '{player_name}' AND color_tank = '{tank_color}'"
        ).fetchone()

        if not player_id:
            # Добавляем нового игрока, включая цвет танка
            cur.execute(f"""
                INSERT INTO players
                (name, color_tank)
                VALUES
                ('{player_name}', '{tank_color}')
            """)
            con.commit()
            
            player_id = cur.execute(
                f"SELECT id_player FROM players WHERE name = '{player_name}' AND color_tank = '{tank_color}'"
            ).fetchone()

        # Получаем id уровня
        level_id = cur.execute(f"SELECT id_level FROM levels WHERE name = '{map_name}'").fetchone()
        
        # Сохранение результатов
        cur.execute(f"""
            INSERT INTO result
            (id_player, id_level, time_life, result)
            VALUES
            ({player_id[0]}, {level_id[0]}, {time_elapsed}, {score})
        """)
        con.commit()
        
        # Вывод статистики
        result_text = "Статистика:\n"
        results = cur.execute("SELECT player.name, levels.name, result.time_life, result.result FROM result JOIN players ON result.id_player = players.id_player JOIN levels ON result.id_level = levels.id_level").fetchall()
        for res in results:
            result_text += f"{res[0]} - {res[1]}: {res[2]} сек, {res[3]} очков\n"

        print(result_text)  # Здесь просто выводим, можно изменить на текст в окне

    except Exception as e:
        print(e)
    finally:
        con.close()

# Основная функция игры
def main():
    # Получаем имя и цвет игрока
    player_name = get_player_name()  # Сначала получаем имя
    if not player_name:
        return
    tank_color = get_player_color()  # Затем получаем цвет

    # Титульный экран
    selected_map = title_screen()
    if not selected_map:
        return

    run = True
    clock = pygame.time.Clock()

    # Загрузка изображений
    enemy_images = load_enemy_images()
    background = load_background(selected_map)

    # Создание препятствий для выбранной карты
    obstacles = create_obstacles(selected_map)

    # Определяем количество врагов в зависимости от карты
    if selected_map == "map1":
        num_enemies = 3
    elif selected_map == "map2":
        num_enemies = 4
    elif selected_map == "map3":
        num_enemies = 6

    # Получаем позиции спавна
    player_spawn, enemy_spawns = get_spawn_positions(selected_map, obstacles, num_enemies)

    # Создание танков
    tank1 = Tank(*player_spawn, tank_color)  # Здесь нужно передать цвет танка в класс
    enemies = [
        EnemyTank(*enemy_spawns[i], tank1, enemy_images[i % len(enemy_images)])
        for i in range(num_enemies)
    ]

    bullets = []
    enemy_bullets = []
    bonuses = []

    # Создание бонусов
    for _ in range(5):
        valid_position = False
        while not valid_position:
            x = random.randint(0, WIDTH - BONUS_SIZE)
            y = random.randint(0, HEIGHT - BONUS_SIZE)
            if is_position_valid(x, y, obstacles, BONUS_SIZE):
                valid_position = True
        bonuses.append(Bonus(x, y))

    # Время начала игры
    start_time = time.time()
    bonuses_collected = 0
    score = 0

    while run:
        clock.tick(60)
        WIN.blit(background, (0, 0))  # Отрисовка фона

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    confirm_exit()  # Вызов функции подтверждения выхода
        # (продолжение кода...)


# Функция для подтверждения выхода
def confirm_exit():
    # Здесь реализация подтверждения, например, показываем диалог
    WIN.fill(WHITE)
    font = pygame.font.SysFont("Arial", 40)
    text_surface = font.render("Вы действительно хотите выйти? (Y/N)", True, BLACK)
    WIN.blit(text_surface, (WIDTH//2 - text_surface.get_width()//2, HEIGHT//2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    pygame.quit()
                    exit()  # Завершить игру
                if event.key == pygame.K_n:
                    waiting = False  # Вернуться в игру

# Функция для отображения активного бонуса
def display_bonus_effect(effect_name):
    font = pygame.font.SysFont("Arial", 30)
    effect_surface = font.render(f"Активен эффект: {effect_name}", True, BLACK)
    WIN.blit(effect_surface, (WIDTH // 2 - effect_surface.get_width() // 2, 10))

# (Остальные классы и функции, такие как Tank, Bullet, Bonus и другие...)
