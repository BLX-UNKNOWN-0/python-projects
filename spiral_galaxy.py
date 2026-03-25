#Fun Time 
#BLX UNKNOWN 0

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# generate galaxy stars
n_stars = 3000
theta = np.random.uniform(0, 4 * np.pi, n_stars)
r = np.random.exponential(0.5, n_stars)
noise = np.random.normal(0, 0.05, n_stars)

x = r * np.cos(theta + r) + noise
y = r * np.sin(theta + r) + noise
colors = plt.cm.plasma(np.random.uniform(0, 1, n_stars))
sizes = np.random.uniform(0.5, 8, n_stars)

scat = ax.scatter(x, y, c=colors, s=sizes, alpha=0.8)
title = ax.set_title('SPIRAL GALAXY', color='white',
                      fontsize=18, fontweight='bold', pad=15)

def animate(frame):
    angle = frame * 0.01
    new_x = x * np.cos(angle) - y * np.sin(angle)
    new_y = x * np.sin(angle) + y * np.cos(angle)
    scat.set_offsets(np.c_[new_x, new_y])
    colors_shifted = plt.cm.plasma(
        (np.random.uniform(0, 1, n_stars) + frame * 0.01) % 1
    )
    scat.set_color(colors_shifted)
    return scat,

ani = animation.FuncAnimation(fig, animate, frames=500,
                               interval=30, blit=True)
plt.tight_layout()
plt.show()