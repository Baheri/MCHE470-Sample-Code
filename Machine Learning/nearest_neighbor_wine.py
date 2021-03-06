#! /usr/bin/env python 

##########################################################################################
# nearest_neighbor_example.py
#
# Script to look at an example nearest-neighbor classificaiton
#
# Based on: 
#   http://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html
#
# NOTE: Plotting is set up for output, not viewing on screen.
#       So, it will likely be ugly on screen. The saved PDFs should look
#       better.
# 
# Created: 12/4/13 
#   - Joshua Vaughan 
#   - joshua.vaughan@louisiana.edu
#   - http://www.ucs.louisiana.edu/~jev9637
#
# Modified:
#   * 
##########################################################################################

import numpy as np
from scipy import genfromtxt
from matplotlib.pyplot import * 
from matplotlib.colors import ListedColormap
from sklearn import neighbors
from sklearn.preprocessing import scale

n_neighbors = 11

# import some data to play with
data = genfromtxt("wine_data.csv",delimiter=",",skip_header=1)
X = data[:,(1,11)]    # we only take two features at a time

# Normalize/scale the data
X[:,0] = 1*X[:,0]/np.max(X[:,0])
X[:,1] = 1*X[:,1]/np.max(X[:,1])
# or
# X = scale(X)


# the first column is the category
y = data[:,0]    

# Get the A data
A_itemindex=np.where(y==1)
X_A = X[A_itemindex]
y_A = y[A_itemindex]

# Get the B data
B_itemindex=np.where(y==2)
X_B = X[B_itemindex]
y_B = y[B_itemindex]

# Get the <C data
C_itemindex=np.where(y==3)
X_C = X[C_itemindex]
y_C = y[C_itemindex]

# Show the raw data
plot(X_A[:,0],X_A[:,1],'r*',label='Wine 1')
plot(X_B[:,0],X_B[:,1],'bo',label='Wine 2')
plot(X_C[:,0],X_C[:,1],'kx',label = 'Wine 3')
xlim(0.9*min(X[:,0]),1.1*max(X[:,0]))
ylim(0.9*min(X[:,1]),1.1*max(X[:,1]))

leg = legend(loc='upper right', ncol = 2, fancybox=True, borderaxespad=0.2)
ltext  = leg.get_texts() 
setp(ltext,fontsize=16)

# save the figure as a high-res pdf in the current folder
# savefig('NearestNeighbor_RawData.pdf',dpi=300)


h = .01  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min()*0.9, X[:, 0].max()*1.1
    y_min, y_max = X[:, 1].min()*0.9, X[:, 1].max()*1.1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    figure()
    pcolormesh(xx, yy, Z, cmap=cmap_light)

    # include the raw data
    plot(X_A[:,0],X_A[:,1],'r*',label='Wine 1')
    plot(X_B[:,0],X_B[:,1],'bo',label='Wine 2')
    plot(X_C[:,0],X_C[:,1],'kx',label = 'Wine 3')


    # Plot also the training points
#     scatter(X[:, 0], X[:, 1], cmap=cmap_bold)
    xlim(xx.min(), xx.max())
    ylim(yy.min(), yy.max())
    xlabel('Feature 1',fontsize=22,labelpad=8)
    ylabel('Feature 2',fontsize=22,labelpad=8)

    leg = legend(loc='upper right', ncol = 2, fancybox=True, borderaxespad=0.2)
    ltext  = leg.get_texts() 
    setp(ltext,fontsize=16)

show()
