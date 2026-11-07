import sympy as sp

x = sp.symbols("x", positive=True)
N = 18

# x^2 y'' - 2x y' + (2-x) y = 0, roots 2 and 1
c = [0] * (N + 1)
c[0] = 1
for n in range(1, N + 1):
    c[n] = sp.nsimplify(c[n - 1] / (n * (n + 1)))
y1 = sum(c[n] * x ** (n + 2) for n in range(N + 1))
u = sp.series(y1 / x ** 2, x, 0, 12).removeO()
g = sp.series(1 / u ** 2, x, 0, 12).removeO()
integrand = sp.expand(g * x ** -2)
poly = sp.Poly(sp.expand(integrand * x ** 3), x)
I = sp.Integer(0)
for (k,), a in poly.terms():
    power = k - 3
    if power == -1:
        I += a * sp.log(x)
    else:
        I += a * x ** (power + 1) / (power + 1)
y2 = sp.expand(y1 * I)
print("y1 =", sp.series(y1, x, 0, 8))
print("y2 =", sp.series(y2, x, 0, 8))
res = sp.expand(x ** 2 * y2.diff(x, 2) - 2 * x * y2.diff(x) + (2 - x) * y2)
print("resid:", sp.series(res, x, 0, 2))

# Bessel-type case 3: x^2 y'' + x y' + (x^2-1) y = 0
c = [0] * (N + 1)
c[0] = 1
for n in range(2, N + 1, 2):
    c[n] = sp.nsimplify(-c[n - 2] / ((n + 1) ** 2 - 1))
yb = sum(c[n] * x ** (n + 1) for n in range(N + 1))
print("y1b =", sp.series(yb, x, 0, 10))
u = sp.series(yb / x, x, 0, 10).removeO()
g = sp.series(1 / u ** 2, x, 0, 10).removeO()
integrand = sp.expand(g * x ** -3)
poly = sp.Poly(sp.expand(integrand * x ** 5), x)
I = sp.Integer(0)
for (k,), a in poly.terms():
    power = k - 5
    if power == -1:
        I += a * sp.log(x)
    else:
        I += a * x ** (power + 1) / (power + 1)
y2b = sp.expand(yb * I)
print("y2b =", sp.series(y2b, x, 0, 8))
resb = sp.expand(x ** 2 * y2b.diff(x, 2) + x * y2b.diff(x) + (x ** 2 - 1) * y2b)
print("residb:", sp.series(resb, x, 0, 2))

# equal roots example x^2 y'' + 3x y' + (1-x) y = 0
co = [sp.Rational(1, sp.factorial(n) ** 2) for n in range(12)]
yq = sum(co[n] * x ** (n - 1) for n in range(12))
H = sp.Integer(0)
tail = 0
for n in range(1, 12):
    H = H + sp.Rational(1, n)
    tail = tail + H * x ** n / sp.factorial(n) ** 2
y2q = sp.expand(yq * sp.log(x) - 2 * tail / x)
print("y1q =", sp.series(yq, x, 0, 6))
print("y2q =", sp.series(y2q, x, 0, 5))
print("residq:", sp.series(sp.expand(x ** 2 * y2q.diff(x, 2) + 3 * x * y2q.diff(x) + (1 - x) * y2q), x, 0, 2))

# 4x^2 y'' + y = 0 Euler double root
ye = x ** sp.Rational(1, 2) * (1 + sp.log(x))
print("Euler double resid:", sp.simplify(sp.expand(4 * x ** 2 * ye.diff(x, 2) + ye)))
