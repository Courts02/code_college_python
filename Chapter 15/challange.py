import numpy as np
import matplotlib.pyplot as plt

# Data for pie chart
labels = ['Python', 'Javascript', 'Html', 'Css']
sizes = [40, 20, 20, 20]

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Favorite Programming Languages')
plt.show()