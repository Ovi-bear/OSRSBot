test = WindowCapture('Old School RuneScape')



while True:
    screenie = test.capture_screen()
    cv.imshow('test', screenie)
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
