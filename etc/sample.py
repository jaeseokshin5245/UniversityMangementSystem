import matplotlib.pyplot as plt

# Create a new figure with figsize (width, height)
fig = plt.figure(figsize=(3, 2))

# Add a plot to the figure
ax = fig.add_subplot(1, 1, 1)

# Plot some data
ax.plot([1, 2, 3, 4], [10, 20, 30, 40])

# Show the plot
plt.show()
