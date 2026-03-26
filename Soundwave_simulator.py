#Fun Time 
#BLX UNKNOWN 0

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-3, 3)
ax.axis('off')
ax.set_title('SOUND WAVE VISUALIZER', color='#00ffcc',
             fontsize=18, fontweight='bold')
 
x = np.linspace(0, 2 * np.pi, 1000)
colors_wave = ['#ff0080', '#00ffcc', '#ffff00', '#aa00ff', '#ff6600']
lines = []
for i, c in enumerate(colors_wave):
    line, = ax.plot(x, np.zeros_like(x), color=c,
                    linewidth=2, alpha=0.8)
    lines.append(line)
 
# bar visualizer at bottom
n_bars = 60
bar_x = np.linspace(0, 2 * np.pi, n_bars)
bars = ax.bar(bar_x, np.zeros(n_bars),
              width=0.08, color='#00ffcc',
              alpha=0.6, bottom=-3)
 
frame_count = [0]
 
def animate(frame):
    frame_count[0] += 1
    f = frame_count[0]
 
    for i, line in enumerate(lines):
        freq = (i + 1) * 0.7
        amp  = 0.6 / (i + 1) * 3
        phase = f * 0.05 * (i + 1)
        y = amp * np.sin(freq * x + phase)
        line.set_ydata(y)
        line.set_color(plt.cm.hsv((i / 5 + f * 0.002) % 1))
 
    for i, bar in enumerate(bars):
        height = abs(np.sin(bar_x[i] * 2 + f * 0.1)) * \
                 np.random.uniform(0.5, 1.5)
        bar.set_height(height)
        bar.set_color(plt.cm.plasma(height / 2))
 
    return lines
 
ani = animation.FuncAnimation(fig, animate, interval=30,
                               blit=False, cache_frame_data=False)
plt.tight_layout()
plt.show()