import numpy as np
from scipy import linalg as sp_linalg
from sklearn import datasets, metrics, linear_model, model_selection as ms

from matplotlib import pyplot as plt
from matplotlib import axes
plt.subplots

def scatter_xy(x, y, xlabel="", ylabel="MedHouseVal", marker=".", plt=plt):
    plt.xlabel=xlabel
    plt.ylabel=ylabel
    plt.scatter(x, y, marker=marker)

def draw_line(coef_, intercept_, xlim=(0, 14), ylim=None, num=3, color="red", subplot=None):
    if subplot:
        plt = subplot
    x = np.linspace(xlim[0], xlim[1], num=num)
    y = coef_ * x + intercept_
    plt.plot(x, y, color=color)
    # plt.Line2D(x, y, color=color)
    if subplot:
        plt.axis(xmin=xlim[0], xmax=xlim[1])
    else:
        plt.xlim(xlim)

    if ylim and subplot:
        plt.axis(ymin=ylim[0], ymax=ylim[1])
    elif ylim:
        plt.ylim(ylim)