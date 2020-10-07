
import numpy as np
import torch
import math
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import GPyOpt

import os

import matplotlib as mpl
import matplotlib.tri as tri

import ternary
import pickle
import datetime


def latin_hypercube(n_pts, dim):
    """Basic Latin hypercube implementation with center perturbation."""
    X = np.zeros((n_pts, dim))
    centers = (1.0 + 2.0 * np.arange(0.0, n_pts)) / float(2 * n_pts)
    for i in range(dim):  # Shuffle the center locataions for each dimension.
        X[:, i] = centers[np.random.permutation(n_pts)]

    # Add some perturbations within each box
    pert = np.random.uniform(-1.0, 1.0, (n_pts, dim)) / float(2 * n_pts)
    X += pert
    return X



def constrained_latin_hypercube(n_goal = 15, dim = 3, n_init = 200):
    assert n_init >= n_goal
    
    X = np.zeros((n_init, dim))
    centers = (1.0 + 2.0 * np.arange(0.0, n_init)) / float(2 * n_init)
    for i in range(dim):  # Shuffle the center locataions for each dimension.
        X[:, i] = centers[np.random.permutation(n_init)]
    # Add some perturbations within each box
    pert = np.random.uniform(-1.0, 1.0, (n_init, dim)) / float(2 * n_init)
    X += pert
    
    X_constrained = np.array([[100, 100, 100]])
#     materials = ['CsPbI', 'MAPbI', 'FAPbI']
    for i in X:
        if 0.995 < i[0] + i[1] + i[2] <= 1.005:
            if ((167*i[0]+217*i[1]+253*i[2])+220)/(1.4142*(119+220)) > 0.80:
                X_constrained = np.append(X_constrained, [i], axis = 0) 
                
    X_constrained = X_constrained[1:]
    
    
    
    X_ = np.array([[100, 100, 100]])
    for j in X_constrained:
        j = np.round(j, 2)
        if np.sum(j) == 1:
            X_ = np.append(X_, [j], axis = 0) 
    X_ = X_[1:]
            
    print('found: ' + str(len(X_)) +' with n_init =' +str(n_init))
    
    if len(X_) >= n_goal:
        X_ = X_[0:n_goal]
        dataset = pd.DataFrame(X_, columns = ['Cs', 'MA', 'FA'])
        return dataset
    else:
        return constrained_latin_hypercube(n_goal, dim, n_init * 2)


