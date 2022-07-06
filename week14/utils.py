import numpy as np
from scipy import linalg as sp_linalg
from sklearn import datasets, metrics, linear_model, model_selection as ms

from matplotlib import pyplot as plt

def scatter_xy(x, y, xlabel="", ylabel="MedHouseVal", marker="."):
    plt.xlabel=xlabel
    plt.ylabel=ylabel
    plt.scatter(x, y, marker=marker)

def draw_line(coef_, intercept_, xlim=(0, 14), ylim=None, num=3, color="red"):
    x = np.linspace(xlim[0], xlim[1], num=num)
    y = coef_ * x + intercept_
    plt.plot(x, y, color=color)
    # plt.Line2D(x, y, color=color)
    plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)