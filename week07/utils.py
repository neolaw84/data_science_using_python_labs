from io import StringIO
from matplotlib.pyplot import gray
from matplotlib import pyplot as plt
import requests

import cv2
import numpy as np
from scipy import misc
import pandas as pd

my_data = """id, length, width
height
1,10.0,10.0
9.0
2,12.0,8.0
17.5
"""

readable_data = StringIO(my_data)

df = pd.read_csv(readable_data, skiprows=2,names=[str(i) for i in range(3)])
np_data = df.values

def download_and_decode_cv2(url, grayscale=True):
    rr = requests.get(url)
    _nparr = np.frombuffer(rr.content, np.uint8)
    _img = cv2.imdecode(_nparr, cv2.IMREAD_COLOR)
    if grayscale:
        _img = cv2.cvtColor(_img, cv2.COLOR_RGB2GRAY)
    return _img

def get_image(url=None, grayscale=True):
    if url:
        img = download_and_decode_cv2(url=url, grayscale=grayscale)
        img = img/255
    else:
        img = misc.face()
        img = img/255
        if grayscale:
            img = img @ [0.2126, 0.7152, 0.0722]
    return img

X_0 = 0
X_1 = 1
def plot_points_and_vectors(my_points, xlim=(0.0, 1.1), ylim=(0.0, 1.1)):
    plt.scatter(x=my_points[X_0], y=my_points[X_1])
    for x_0, x_1 in zip(my_points[X_0, :], my_points[X_1, :]):
        plt.arrow(0, 0, dx=x_0, dy=x_1, )
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.show()