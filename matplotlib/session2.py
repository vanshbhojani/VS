import matplotlib
import matplotlib.pyplot as plt # pyplot is a collection of command style functions that make matplotlib work like MATLAB
import pandas as pd
import numpy as np

# print(matplotlib.__version__)

'''xpoints= np.array([0, 6])
ypoints= np.array([0, 250])

plt.plot(
    xpoints,
    ypoints
)
plt.show()
'''
#To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'
'''
xpoints= np.array([1,8])
ypoints= np.array([3,10])

plt.plot(
    xpoints,
    ypoints,
    'o'
)
plt.show()
'''
'''
xpoints= np.array([1,2,6,8])
ypoints= np.array([3,8,1,10])

plt.plot(
    xpoints,
    ypoints,

)
plt.show()
'''
'''
ypoints= np.array([3,8,1,10])

plt.plot(
    ypoints,
    )

plt.show()
'''
'''
ypoints = np.array([3,8,1,10])

plt.plot(
    ypoints,
    marker = 'o' # marker parameter is used to mark the points on the graph
)
plt.show()
'''

# what is fmt : You can also use the shortcut string notation parameter to specify the marker.
'''
# we can use the format string parameter, also called fmt, to specify the color and line type of the marker.
# and we cna use the marker linestylr and color parameter to achieve the same result.

ypoints = np.array([2,8,54,65,47,89,45,78,12,34])

plt.plot(
    ypoints,
    'o:r' # o = marker, : = line style, r = color
)
plt.show()
'''
'''
ypoints = np.array([2,8,54,65,47,89,45,78,12,34])
plt.plot(
    ypoints,
    ':'
)
plt.show()
'''
'''
ypoints = np.array([2,8,54,65,47,89,45,78,12,34])

plt.plot(
    ypoints,
    color = 'r',
    marker = 'o',
    linestyle = ':'
)
plt.show()
'''

# marker size and color
'''
ypoints = np.array([2,8,54,65,47,89,45,78,12,34])

plt.plot(
    ypoints,
    color = 'r',
    marker = 'o',
    markersize = 5, # marker size mate aapde ms or markersize parameter use kari sakiye chhiye
    linestyle = ':'
)
plt.show()

'''

# marker Edge color
'''
ypoints = np.array([2,8,54,65,47,89,45,78,12,34])

plt.plot(
    ypoints,
    color = 'g',
    marker = 'o',
    markersize = 5,
    markeredgecolor = 'r', # markeredgecolor or mec 
    linestyle = ':'
)
plt.show()
'''

# marker face color
'''
ypoints = np.array([2,8,54,65,47,89,45,78,12,34])

plt.plot(
    ypoints,
    color = 'y',
    marker = 'o',
    markersize = 5,
    markerfacecolor = 'r', # markerfacecolor or mfc
    linestyle = ':'
)
plt.show()
'''

# marker eade color and marker face color

ypoints = np.array([2,8,54,65,47,89,45,78,12,34])   

plt.plot(
    ypoints,
    color = 'y',
    marker = 'o',
    markersize = 5,
    mec = 'b', # markeredgecolor or mec
    mfc = 'r', # markerfacecolor or mfc
    linestyle = '-.'
)
plt.show()



