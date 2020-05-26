import cv2, pickle, time
from alarm_system import raise_alarm

def camera():

    face_cascade = cv2.CascadeClassifier("C:\\Users\\Swapnil\\OpenCV_git_projects\\Cascades\\haarcascade_frontalface_alt2.xml")

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml")

    with open("labels.pickle", "rb") as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}

    video = cv2.VideoCapture(0)

    while True:

        check, frame = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

        for (x, y, w, h) in face:
            # print(x, y, w, h)

            ##region of interest
            roi_gray = gray[y:y+h, x:x+w]

            id_, conf = recognizer.predict(roi_gray)
            if conf >= 45:  #and conf <= 85:
                print(labels[id_])
                print("Authorised")
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame,name,(x,y), font, 1, color, stroke, cv2.LINE_AA)

            if conf >= 95:
                print("Unauthorised")
                ##save image to send
                cv2.imwrite("image.jpg", frame)

                raise_alarm.alarm()
                ##Open image path and send it via email
                with open('image.jpg', 'rb') as f:
                    file_data = f.read()
                    raise_alarm.sendEmail(file_data)
                    time.sleep(30)

            ##rectangle on the face
            rectangle = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        ##Display screen
        cv2.imshow("Capturing", frame)

        # ##if the label name is in list then authorised
        # for i in range(len(list_labels)):
        #     if labels[id_] in list_labels[i]:
        #         print("Authorised Personnel")
        #         break
        #
        #     elif labels[id_] not in list_labels:
        #         print("Unauthorised")



        ##Close frame on pressing "q"
        key = cv2.waitKey(1)
        if key == ord("q"):
            break


    video.release()
    cv2.destroyAllWindows()

camera()