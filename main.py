import windowcapture
import vision
import cv2 as cv

wincap = windowcapture.WindowCapture('Old School RuneScape')

while True:
    screenie = wincap.capture_screen()
    vision.findUser('user.PNG', screenie)
    cv.imshow('test', screenie)
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break