#Fun Time 
#BLX UNKNOWN 0

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap

# custom fire colormap
fire_colors = [
    (0,    '#000000'),  # black  - cold
    (0.3,  '#ff0000'),  # red    - warm
    (0.6,  '#ff6600'),  # orange - hot
    (0.8,  '#ffcc00'),  # yellow - very hot
    (1.0,  '#ffffff'),  # white  - max heat
]
fire_cmap = LinearSegmentedColormap.from_list(
    'fire', [c[1] for c in fire_colors])

# canvas size
W, H = 120, 80

fig, ax = plt.subplots(figsize=(6, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_title('🔥 FIRE', color='#ff6600',
             fontsize=22, fontweight='bold', pad=10)

fire = np.zeros((H, W), dtype=np.float32)
img  = ax.imshow(fire, cmap=fire_cmap, vmin=0,
                 vmax=255, aspect='auto',
                 origin='lower', interpolation='bilinear')

def animate(frame):
    global fire

    # ignite bottom 2 rows randomly
    fire[0, :] = np.random.randint(200, 256, W).astype(np.float32)
    fire[1, :] = np.random.randint(160, 256, W).astype(np.float32)

    # spread fire upward using numpy — NO loops!
    # average 4 neighbors below and cool slightly
    new_fire        = fire.copy()
    new_fire[2:, :] = (
        fire[1:-1, :]           +   # directly below
        np.roll(fire[1:-1, :],  1, axis=1) +  # below left
        np.roll(fire[1:-1, :], -1, axis=1) +  # below right
        fire[:-2, :]                # two below
    ) / 4.1                         # divide by slightly more than 4 = cooling

    # add random turbulence so it flickers
    turbulence = np.random.uniform(-8, 8, (H, W)).astype(np.float32)
    new_fire   = np.clip(new_fire + turbulence, 0, 255)

    fire = new_fire
    img.set_array(fire)
    return img,

ani = animation.FuncAnimation(fig, animate, interval=30,
                               blit=True, cache_frame_data=False)
plt.tight_layout()
plt.show()
