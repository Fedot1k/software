from functools import lru_cache


def move(s):
    return [x for x in [s + 1, s * 3] if x <= 80]  # возможные действия, верхнее ограничение = не передавать


@lru_cache(None)
def game(s):
    if s >= 56:  # Число необходимое для победы
        return 'w'
    if any(game(m) == 'w' for m in move(s)):
        return 'p1'
    if all(game(m) == 'p1' for m in move(s)):  # <all> для нормальной игры, <any> для плохой игры
        return 'b1'
    if any(game(m) == 'b1' for m in move(s)):
        return 'p2'
    if all(game(m) in ['p1', 'p2'] for m in move(s)):  # 3 хода = <['p1', 'p2', 'p3']>
        return 'b2'


for s in range(1, 56):  # Количество камней в куче
    if game(s) == 'b1':  # b - Ваня, p - Петя, 1 - первый ход, 2 - второй ход
        print(s, game(s))
