import requests 

import numpy as np

import cv2 
from matplotlib import pyplot as plt
from insightface.app import FaceAnalysis

def download_and_decode_cv2(url):
    rr = requests.get(url)
    _nparr = np.frombuffer(rr.content, np.uint8)
    _img = cv2.imdecode(_nparr, cv2.IMREAD_COLOR)
    return _img

def show_cv2_image(img): # <-- ဒီလိုရေးတာ function ကို define တယ်လို့ ခေါ်တယ်။
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def get_face_landmark(img, plot=True, is_cv2=True):
    if is_cv2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    app = FaceAnalysis(allowed_modules=["detection", "landmark_3d_68"], providers=['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    
    faces = app.get(img)
    f = faces[0]
    landmark = f["landmark_3d_68"]

    plt.imshow(img)
    # draw only 1/3 of the landmarks because the markers are large
    plt.scatter(x=landmark.T[0,::3], y=landmark.T[1,::3], marker=".")

    return landmark

def get_black_and_white_flip(img, threshold=200):
    img_ = 255 - img
    img_[img_ < threshold] = 0
    return img_