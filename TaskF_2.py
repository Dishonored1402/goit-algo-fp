import matplotlib.pyplot as plt
import math

def draw_pythagoras_tree(ax, x, y, angle, size, level):
    if level == 0:
        return

    x_end = x + size * math.cos(math.radians(angle))
    y_end = y + size * math.sin(math.radians(angle))

    ax.plot([x, x_end], [y, y_end], color="brown", linewidth=level)

    new_size = size * 0.7

    draw_pythagoras_tree(ax, x_end, y_end, angle - 45, new_size, level - 1)
    draw_pythagoras_tree(ax, x_end, y_end, angle + 45, new_size, level - 1)

if __name__ == "__main__":
    recursion_level = int(input("Введіть рівень рекурсії (спробуйте 10): "))

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.axis('off')

    initial_x, initial_y = 0.5, 0
    initial_angle = 90
    initial_size = 0.2

    draw_pythagoras_tree(ax, initial_x, initial_y, initial_angle, initial_size, recursion_level)

    plt.show()