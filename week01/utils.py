import requests
from IPython.display import Image

import numpy as np
from matplotlib import pyplot as plt
import cv2

r = requests.get("https://i.ibb.co/5WNdy1R/1200px-Tom-Holland-by-Gage-Skidmore.jpg")

def download_tom_holland():    
    return Image(r.content, width=200)

def download_and_decode_cv2(url):
    rr = requests.get(url)
    _nparr = np.frombuffer(rr.content, np.uint8)
    _img = cv2.imdecode(_nparr, cv2.IMREAD_COLOR)
    return _img

def put_mustache(original_img, mustache, x_offset, y_offset, width=500, height=500):
    
    mustache_resized = cv2.resize(mustache, (width, height))

    rows, columns, chanels = mustache_resized.shape
    roi = original_img[y_offset:y_offset+height, x_offset:x_offset+width]

    mustache_resized_gray = cv2.cvtColor(mustache_resized, cv2.COLOR_RGB2GRAY)
    ret, mask = cv2.threshold(mustache_resized_gray, 120, 255, cv2.THRESH_BINARY)
    final_roi = cv2.bitwise_or(roi,roi,mask = mask)

    mustache_img = original_img.copy()
    mustache_img[y_offset : y_offset + height, x_offset : x_offset + width]=final_roi

    return mustache_img