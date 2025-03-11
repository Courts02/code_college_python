# 15.1
import matplotlib.pyplot as plt

# Generating the first five cubic numbers
x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

# Plotting the first five cubic numbers
plt.figure(figsize=(6, 4))
plt.plot(x_values, y_values, 'bo-', markersize=8, label="Cubes")
plt.xlabel("Number")
plt.ylabel("Cube of Number")
plt.title("First Five Cubic Numbers")
plt.legend()
plt.show()

# Generating the first 5000 cubic numbers
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, 'r-', linewidth=1)
plt.xlabel("Number")
plt.ylabel("Cube of Number")
plt.title("First 5000 Cubic Numbers")
plt.show()

# 15.2
import numpy as np

# Generating data
x_values = np.arange(1, 5001)
y_values = x_values**3

# Scatter plot with colormap
plt.figure(figsize=(8, 5))
plt.scatter(x_values, y_values, c=y_values, cmap='viridis', edgecolors='none', s=10)
plt.xlabel("Number")
plt.ylabel("Cube of Number")
plt.title("Cubes with Colormap")
plt.colorbar(label="Cube Value")  # Adds a color legend
plt.show()

# 15.3
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Generate a random walk
rw = RandomWalk(5000)  # 5000 steps instead of 50,000
rw.fill_walk()

# Plot the walk
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the path using a line (instead of scattered points)
ax.plot(rw.x_values, rw.y_values, linewidth=1)

# Emphasize start and end points
ax.scatter(0, 0, c='green', edgecolors='black', s=100, label="Start")
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='black', s=100, label="End")

ax.set_title("Molecular Motion (Random Walk)", fontsize=14)
ax.legend()
plt.show()

# 15.4
from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = choice([1, -1]) * choice(range(9))  # Expanding distance choices
            y_step = choice([1]) * choice(range(9))  # Only forward movement

            if x_step == 0 and y_step == 0:
                continue  # Skip steps that don't move

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)

# 15.5
from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Generate a step with direction and distance."""
        direction = choice([1, -1])
        distance = choice(range(9))  # 0-8 step distance
        return direction * distance

    def fill_walk(self):
        """Generate the full walk using get_step()."""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue  # Skip stationary points

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)
