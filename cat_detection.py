import cv2

cat_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')


img = cv2.imread('cat.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cats = cat_cascade.detectMultiScale(gray, 1.1, 4)


for x, y, w, h in cats:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 4)

cv2.putText(img, "Cat", (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
