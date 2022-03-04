import cv2
import sys
import paho.mqtt.client as mqtt
import time

mqtt_broker = "192.168.1.189"
broker_port = 1883


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print(f"connected with Result Code: {rc}")
    else:
        print(f"bad connection with Result Code: {rc}")


def on_message(client, userdata, message):
    print(f"Message Recieved: {message.payload.decode()}")
    # Do something here with the message


def on_log(client, obj, level, string):
    print(string)


def read_sensor():
    sensor_reading = "Hola hola caracola"
    return

    # create client object


client = mqtt.Client(clean_session=True)
client.connected_flag = False  # create flag in class
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log

client.connect(mqtt_broker, broker_port)
if client.connect(mqtt_broker, broker_port) != 0:
    print("Could not connect!")
    sys.exit(-1)

client.loop_start()
# to see connection status from publisher side
while not client.connected_flag:
    print("in wait loop")
    time.sleep(1)
print("in main loop!")


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

    if len(faces) > 0:
        print("face detected")
        my_topic = 'air_in'
        # publish over MQTT air in
    elif len(smile) > 0:
        print("Smile detected")
        my_topic = 'air_out'
        # publish over MQTT sir out
    else:
        print("face not detected")
        my_topic = 'none'



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

    my_message = 'hello'
    client.publish(my_topic, my_message, qos=1, retain=False)
    time.sleep(4)



    #cv2.imshow("Output", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
#cv2.destroyAllWindows()
