import vlc
import numpy
import cv2
import time

class MyMediaPlayer():
    def __init__(self):
        self.detector=cv2.CascadeClassifier("Files\haarcascade_frontalface_default.xml")
        self.cap=cv2.VideoCapture(0)

    def play_music(self,dir):
        music=vlc.MediaPlayer(dir)
        music.play()
        time.sleep(15)
    
    def webcam_stream(self):
        while True:
            ret , frame = self.cap.read()
            if ret:
                frame=cv2.flip(frame , 1)
                gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                result=self.detector.detectMultiScale(gray)

                for (x , y , w , h) in result:
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

                cv2.imshow("webcam" , frame)
                q=cv2.waitKey(1)
                if q==ord('q'):
                    break
        cv2.destroyAllWindows()
        self.cap.release()
            
mp=MyMediaPlayer()
mp.webcam_stream()
# mp.play_music("1.mp3")
