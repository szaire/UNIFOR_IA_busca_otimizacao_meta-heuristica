import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2):
    return (x1 * np.sin(4 * np.pi * x1)) - (x2 * np.sin((4 * np.pi * x2) + np.pi)) + 1

x1_ls = 3
x1_li = -1

x2_ls = -1
x2_li = 3

num = 1000

x1 = np.linspace(x1_li, x1_ls, num)
x2 = np.linspace(x2_li, x2_ls, num)

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