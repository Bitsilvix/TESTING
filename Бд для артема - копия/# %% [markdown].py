# %% [markdown]
# ПОДКЛЮЧЕНИЕ К БД

# %%
import sqlite3
con = sqlite3.connect("tanks.db")
cur = con.cursor()

# %% [markdown]
# СМОТРЕТЬ ДАННЫЕ

# %%
players = cur.execute("SELECT * FROM players")
players.fetchall()

# %%
levels = cur.execute("SELECT * FROM levels")
levels.fetchall()

# %%
res = cur.execute("SELECT * FROM result")
res.fetchall()

# %% [markdown]
# ВСТАВКА ДАННЫХ

# %%
name_player = 'anton2'
color = 'black'

cur.execute(f"""
 INSERT INTO players
 (name, color_tank)
  VALUES
 ('{name_player}', '{color}')
""")
con.commit()

# %%
name_level = 'Castle_Lawn'
col_enemies = 5
col_blocks = 15

cur.execute(f"""
 INSERT INTO levels
 (name_level, col_enemies, col_blocks)
  VALUES
 ('{name_level}', '{col_enemies}', '{col_blocks}')
""")
con.commit()

# %%
name_level = 'Castle_Lawn'
name_player = "artem23123"
time = 1243452
result = 100

levels = cur.execute(
    f"""SELECT id_level FROM levels
    where name_level = '{name_level}' """)
id_level = levels.fetchall()[0][0]

players = cur.execute(
    f"""SELECT id_player FROM players
    where name = '{name_player}'""")
id_player = players.fetchall()[0][0]

cur.execute(f"""
 INSERT INTO result
 (id_player, id_level, time_life, result)
  VALUES
 ('{id_player}'
 , '{id_level}'
 , '{time}', '{result}')
""")
con.commit()

# %% [markdown]
# ВЫВОД ЗНАЧЕНИЙ ОТДЕЛЬНО

# %%
all_res = cur.execute("""
SELECT * FROM 
    result as r
INNER JOIN players as p
ON r.id_player = p.id_player
INNER JOIN levels as l
ON r.id_level = l.id_level
""")
all_res = all_res.fetchall()
all_res

# %%
for row in all_res:
    print(row[2], row[3], row[5], row[6], row[8], row[9])

# %% [markdown]
# Отключить соедеинение от БД

# %%
con.close()


