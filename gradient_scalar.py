import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.linspace(-2.5, 2.5, 11), np.linspace(-2.5, 2.5, 11))

phi = Y*Y*np.sin(X)+X*np.exp(Y)

u = Y*Y*np.cos(X)+np.exp(Y)
v = 2*Y*np.sin(X)+X*np.exp(Y)



magnitude = np.hypot(u, v)
safe_magnitude = np.where(magnitude == 0, 1, magnitude)

u_norm = u / safe_magnitude
v_norm = v / safe_magnitude

plt.figure(figsize=(8, 6))

heatmap = plt.contourf(X, Y, phi, levels=50, cmap='viridis')
cbar = plt.colorbar(heatmap, shrink=0.8)
cbar.set_label('Skalärfält magnitud')



Q = plt.quiver(X, Y, 
               u_norm, v_norm,
               magnitude,
               cmap='viridis',
               pivot='mid',
               angles='xy',
               scale_units='xy',
               scale=2.5)

plt.colorbar(Q, label='Vektormagnitud', shrink=0.8)

plt.xticks(np.arange(-2.5, 2.6, 0.5))
plt.yticks(np.arange(-2.5, 2.6, 0.5))
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)

plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.savefig('gradient_exempel1v2.pdf')


plt.show()

