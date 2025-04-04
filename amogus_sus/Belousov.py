import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('on')
ax.set_aspect('equal')

backpack = patches.FancyBboxPatch(
    (2, 3), 1.2, 4,
    boxstyle="round,pad=0.2,rounding_size=0.5",
    facecolor='darkred', edgecolor='black', linewidth=2
) 
ax.add_patch(backpack)

body = patches.Ellipse(
    (5, 5), 5, 7, angle=0,
    facecolor='red', edgecolor='black', linewidth=2
)
ax.add_patch(body)

visor = patches.Ellipse(
    (6, 6.5), 3, 2, angle=0,
    facecolor='cyan', alpha=0.6, edgecolor='black', linewidth=1
)
ax.add_patch(visor)

left_leg = patches.Polygon(
    [[3.3, 2.5], [4.3, 2.5], [4.3, 1], [3.3, 1]],
    closed=True, facecolor='red', edgecolor='black', linewidth=1
)
ax.add_patch(left_leg)

right_leg = patches.Polygon(
    [[5.7, 2.5], [6.7, 2.5], [6.7, 1], [5.7, 1]],
    closed=True, facecolor='red', edgecolor='black', linewidth=1
)
ax.add_patch(right_leg)

plt.show()