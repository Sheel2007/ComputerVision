import cv2


class Detector:
    def __init__(self, classifier):
        self.classifier = classifier

    def detect(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        object = self.classifier.detectMultiScale(gray, 1.1, 4)
        new_img = img
        return object, new_img

    def draw(self, img, object, text, color, lineThickness):
        for x, y, w, h in object:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, lineThickness)
            cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)


cat_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
detector = Detector(cat_cascade)

# img = cv2.imread('cat.jpg')
cap = cv2.VideoCapture(0)
while True:

    _, img = cap.read()

    resized = cv2.resize(img, (470, 300))
    cv2.imshow('original img', resized)

    object, new_img = detector.detect(img)
    detector.draw(new_img, object, "Human", (255, 0, 255), 4)

    r = cv2.resize(img, (470, 300))
    cv2.imshow('new img', r)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
