import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2):
    return (x1**2 + x2**2)

ls = 100
li = -100

x1 = np.linspace(li, ls, num=1000)
X1, X2 = np.meshgrid(x1, x1)

Y = f(X1, X2)

x1_candidato, x2_candidato = 50, 50
f_candidato = f(x1_candidato, x2_candidato)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# TODO: Verificar essa linha pois está dando erro devido ao método "plot_surface" não existir
#ax.plot_surface(X1, X2, Y, rstride=10, cstrid=10, alpha=0.6, cmap='jet')

ax.scatter(x1_candidato, x2_candidato, f_candidato, marker='x', s=90, linewidths=3, color='red')

#plot_surface(X1, X2, Y, rstride=10, cstrid=10, alpha=0.6, cmap='jet')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('f(x1,x2)')
plt.tight_layout()
plt.show()