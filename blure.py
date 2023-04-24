import cv2

face_cascade=cv2.CascadeClassifier("Files\haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    if ret:
        frame=cv2.flip(frame,1)
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray ,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            face_area=frame[y:y+h,x:x+w]
            face_area=cv2.GaussianBlur(face_area,(51,51),10)
            frame[y:y+h,x:x+w]=face_area
    cv2.imshow("Webcam",frame)
    q=cv2.waitKey(1)
    if q==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()