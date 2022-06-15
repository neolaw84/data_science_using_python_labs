import numpy as np
from matplotlib import pyplot as plt

def visualize(X, y, n_cols=5, n_rows=None):
    n_rows = n_rows if n_rows else len(y) // n_cols;
    if len(y) > n_rows * n_cols:
        n_rows = n_rows + 1
    _, ax = plt.subplots(n_rows, n_cols)
    if not isinstance(y, np.ndarray):
        _y = np.array(y)
    else:
        _y = y
    if len(y) < n_rows * n_cols:
        _y = np.hstack((_y, np.full((n_rows*n_cols-len(y)), -999)))
    for X_, y_, a in zip(X, y, ax.flatten()):
        a.imshow(X_, cmap=plt.get_cmap('gray'))
    plt.show()
    print (_y.reshape(n_rows, n_cols))