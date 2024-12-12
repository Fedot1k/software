from functools import lru_cache

def moves(s):
    return s + 1, s + 2, s * 3  # возможные действия

@lru_cache(None)

def game(s):
    if s >= 65: return 'w' # число необходимое для победы
    if any(game(m) == 'w' for m in moves(s)): return 'p1'
    if all(game(m) == 'p1' for m in moves(s)): return 'b1' # <all> для нормальной игры, <any> для для плохой игры
    if any(game(m) == 'b1' for m in moves(s)): return 'p2'
    if all(game(m) == 'p1' or game(m) == 'p2' for m in moves(s)): return 'b2'

for s in range(1, 65): # количество камней в куче
    if game(s) == 'b2': # b - Ваня, p - Петя, 1 - первый ход, 2 - второй ход
        print(s, game(s))