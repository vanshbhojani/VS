import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

## lint plotting
'''
ypoints = np.array([2,8,25,45,67,35,48,45,87])

plt.plot(
    ypoints,
    marker = 'o', # marker parameter is used to mark the points on the graph
    markersize = 5,
    markerfacecolor = 'red',
    markeredgecolor = 'green',
    linestyle = '--',
    color = 'hotpink',
    linewidth = 2
)
plt.show()
'''
## lables and title

ypoints = np.array([2,8,25,45,67,35,48,45,87])
xpoints = np.array([1,2,3,4,5,6,7,8,9])

plt.plot(
    xpoints,
    ypoints,
    marker = 'o', # marker parameter is used to mark the points on the graph
    markersize = 5,
    markerfacecolor = 'red',
    markeredgecolor = 'green',
    linestyle = '--',
    color = 'hotpink',
    linewidth = 2
)
plt.title("my first graph" , fontsize = 20 , color = 'green' , loc = 'left') # loc parameter is used to set the location of the title
plt.xlabel("x axis" , fontsize = 15 , color = 'blue')
plt.ylabel("y axis" , fontsize = 15 , color = 'blue')
plt.show()

