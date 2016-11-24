delta = 0.01
x = np.arange(-1.5, 1.5, delta)
y = np.arange(-1.5, 1.5, delta)
X, Y = np.meshgrid(x, y)
Z = cos(X**2 * 2*pi) * cos(Y**2 * 2*pi) * exp(-(X**2 + Y**2))

f, ax1 = plt.subplots(1, figsize=[4, 2.472135955])
#f, ax1 = plt.subplots(1)

c1 = ax1.contour(X, Y, Z, levels=[-0.3, -0.2, -0.1, 0.1, 0.2, 0.3])

ax1.set_xlabel('x-coordinate')
ax1.set_ylabel('y-coordinate')

ax1.minorticks_on()
#grid(color='grey', zorder=0)

savefig('f03.pdf')
