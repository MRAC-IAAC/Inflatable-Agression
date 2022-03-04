import cv2
import sys

video = cv2.VideoCapture(0)

try:
    face_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier('Resources/haarcascade_smile.xml')
except AttributeError:
    sys.exit("no xml file")

count = 0

while True:
    check, frame = video.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY2GRAY)
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)
    smile = smile_cascade.detectMultiScale(frame, scaleFactor=1.8, minNeighbors=20)

    if len(smile) > 0:
        print("face detected")
        # publish over MQTT air in
    else:
        print("face not detected")
        # publish over MQTT sir out
    for x, y, w, h in faces:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        count = count + 1
        name = './images/Faces/' + str(count) + '.jpg'
        print("creating Images..." + name)
        cv2.imwrite(name, frame[y:y + h, x:x + w])

    for x, y, w, h in smile:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
        count = count + 1
        name = './images/Smile_faces/' + str(count) + '.jpg'
        print("creating Images..." + name)
        cv2.imwrite(name, frame[y:y + h, x:x + w])


    cv2.imshow("Output", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
#cv2.destroyAllWindows()
