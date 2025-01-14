rate = 140    # ($ / y^3) "Dollars per cubic yard"
inTy = 1 / 36 # (y / in.) "Inches to yards coefficient"

T_costs = [1, 2, 5, 10, 25, 100, 500, 1000]
heights = [1, 2, 3, 4, 5, 6, 12]

def quad(a, b, c, p=None):
	#((-4 * inTy * ((-1 * (rate * (1 / inTy))) / (c * h)))**0.5)
	if p:
		return ((-1 * b) + ((b**2 - (4 * a * c))**0.5)) / (2 * a)
	elif p == False:
		return ((-1 * b) - ((b**2 - (4 * a * c))**0.5)) / (2 * a)
	else:
		return quad(a, b, c, True), quad(a, b, c, False)
		# return (-1 * b) + (((b**2 - (4 * a * c))**0.5) / (2 * a)), (-1 * b) - (((b**2 - (4 * a * c))**0.5) / (2 * a))

def vertex(a, b, c):
	x = -b / (2 * a)
	y = (a * x**2) + (b * x) + c
	return x, y


# sol_lw = lambda c, h: ((-4 * inTy * ((-1 * (rate * (1 / inTy))) / (c * h)))**0.5)
# sol_lw = lambda c, h: quad(inTy, 0, ((-1 * rate) * (1 / inTy)) / (c * h), p=True)  #((-4 * inTy * ((-1 * (rate * (1 / inTy))) / (c * h)))**0.5)
sol_lw = lambda c, h: quad(inTy * h * rate, 0, -c, p=True)  #((-4 * inTy * ((-1 * (rate * (1 / inTy))) / (c * h)))**0.5)

for c in T_costs:
	for h in heights:
		lw = sol_lw(c, h)
		l = (lw**0.5) / inTy
		w = l
		print("c: $ {c}, h: {h}\", lw: {lw} y^2, lxw: ({l}\" x {w}\", v: {v})".format(c=c, h=h, lw=lw, l=l, w=w, v=vertex(inTy * h * rate, 0, -c)))

for c, h in zip(T_costs, heights):
	lw = sol_lw(c, h)
	l = (lw**0.5) / inTy
	w = l
	print("c: $ {c}, h: {h}\", lw: {lw} y^2, lxw: ({l}\" x {w}\", v: {v})".format(c=c, h=h, lw=lw, l=l, w=w, v=vertex(inTy * h * rate, 0, -c)))