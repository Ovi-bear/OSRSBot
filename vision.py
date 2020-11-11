import cv2 as cv
import numpy as np

def findUser(user_img_path,client):
    user = cv.imread(user_img_path)
    result = cv.matchTemplate(client, user, cv.TM_CCOEFF_NORMED)

    threshold = 0.9

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    if max_val > threshold:
        w = user.shape[1]
        h  = user.shape[0]
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        image = cv.rectangle(client,top_left,bottom_right,255,2)
        cv.putText(image, 'userg', (top_left[0], top_left[1] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
