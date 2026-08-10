# lines.py
import sys
import random
import argparse
from datetime import datetime

class LinesPuzzle:
    def __init__(self, size=6, seed=None):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.pairs = []
        self.solution = None
        if seed is not None:
            random.seed(seed)

    def generate(self):
        # Простой генератор: создаём несколько горизонтальных и вертикальных линий
        # Для демонстрации используем предопределённую головоломку
        # В реальной реализации используется алгоритм с возвратом
        # Здесь упрощённо: фиксированные пары для размера 6
        if self.size == 6:
            self.pairs = [
                ((0,0), (5,5)), ((0,1), (4,3)), ((1,0), (3,4)),
                ((2,2), (4,4)), ((3,1), (5,3)), ((0,5), (5,0))
            ]
        else:
            # Для других размеров генерируем случайные пары (не гарантируем решение)
            self.pairs = []
            for i in range(self.size // 2):
                start = (random.randint(0,self.size-1), random.randint(0,self.size-1))
                end = (random.randint(0,self.size-1), random.randint(0,self.size-1))
                self.pairs.append((start, end))
        self.solution = self.solve()  # заглушка

    def solve(self):
        # Заглушка: возвращает решение (в реальности строится)
        return None

    def display(self, show_solution=False):
        # Вывод поля
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print('  ' + ' '.join(str(i+1) for i in range(self.size)))
        for r in range(self.size):
            row = letters[r] + ' '
            for c in range(self.size):
                # Определяем, есть ли пара в этой клетке
                found = False
                for idx, (start, end) in enumerate(self.pairs):
                    if (r,c) == start or (r,c) == end:
                        row += str(idx+1) + ' '
                        found = True
                        break
                if not found:
                    row += '. '
            print(row)

def main():
    parser = argparse.ArgumentParser(description='Головоломка "Линии"')
    parser.add_argument('--size', type=int, default=6, help='Размер поля (по умолчанию 6)')
    parser.add_argument('--show-solution', action='store_true', help='Показать решение')
    parser.add_argument('--date', help='Дата для ежедневного задания (ГГГГ-ММ-ДД)')
    args = parser.parse_args()

    seed = None
    if args.date:
        seed = hash(args.date) & 0xFFFFFFFF
    else:
        seed = datetime.now().toordinal()  # день года

    puzzle = LinesPuzzle(args.size, seed)
    puzzle.generate()
    puzzle.display(args.show_solution)

if __name__ == '__main__':
    main()
