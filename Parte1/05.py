import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2):
    return (x1 - 1)**2 + (100 * (x2 - x1**2)**2)

ls = 8
li = -8
num = 1000

x1 = np.linspace(-2, 2, num)
x2 = np.linspace(-1, 3, num)

X1, X2 = np.meshgrid(x1, x2)

Y = f(X1, X2)

x1_candidato, x2_candidato = 0, 0
f_candidato = f(x1_candidato, x2_candidato)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X1, X2, Y, rstride=10, cstride=10, alpha=0.6, cmap='jet')
ax.scatter(x1_candidato, x2_candidato, f_candidato, marker='x', s=90, linewidths=3, color='red')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('f(x1,x2)')
plt.tight_layout()
plt.show()