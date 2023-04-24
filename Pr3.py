import cv2
import numpy as np
import vlc
import time

class MyClass():
    def __init__(self):
        self.face_cascade=cv2.CascadeClassifier("Files\haarcascade_frontalface_default.xml")
        self.eye_cascade=cv2.CascadeClassifier('Files\haarcascade_eye.xml')
        self.cap=cv2.VideoCapture(0)

    def detect_face(self,mode=None):
        while True:
            if mode==None:
                ret , frame = self.cap.read()
                if ret:
                    frame=cv2.flip(frame,1)
                    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    face=self.face_cascade.detectMultiScale(gray)

                    for (x,y,w,h) in face:
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.imshow("Webcam",frame)
                q=cv2.waitKey(1)
                if q==ord('q'):
                    break
            elif mode=="blure":
                ret , frame = self.cap.read()
                if ret:
                    frame=cv2.flip(frame,1)
                    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces=self.face_cascade.detectMultiScale(gray ,1.3,5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                        face_area=frame[y:y+h,x:x+w]
                        face_area=cv2.GaussianBlur(face_area,(51,51),10)
                        frame[y:y+h,x:x+w]=face_area
                cv2.imshow("Webcam",frame)
                q=cv2.waitKey(1)
                if q==ord('q'):
                    break
            else:
                print("unknown mode")
                mode=None
        cv2.destroyAllWindows()
        self.cap.release()

    


    def detect_eye(self):
        while True:
            ret , frame = self.cap.read()
            if ret:
                frame=cv2.flip(frame,1)
                gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face=self.face_cascade.detectMultiScale(gray)

                for (x,y,w,h) in face:
                    # cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                    face_scop_gray=gray[y:y+h,x:x+w]
                    face_scop_color=frame[y:y+h,x:x+w]

                    eye=self.eye_cascade.detectMultiScale(face_scop_gray)
                    for(ex,ey,ew,eh) in eye:
                        cv2.rectangle(face_scop_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            cv2.imshow("Webcam",frame)
            q=cv2.waitKey(1)
            if q==ord('q'):
                break
        cv2.destroyAllWindows()
        self.cap.release()
        
    # def do_something(self):
    #     while True:
    #         inp=input("what do yo want? -play music- , -read a book- or -watch a move- ? ")

    #         if inp=="play music":
    #             dir=input("please write the address of music ")
    #             music=vlc.MediaPlayer(dir)
    #             music.play()
    #             time.sleep(35)
    #             break
    #         elif inp=="watch a move":
    #             cv2.imshow("see this",cv2.imread("Files\img1.jpg"))
    #             cv2.waitKey(0)
    #             break
    #         elif inp=="read a book":
    #             cv2.imshow("read this",cv2.imread("Files\img2.jpg"))
    #             cv2.waitKey(0)
    #             break
    #         else:
    #             print("please check your answer")
                

mc=MyClass()
mc.detect_face("blfhf")
