from pytest import approx, raises
from calc import Calc


class TestCalc:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.c = Calc()

    def test_raises1(self):
        with raises(Exception):
            self.c.compile('a')

    # числа без 0o
    def test_raises2(self):
        with raises(Exception):
            self.c.compile('01546-345')

    # одно число без 0o
    def test_raises3(self):
        with raises(Exception):
            self.c.compile('0o+0o4')
    def test_raises4(self):
        with raises(Exception):
            self.c.compile('0o9+0o9')

    # Тесты на сложение
    def test_addition1(self):
        assert self.c.compile('0o45+0o1001') == 550

    def test_addition2(self):
        assert self.c.compile('0o34+0o23+0o56+0o1') == 94

    def test_addition3(self):
        assert self.c.compile('(0o22+0o23)+(0o1+0o67)') == 93

    def test_addition4(self):
        assert self.c.compile('(0o1255+(0o42+0o5)+0o617)') == 1123

    # Тесты на вычитание
    def test_subtraction1(self):
        assert self.c.compile('0o1211-0o32') == 623

    def test_subtraction2(self):
        assert self.c.compile('0o3755-0o46702') == -17877

    def test_subtraction3(self):
        assert self.c.compile('0o161-0o222-0o36-0o44-0o5-0o6') == -40

    def test_subtraction4(self):
        assert self.c.compile('(0o121-0o2132)-(0o343-0o57)') == -1213

    # Тесты на умножение
    def test_multiplication1(self):
        assert self.c.compile('0o1*0o52') == 42

    def test_multiplication2(self):
        assert self.c.compile('0o0*0o0') == 0

    def test_multiplication3(self):
        assert self.c.compile('0o747*0o1*0o1*0o1123') == 289765

    def test_multiplication4(self):
        assert self.c.compile('0o2*0o5*0o312') == 2020

    # Тесты на деление
    def test_division1(self):
        assert self.c.compile('0o1/0o2') == approx(0.5)

    def test_division2(self):
        assert self.c.compile('0o2/0o1') == approx(2.0)

    def test_division3(self):
        assert self.c.compile('0o0/0o234') == approx(0.0)

    def test_division4(self):
        assert self.c.compile('0o777/0o6/0o3/0o2') == approx(127.75)

    # деление на 0
    def test_division5(self):
        with raises(ZeroDivisionError):
            self.c.compile('0o123/0o0')

    # Тесты на сложные арифметические выражения
    def test_expressions1(self):
        assert self.c.compile('(0o1-0o2)') == -1

    def test_expressions2(self):
        assert self.c.compile('(0o1+0o2)*0o11') == 27

    def test_expressions3(self):
        assert self.c.compile('0o7*(0o1450)/0o4*0o3') == approx(471.333333)

    def test_expressions4(self):
        test = '0o31+0o3*0o33-0o2+(0o2*(0o3+0o7-0o67))/(0o5/0o1*0o10/0o3)'
        assert self.c.compile(test) == approx(152.0)

    def test_expressions5(self):
        test = '(0o33-0o5*0o3(0o1+0o1))*(0o2*0o5+0o13+0o4*' \
               '(0o55*0o2/0o3))-(0o7466+0o4+0o72/0o16)/(0o1+0o65/0o3*0o22)+0o444'
        assert self.c.compile(test) == approx(-2402.305740987984)
