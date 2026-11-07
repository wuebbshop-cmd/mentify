import sympy as sp

x = sp.symbols("x", positive=True)


def check(name, y, expr, order=8):
    res = sp.simplify(sp.expand(expr.subs(sp.Symbol("y"), y)))
    ser = sp.series(res, x, 0, order).removeO()
    ser = sp.expand(ser)
    poly = sp.Poly(sp.expand(ser * x ** 6), x) if False else None
    terms = sp.Add.make_args(ser)
    return name, sp.simplify(ser)


# E1: y' - 2xy = 0 with c0 = 1
c = [sp.Integer(1)]
N = 9
for n in range(0, N):
    # (n+1)c[n+1] = 2 c[n-1]
    c.append(sp.Rational(2) * (c[n - 1] if n - 1 >= 0 else 0) / (n + 1))
y1 = sum(c[n] * x ** n for n in range(N + 1))
print("E1", sp.series(y1.diff(x) - 2 * x * y1, x, 0, 8))

# E3: (x^2-1)y'' + 3x y' + x y
C = [sp.Integer(1), sp.Integer(0)] + [0] * 9  # c0=1, c1=0
for r in range(1, 9):
    C[r + 2] = sp.Rational(r * (r + 2) * C[r] + C[r - 1], (r + 1) * (r + 2))
print("E3 coeffs c0..c8:", [sp.nsimplify(C[n]) for n in range(9)])
y3 = sum(C[n] * x ** n for n in range(9))
print("E3", sp.series(sp.expand((x ** 2 - 1) * y3.diff(x, 2) + 3 * x * y3.diff(x) + x * y3), x, 0, 8))

# E3 second family c0=0, c1=1
D = [sp.Integer(0), sp.Integer(1)] + [0] * 9
for r in range(1, 9):
    D[r + 2] = sp.Rational(r * (r + 2) * D[r] + D[r - 1], (r + 1) * (r + 2))
print("E3b coeffs:", [sp.nsimplify(D[n]) for n in range(9)])
y3b = sum(D[n] * x ** n for n in range(9))
print("E3b", sp.series(sp.expand((x ** 2 - 1) * y3b.diff(x, 2) + 3 * x * y3b.diff(x) + x * y3b), x, 0, 8))

# E4: y'' - x y = 0 (Airy)
A = [0] * 10
A[0], A[1] = 1, 0
A[2] = 0
for m in range(1, 8):
    A[m + 2] = sp.Rational(A[m - 1], (m + 1) * (m + 2))
A[2] = 0
print("Airy even:", A)
y4 = sum(A[n] * x ** n for n in range(9))
print("E4", sp.series(sp.expand(y4.diff(x, 2) - x * y4), x, 0, 8))

B = [0] * 10
B[0], B[1] = 0, 1
for m in range(1, 8):
    B[m + 2] = sp.Rational(B[m - 1], (m + 1) * (m + 2))
B[2] = 0
y4b = sum(B[n] * x ** n for n in range(9))
print("Airy odd:", B)
print("E4b", sp.series(sp.expand(y4b.diff(x, 2) - x * y4b), x, 0, 8))

# E5: 2x^2 y'' - x y' + (1-x^2) y = 0, Frobenius
for rr in [sp.Integer(1), sp.Rational(1, 2)]:
    co = [sp.Integer(1), 0]
    for n in range(2, 9):
        co.append(sp.simplify(co[n - 2] / ((2 * (n + rr) - 1) * (n + rr - 1))))
    y = sum(co[n] * x ** (n + rr) for n in range(len(co)))
    print("E5 r=", rr, [sp.nsimplify(co[n]) for n in range(len(co))])
    print("E5 res", sp.series(sp.expand(2 * x ** 2 * y.diff(x, 2) - x * y.diff(x) + (1 - x ** 2) * y), x, 0, 6))

# E6: x^2 y'' + 3x y' + (1-x) y = 0, double root -1
co = []
for n in range(9):
    # c_n = c_{n-1}/n^2 for r=-1
    co.append(sp.Rational(1, sp.factorial(n) ** 2))
y6 = sum(co[n] * x ** (n - 1) for n in range(9))
print("E6", sp.series(sp.expand(x ** 2 * y6.diff(x, 2) + 3 * x * y6.diff(x) + (1 - x) * y6), x, 0, 6))
# y2 = y1 ln x - 2 x^-1 sum H_n x^n/(n!)^2
H = sp.Integer(0)
tail = 0
for n in range(1, 9):
    H = H + sp.Rational(1, n)
    tail = tail + H * x ** n / sp.factorial(n) ** 2
y6b = y6 * sp.log(x) - 2 * tail / x
print("E6 log resid", sp.series(sp.expand(x ** 2 * y6b.diff(x, 2) + 3 * x * y6b.diff(x) + (1 - x) * y6b), x, 0, 6))

# E7: x^2 y'' - 2x y' + (2-x) y = 0 roots 2 and 1
co = [sp.Integer(1)]
for n in range(1, 9):
    co.append(sp.simplify(co[n - 1] / (n * (n + 1))))
y7 = sum(co[n] * x ** (n + 2) for n in range(len(co)))
print("E7 r=2 coeffs", [sp.nsimplify(v) for v in co])
print("E7", sp.series(sp.expand(x ** 2 * y7.diff(x, 2) - 2 * x * y7.diff(x) + (2 - x) * y7), x, 0, 6))

# E8: y'' - y = x
c0 = sp.Integer(1)
co = [c0, sp.Integer(0), c0 / 2]
co.append(sp.Rational(1, 6))
for m in range(2, 9):
    co.append(co[m] / ((m + 1) * (m + 2)))
y8 = sum(co[n] * x ** n for n in range(9))
print("E8 coeffs", co)
print("E8", sp.series(sp.expand(y8.diff(x, 2) - y8 - x), x, 0, 7))

# E9: y'' + y = x
co = [sp.Integer(1), sp.Integer(0)]
co.append(-co[0] / 2)
co.append(sp.Rational(1, 6))
for m in range(2, 9):
    co.append(-co[m] / ((m + 1) * (m + 2)))
y9 = sum(co[n] * x ** n for n in range(9))
print("E9 coeffs", co)
print("E9", sp.series(sp.expand(y9.diff(x, 2) + y9 - x), x, 0, 7))
