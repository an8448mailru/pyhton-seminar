# Модуль для выполнения операций
import sympy

def execute_expr(expr: str) -> str:
    """Возвращает результат примера"""
    return str(eval(expr))

def solve_eq(expr: str) -> str:
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителями"""
    try:
        x = sympy.Simbol('x')
        res = sympy.solve(expr, x)
        res = list(map(str, res))
        return " || ".join(res)
    except ValueError:
        return 'Incorrect input'

def simplify_pol(expr: str) -> str:
    """Упрощает многочлен"""
    return str(sympy.simplify(expr))