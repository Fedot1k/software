from functools import lru_cache

def move(s):
    a, b = s
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2) # возможные действия, верхнее ограничение = не передавать

@lru_cache(None)

def game(s):
    if sum(s) >= 77: return 'w' # число необходимое для победы
    if any(game(m) == 'w' for m in move(s)): return 'p1'
    if all(game(m) == 'p1' for m in move(s)): return 'b1' # <all> для нормальной игры, <any> для плохой игры
    if any(game(m) == 'b1' for m in move(s)): return 'p2'
    if all(game(m) in ['p1', 'p2'] for m in move(s)): return 'b2'


for s_ in range(1, 77):
    s = 13, s_ # две кучи камней, s - камней в первой, s_ - камней во второй
    if game(s) == 'b2': # b - Ваня, p - Петя, 1 - первый ход, 2 - второй ход
        print(list(s), game(s))