# f(x) = sin(x)^2 - cos(x)^2

# Определить корни

# Найти интервалы, на которых функция возрастает

# Найти интервалы, на которых функция убывает

# Построить график

# Вычислить вершину

# Определить промежутки, на котором f > 0

# Определить промежутки, на котором f < 0

from sympy import symbols, sin, cos, Symbol, solveset, diff, pprint, S
from sympy.plotting import plot
x = Symbol('x')
# Построить график
f = sin(x)**2 - cos(x)**2
func = plot(f , show=False)
func.show()

# Определить корни
ans = solve(f,x)
print(ans)
for i in ans:
    print(i.evalf())

# Найти интервалы, на которых функция возрастает
pprint(solveset(eq_diff > 0, x,domain= S.Reals), use_unicode=True)

# Найти интервалы, на которых функция убывает
pprint(solveset(eq_diff < 0, x,domain= S.Reals), use_unicode=True)

# Вычислить вершину
pprint(solveset(eq_diff, x,domain= S.Reals ), use_unicode=True)

# Определить промежутки, на котором f > 0
pprint(solveset(f > 0, x,domain= S.Reals ), use_unicode=True)

# Определить промежутки, на котором f < 0
pprint(solveset(f < 0, x,domain= S.Reals ), use_unicode=True)