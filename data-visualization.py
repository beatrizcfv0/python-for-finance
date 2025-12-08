# 08/12/2025
# Página 187

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1000)

y = np.random.standard_normal((1000, 2))
x = np.arange(len(y))

'''
plt.plot(x, y)
plt.plot(y.cumsum()) # cumulative sum
plt.grid(False)
plt.axis('equal') # empty, off, equal, scaled, tight, image, [xmin, xmax, ymin, ymax]
'''

'''
plt.figure(figsize=(10, 6))
plt.plot(y.cumsum(), 'b', lw = 1.5) # colour
plt.plot(y.cumsum(), 'ro') # red and circle marker
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Simple plot')
'''

# 2 plots
'''
plt.figure(figsize=(10, 6))
plt.subplot(211)
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.legend(loc=0)
plt.ylabel('value')
plt.title('A Simple Plot');
plt.subplot(212)
plt.plot(y[:, 1], 'g', lw=1.5, label='2st')
plt.plot(y[:, 1], 'ro')
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
'''

# Plot and bar chart
'''
plt.figure(figsize=(10, 6))
plt.subplot(121)
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.title('1st Data Set')
plt.subplot(122)
plt.bar(np.arange(len(y)), y[:, 1], width=0.5, color = 'g', label='2nd')
plt.xlabel('index')
'''

# Scatter plot
'''
plt.figure(figsize=(10, 6))
plt.scatter(y[:, 0], y[:, 1], marker='o')
plt.xlabel('1st')
plt.ylabel('2nd')
'''

# Scatter plot in third dimension
'''
c = np.random.randint(0, 10, len(y))
plt.figure(figsize=(10, 6))
plt.scatter(y[:, 0], y[:, 1], c=c, cmap='coolwarm', marker='o')
'''

# Histogram
'''
plt.figure(figsize=(10, 6))
plt.hist(y, label=['1st', '2nd'], bins=25)
plt.xlabel('value')
plt.ylabel('frequency')
'''

# Interactive 2D plotting
plt.show()