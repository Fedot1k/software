from functools import lru_cache
import math

def moves(s):
    return (s + 1, s * 3) if s * 3 <= 80 else ((s + 1, ) if s + 1 <= 80 else ()) # возможные действия, верхнее ограничение = не передавать

@lru_cache(None)
def game(s):
    if s >= 56: return 'w'  # Число необходимое для победы
    if any(game(m) == 'w' for m in moves(s)): return 'p1'
    if all(game(m) == 'p1' for m in moves(s)): return 'b1'
    if any(game(m) == 'b1' for m in moves(s)): return 'p2'
    if all(game(m) == 'p1' or game(m) == 'p2' for m in moves(s)): return 'b2'

for s in range(1, 56):  # Количество камней в куче
    if game(s) == 'b1':  # b - Ваня, p - Петя, 1 - первый ход, 2 - второй ход
        print(s, game(s))
