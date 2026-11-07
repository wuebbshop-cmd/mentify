import sympy as sp

x = sp.symbols("x", positive=True)


def trunc(res, n):
    return sp.simplify(sp.expand(sp.series(res, x, 0, n).removeO()))


# E3 with enough coefficients
C = [sp.Integer(1), sp.Integer(0)] + [0] * 14
for r in range(1, 14):
    C[r + 2] = sp.Rational(r * (r + 2) * C[r] + C[r - 1], (r + 1) * (r + 2))
y3 = sum(C[n] * x ** n for n in range(13))
r3 = sp.expand((x ** 2 - 1) * y3.diff(x, 2) + 3 * x * y3.diff(x) + x * y3)
print("E3 c0..c8:", [C[n] for n in range(9)])
print("E3 residual lowest:", sp.series(r3, x, 0, 1))

D = [sp.Integer(0), sp.Integer(1)] + [0] * 14
for r in range(1, 14):
    D[r + 2] = sp.Rational(r * (r + 2) * D[r] + D[r - 1], (r + 1) * (r + 2))
y3b = sum(D[n] * x ** n for n in range(13))
r3b = sp.expand((x ** 2 - 1) * y3b.diff(x, 2) + 3 * x * y3b.diff(x) + x * y3b)
print("E3b c0..c8:", [D[n] for n in range(9)])
print("E3b residual lowest:", sp.series(r3b, x, 0, 1))

# Airy full check
A = [0] * 20
A[0] = 1
for m in range(0, 14):
    A[m + 3] = sp.Rational(A[m], (m + 2) * (m + 3))
y4 = sum(A[n] * x ** n for n in range(15))
print("Airy even c:", [A[n] for n in range(10)])
print("Airy even resid:", sp.series(sp.expand(y4.diff(x, 2) - x * y4), x, 0, 1))
B = [0] * 20
B[1] = 1
for m in range(0, 14):
    B[m + 3] = sp.Rational(B[m], (m + 2) * (m + 3))
y4b = sum(B[n] * x ** n for n in range(15))
print("Airy odd c:", [B[n] for n in range(10)])
print("Airy odd resid:", sp.series(sp.expand(y4b.diff(x, 2) - x * y4b), x, 0, 1))

# E5 with more terms
for rr in [sp.Integer(1), sp.Rational(1, 2)]:
    co = [sp.Integer(1), 0]
    for n in range(2, 12):
        co.append(sp.simplify(co[n - 2] / ((2 * (n + rr) - 1) * (n + rr - 1))))
    y = sum(co[n] * x ** (n + rr) for n in range(len(co)))
    res = sp.expand(2 * x ** 2 * y.diff(x, 2) - x * y.diff(x) + (1 - x ** 2) * y)
    print("E5 r=", rr, [sp.nsimplify(c) for c in co])
    print("   resid order:", sp.series(res * x ** (1 - rr), x, 0, 3))

# E7 check second solution needs log: verify forced obstruction
print("E7 indicial:", sp.solve(sp.Eq(sp.symbols('r') * (sp.symbols('r') - 1) - 2 * sp.symbols('r') + 2, 0), sp.symbols('r')))

# E8 / E9 with more coefficients
co = [sp.Integer(1), sp.Integer(0), sp.Rational(1, 2), sp.Rational(1, 6)]
for m in range(2, 12):
    co.append(co[m] / ((m + 1) * (m + 2)))
y8 = sum(co[n] * x ** n for n in range(len(co)))
print("E8", sp.series(sp.expand(y8.diff(x, 2) - y8 - x), x, 0, 1))

co9 = [sp.Integer(1), sp.Integer(0), sp.Rational(-1, 2), sp.Rational(1, 6)]
for m in range(2, 12):
    co9.append(-co9[m] / ((m + 1) * (m + 2)))
y9 = sum(co9[n] * x ** n for n in range(len(co9)))
print("E9", sp.series(sp.expand(y9.diff(x, 2) + y9 - x), x, 0, 1))

# E6: verify y1 and y2 more strongly with mpmath numeric residual
import mpmath as mp
mp.mp.dps = 40


def y1(t, N=40):
    return sum(t ** (n - 1) / (mp.factorial(n) ** 2) for n in range(N))


def y2(t, N=40):
    y = y1(t, N) * mp.log(t)
    s = mp.mpf(0)
    H = mp.mpf(0)
    for n in range(1, N):
        H += mp.mpf(1) / n
        s += H * t ** n / (mp.factorial(n) ** 2)
    return y - 2 * s / t


for t in [mp.mpf("0.7"), mp.mpf("1.3"), mp.mpf("2.1")]:
    for name, f in (("y1", y1), ("y2", y2)):
        h = mp.mpf("1e-15")
        d2 = (f(t + h) - 2 * f(t) + f(t - h)) / h ** 2
        d1 = (f(t + h) - f(t - h)) / (2 * h)
        res = t ** 2 * d2 + 3 * t * d1 + (1 - t) * f(t)
        print("E6", name, t, mp.nstr(res, 8))

# E1 closed form check
co = [mp.mpf(1)]
for n in range(0, 20):
    co.append(2 * (co[n - 1] if n - 1 >= 0 else 0) / (n + 1))
print("E1 c0..c6:", [sp.Rational(2) * (sp.Rational(1) if False else 0)])
