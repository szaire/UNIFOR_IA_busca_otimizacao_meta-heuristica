import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2):
    return -(x2 + 47) * np.sin(np.sqrt(np.abs((x1/2) + (x2+47)))) - x1 * np.sin(np.sqrt(np.abs(x1 - (x2+47))))

ls_x1 = 20
li_x1 = -200

ls_x2 = 20
li_x2 = -200

num = 1000

x1 = np.linspace(li_x1, ls_x1, num)
x2 = np.linspace(li_x2, ls_x2, num)

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