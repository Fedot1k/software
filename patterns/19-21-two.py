from functools import lru_cache
import math

def moves(s):
    a, b = s
    return (a+2, b), (a*2, b), (a, b+2), (a, b*2) # возможные действия

@lru_cache(None)

def game(s):
    a, b = s

    if a + b >= 100: return 'w' # число необходимое для победы
    if any(game(m) == 'w' for m in moves(s)): return 'p1'
    if any(game(m) == 'p1' for m in moves(s)): return 'b1' # <all> для нормальной игры, <any> для для плохой игры
    if any(game(m) == 'b1' for m in moves(s)): return 'p2'
    if all(game(m) == 'p1' or game(m) == 'p2' for m in moves(s)): return 'b2'


for s_ in range(1, 81):
    s = 9, s_ # две кучи камней, s - камней в первой, s_ - камней во второй
    if game(s) == 'b1': # b - Ваня, p - Петя, 1 - первый ход, 2 - второй ход
        print(s)