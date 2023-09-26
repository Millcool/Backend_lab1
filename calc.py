#!/usr/bin/env python3

import re
from operator import add, sub, mul, truediv
from stack import Stack
from compf import Compf


class Calc(Compf):
    """
    Интерпретатор арифметических выражений вычисляет значения
    правильных арифметических формул, в которых в качестве
    операндов допустимы только цифры [0-7]
    """

    SYMBOLS = re.compile("[0-7]")

    def __init__(self):
        # Инициализация (конструктор) класса Compf
        super().__init__()
        # Создание стека чисел для работы стекового калькулятора
        self.r = Stack()

    # Интерпретация арифметического выражения
    def compile(self, str):
        Compf.compile(self, str)
        return self.r.top()

    # Обработка цифры
    def process_value(self, c):
        if self.pref__len == 0 or self.pref__len == 1:
            self.pref__len += 1
        else:
            self.val += c

    # Обработка символа операции
    def process_oper(self, c):
        second, first = self.r.pop(), self.r.pop()
        self.r.push({"+": add, "-": sub, "*": mul,
                     "/": truediv}[c](first, second))

    def try_add_value(self,c):
        if len(self.val) > 0:
            self.r.push(int(self.val, 8))
            self.val = ""
            self.pref__len = 0
            # Просим пользователя ввести число в формате 0O/0o
        elif self.pref__len > 0 and len(self.val) == 0:
            raise Exception("Пожалуйста введите число в формате 0o____")

    def check_symbol(self, c):
        if self.pref__len == 0 and c != "0":
            raise Exception(f"Недопустимый символ '{c}': "
                            f"Число в восьмеричной системе должно начинаться с 0o или 0O")
        if self.pref__len == 1 and c not in "oO":
            raise Exception(f"Недопустимый символ '{c}': "
                            f"Число в восьмеричной системе должно начинаться с 0o или 0O")
        if self.pref__len > 1 and not self.SYMBOLS.match(c):
            raise Exception(f"Недопустимый символ '{c}'")


if __name__ == "__main__":
    c = Calc()
    while True:
        str = input("Арифметическое выражение: ")
        print(f"Результат его вычисления: {c.compile(str)}")
        print()
