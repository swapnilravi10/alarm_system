import cv2
import pickle
from alarm_system import raise_alarm

def camera():
    face_cascade = cv2.CascadeClassifier("C:\\Users\\Swapnil\\OpenCV_git_projects\\Cascades\\haarcascade_frontalface_alt2.xml")
    profile_cascade = cv2.CascadeClassifier("C:\\Users\\Swapnil\\OpenCV_git_projects\\Cascades\\haarcascade_profileface.xml")

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml")
    # labels= {}
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
            if conf >= 45 and conf <= 85:
                print(id_)
                print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame,name,(x,y), font, 1, color, stroke, cv2.LINE_AA)
            # cv2.imwrite("my_gray_image.png", roi_gray)

            ##rectangle on the face
            rectangle = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

            profile_face = profile_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
            for(a,b,c,d) in profile_face:
                cv2.rectangle(frame, (a,b), (a+c,b+d), (0,255,0), 2)

        ##Display screen
        cv2.imshow("Capturing", frame)



        key = cv2.waitKey(20)
        if key == ord("q"):
            break

        if labels[id_] == "swapnil":
            print("Authorised Personnel")
            # raise_alarm.intruder()
            continue
        else:
            print("Unauthorised")

    video.release()
    cv2.destroyAllWindows()

