from matplotlib import pyplot

def show_points(X, c="blue", plt=None):
    if plt:
        _plt = plt
    else:
        _plt = pyplot
    _plt.xlim((-3, 3))
    _plt.ylim((-3, 3))
    _plt.scatter(X[0], X[1], marker="o", c=c)
    [_plt.annotate("p_{}".format(i), (X[0, i] + 0.1, X[1, i])) for i in range(0, X.shape[0] + 1)]
