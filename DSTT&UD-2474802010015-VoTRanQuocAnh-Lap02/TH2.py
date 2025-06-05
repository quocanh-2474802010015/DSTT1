from sympy import symbols, Eq, solve, Matrix

# Problem 1: Hệ 2 phương trình 2 ẩn
x, y = symbols('x y')
eq1 = Eq(x - y, -2)
eq2 = Eq(2*x + 3*y, 6)
sol1 = solve((eq1, eq2), (x, y))
print("Problem 1 - Point of intersection:", sol1)

# Problem 2: Hệ 3 phương trình 3 ẩn
x, y, z = symbols('x y z')
eq3 = Eq(x - y, 2)
eq4 = Eq(2*x - y - z, 3)
eq5 = Eq(x + y + z, 6)
sol2 = solve((eq3, eq4, eq5), (x, y, z))
print("Problem 2 - Point of intersection:", sol2)

# Problem 3: Tìm hệ số đa thức bậc 2 p(x) = ax^2 + bx + c
a, b, c = symbols('a b c')
eq6 = Eq(a + b + c, 4)
eq7 = Eq(4*a + 2*b + c, 3)
eq8 = Eq(9*a + 3*b + c, 4)
sol3 = solve((eq6, eq7, eq8), (a, b, c))
print("Problem 3 - Polynomial coefficients:", sol3)

# Problem 4: Phân tích đa thức để tích phân
a, b, c = symbols('a b c')
eq9 = Eq(a + c, 1)
eq10 = Eq(a + b - 2*c, -3)
eq11 = Eq(-2*a + 2*b + c, 0)
sol4 = solve((eq9, eq10, eq11), (a, b, c))
print("Problem 4 - Coefficients in decomposition:", sol4)
