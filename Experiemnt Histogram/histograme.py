import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Sample data for streaming services popularity (number of subscribers in millions)
streaming_data = {
    'Netflix': 200,
    'Amazon Prime': 200,
    'Disney+': 153.6,
    'HBO Max': 77,
    'Apple TV+': 25,
    'Paramount+': 32,
    'Showmax': 1.7,
    'Crunchyroll': 50,
    'Youtube Premium': 125
}

# Improved color gradients
company_colors = {
    'Netflix': ['#e50914', '#8b0000'],  # Bright red to dark red
    'Amazon Prime': ['#00a8e1', '#002244'],  # Light blue to dark navy
    'Disney+': ['#113ccf', '#0093ff'],  # Deep blue to sky blue
    'HBO Max': ['#800080', '#ff00ff'],  # Purple to magenta
    'Apple TV+': ['#444444', '#bbbbbb'],  # Medium gray to light gray
    'Paramount+': ['#0060a9', '#33ccff'],  # Dark blue to cyan
    'Showmax': ['#ff007f', '#660033'],  # Bright pink to dark purple
    'Crunchyroll': ['#ff6600', '#ffcc00'],  # Deep orange to golden yellow
    'Youtube Premium': ['#ff0000', '#990000']  # Bright red to dark red
}

# Create figure and axis with more height and adjusted margins
fig, ax = plt.subplots(figsize=(12, 8))
fig.patch.set_facecolor('#1a1a1a')  # Black subplot background
ax.set_facecolor('#1a1a1a')  # Deep black background
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)  # Increase bottom padding

# Histogram bins
x = np.arange(len(streaming_data))
heights = list(streaming_data.values())

# Plot bars with transparent color
bars = ax.bar(x, heights, color='none', edgecolor='none')  # Remove edges

# Generate a gradient image for each bar
for bar, height, service in zip(bars, heights, streaming_data.keys()):
    left, right = bar.get_x(), bar.get_x() + bar.get_width()
    bottom, top = 0, height

    # Create a 1D vertical gradient
    gradient = np.linspace(0, 1, 256).reshape(-1, 1)
    cmap = cm.colors.LinearSegmentedColormap.from_list(service, company_colors[service])
    gradient = cmap(gradient)
    gradient = gradient[:, :, :3]

    # Overlay the gradient image onto the bar
    ax.imshow(gradient, extent=[left, right, bottom, top], aspect='auto', alpha=0.85, origin='lower')

# 🎯 **Add Growth Line**
x_smooth = np.linspace(0, len(x) - 1, 300)  # Smooth X values for curve
coeffs = np.polyfit(x, heights, 2)  # Fit quadratic curve (change degree if needed)
y_smooth = np.polyval(coeffs, x_smooth)  # Compute Y values for trend

ax.plot(x_smooth, y_smooth, color='white', linestyle='--', linewidth=2, label='Growth Trend')

# Customize labels and text colors
ax.set_title('Streaming Services Popularity', fontsize=16, fontweight='bold', color='white', pad=20)
ax.set_xlabel('Streaming Service', color='white', fontsize=14, labelpad=10)
ax.set_ylabel('Subscribers (Millions)', color='white', fontsize=14, labelpad=10)
ax.set_xticks(x)
ax.yaxis.set_tick_params(colors='white')
ax.set_xticklabels(streaming_data.keys(), rotation=45, ha='right', color='white', fontsize=12)

# Set y-axis limits with padding
ax.set_ylim(0, max(heights) * 1.1)  # Add 10% padding at the top

# Set x-axis limits with padding
ax.set_xlim(-0.5, len(streaming_data) - 0.5)

# Add labels above bars with contrasting colors
for bar, height in zip(bars, heights):
    ax.text(bar.get_x() + bar.get_width() / 2, height + 5, f'{height}', 
            ha='center', va='bottom', fontsize=12, fontweight='bold', color='white')

# Hide unnecessary spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')

# Add legend for growth line
ax.legend(loc='upper left', fontsize=12, facecolor='#333333', edgecolor='white')

# Show the plot
plt.show()

