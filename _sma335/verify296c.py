import sympy as sp

x = sp.symbols("x", positive=True)
N = 14

# Case 3 example: x^2 y'' - 2x y' + (2-x) y = 0, roots 2 and 1
c = [0] * (N + 1)
c[0] = 1
for n in range(1, N + 1):
    c[n] = sp.nsimplify(c[n - 1] / (n * (n + 1)))
print("c:", c[:7])
y1 = sum(c[n] * x ** (n + 2) for n in range(N + 1))
u = sp.series(y1 / x ** 2, x, 0, 6).removeO()
print("u:", sp.expand(u))
g = sp.series(1 / u ** 2, x, 0, 6).removeO()
print("g=1/u^2:", sp.expand(g))
integrand = sp.series(x ** -2 * g, x, 0, 5).removeO()
print("integrand:", sp.expand(integrand))
# integrate term by term, keeping log for x^-1
terms = sp.Add.make_args(sp.expand(integrand * x ** 2))
print("scaled terms:", terms)
I = sp.Integer(0)
for t in sp.Add.make_args(sp.expand(integrand)):
    p = sp.Poly(sp.expand(t * x ** 3), x)
    pass
# manual: integrand = sum a_k x^k, integrate a_k x^k -> a_k x^(k+1)/(k+1), except k=-1 -> log
ser = sp.series(integrand * x ** 2, x, 0, 4).removeO()
print("integrand*x^2 =", sp.expand(ser))
I = -sp.Integer(0)
poly = sp.Poly(sp.expand(ser), x)
for (k,), a in poly.terms():
    power = k - 2
    if power == -1:
        I += a * sp.log(x)
    else:
        I += a * x ** (power + 1) / (power + 1)
print("I =", sp.simplify(I))
y2 = sp.expand(y1 * I)
print("y2 =", sp.series(y2, x, 0, 4))
res = sp.expand(x ** 2 * y2.diff(x, 2) - 2 * x * y2.diff(x) + (2 - x) * y2)
print("residual:", sp.series(res, x, 0, 3))

# Bessel-type: x^2 y'' + x y' + (x^2-1) y = 0
c = [0] * (N + 1)
c[0] = 1
for n in range(2, N + 1, 2):
    c[n] = sp.nsimplify(-c[n - 2] / ((n + 1) ** 2 - 1))
print("bessel c:", c[:8])
yb = sum(c[n] * x ** (n + 1) for n in range(N + 1))
print("yb:", sp.series(yb, x, 0, 8))
print("resid:", sp.series(sp.expand(x ** 2 * yb.diff(x, 2) + x * yb.diff(x) + (x ** 2 - 1) * yb), x, 0, 2))
