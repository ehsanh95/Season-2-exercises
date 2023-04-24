import cv2 
import numpy as np
import time

cap=cv2.VideoCapture(0)

t0=time.time()

width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=cap.get(cv2.CAP_PROP_FPS)
print( width , height , fps)


while True:
    ret , frame = cap.read()
    if ret:
        frame=cv2.flip(frame , 1)

        sub_frame1=frame[:240 , :320]

        sub_frame2=frame[:240,320:]
        sub_frame2[:,:,2]=255

        sub_frame3=frame[240: , :320]
        sub_frame3=255-sub_frame3

        sub_4=frame[240: , 320:]
        sub_4=cv2.cvtColor(sub_4, cv2.COLOR_BGR2GRAY)
        sub_frame4=sub_4.reshape(240,320,1)
        sub_frame4=np.concatenate((sub_frame4,sub_frame4,sub_frame4),2)
        
        up_frame=np.concatenate((sub_frame1,sub_frame2) , 1)
        down_frame=np.concatenate((sub_frame3,sub_frame4),1)
        new_frame=np.concatenate((up_frame,down_frame),0)

        t1=time.time()-t0
        t1_str=str(round(t1,3))

        cv2.putText(new_frame,"Ehsan Hosseini",(5,35), cv2.FONT_HERSHEY_COMPLEX,
                    1,(0,0,255),2)
        cv2.putText(new_frame,t1_str,(85,85), cv2.FONT_HERSHEY_COMPLEX,
                    1,(0,0,255),2)

        cv2.imshow("webcam" , new_frame)
        q=cv2.waitKey(1)
        if q==ord('q'):
            break
print(sub_frame1.shape , sub_frame2.shape , sub_frame3.shape , sub_frame4.shape )
cv2.destroyAllWindows()
cap.release()
