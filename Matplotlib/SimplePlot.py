import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Create Figures
# An empty figure with no Axes
fig = plt.figure()  
plt.show()

# Figure with one line
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.show()

# A figure with a single Axes
fig, ax = plt.subplots()  
plt.show()

# A figure with a 2x2 grid of Axes
fig, ax = plt.subplots(2, 2)  
plt.show()

# Coding styles
x = np.linspace(0, 2, 100)

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x**3, label='cubic')
ax.plot(x, np.log(x), label='logaritmic')
ax.set_xlabel('x label')  
ax.set_ylabel('y label')  
ax.set_title("Simple functions")
ax.legend()
plt.show()

# Making a helper functions
def plotter1(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
plotter1(ax1, data1, data2, {'marker': 'x'})
plotter1(ax2, data3, data4, {'marker': 'o'})
plt.show()

fig, ax = plt.subplots(figsize=(5, 2.7))
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
l.set_linestyle(':')
plt.show()

# Colors
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.scatter(data1, data2, s=60, facecolor='C4', edgecolor='k')
plt.show()

# Linewidtsh, linestyles and markersizes
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(data1, 'o', label='data1')
ax.plot(data2, 'd', label='data2')
ax.plot(data3, 'v', label='data3')
ax.plot(data4, 's', label='data4')
ax.legend()
plt.show()

mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)

ax.set_xlabel('Length [cm]')
ax.set_ylabel('Probability')
ax.set_title('Aardvark lengths\n (not really)')
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.axis([55, 175, 0, 0.03])
ax.grid(True)
plt.show()

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']
ax.bar(categories, np.random.rand(len(categories)))
plt.show()