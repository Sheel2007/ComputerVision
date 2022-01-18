import cv2
import numpy as np

darkest_yellow = (110, 110, 20)
lightest_yellow = (255, 255, 130)

darkest_red = (61, 31, 0)
lightest_red = (255, 71, 71)

darkest_black = (0, 0, 0)
lightest_black = (60, 30, 80)

darkest_white = (200, 200, 200)
lightest_white = (255, 255, 255)

darkest_blue = (110, 0, 100)
lightest_blue = (180, 250, 255)

darkest_green = (50, 100, 30)
lightest_green = (110, 255, 150)

array = np.array([[darkest_yellow, lightest_yellow, 'yellow'],
              [darkest_red, lightest_red, 'red'],
              [darkest_black, lightest_black, 'black'],
              [darkest_white, lightest_white, 'white'],
              [darkest_blue, lightest_blue, 'blue'],
              [darkest_green, lightest_green, 'green']])


def checker(rgb, darkest, lightest):
    r, g, b = rgb
    if darkest[0] <= r and r <= lightest[0]:  # red
        if darkest[1] <= g and g <= lightest[1]:
            if darkest[2] <= b and b <= lightest[2]:
                return True
    return False


cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    color = (img[img.shape[0] // 2][img.shape[1] // 2][2],
             img[img.shape[0] // 2][img.shape[1] // 2][1],
             img[img.shape[0] // 2][img.shape[1] // 2][0])

    img = cv2.circle(img, (img.shape[1] // 2, img.shape[0] // 2), 5, (0, 0, 0), 3)

    cols = []

    for i in array:
        a = checker(color, darkest=i[0], lightest=i[1])
        if a:
            cols.append(i[2])

    distance = 39

    for i in cols:
        cv2.putText(img, f"{i}", (img.shape[0] // 2 - 100, img.shape[1] // 2 - distance), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
        distance += 50

    title = 'Color Detection'
    cv2.imshow(title, img)

    keyCode = cv2.waitKey(1)

    if cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) < 1 or keyCode == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
