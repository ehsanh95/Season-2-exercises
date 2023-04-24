import cv2

face_cascade=cv2.CascadeClassifier("Files\haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier('Files\haarcascade_eye.xml')
cap=cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    if ret:
        frame=cv2.flip(frame,1)
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face=face_cascade.detectMultiScale(gray)

        for (x,y,w,h) in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            face_scop_gray=gray[y:y+h,x:x+w]
            face_scop_color=frame[y:y+h,x:x+w]

            eye=eye_cascade.detectMultiScale(face_scop_gray)
            for(ex,ey,ew,eh) in eye:
                cv2.rectangle(face_scop_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    cv2.imshow("Webcam",frame)
    q=cv2.waitKey(1)
    if q==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()