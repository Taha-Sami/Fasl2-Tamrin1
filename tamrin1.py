import cv2
import numpy as np
import matplotlib.pyplot as plt
import time 
t0=time.time()



cap=cv2.VideoCapture(0)
w=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#print(w,h)

while True:
	ret,frame=cap.read()
	if ret:
		t1=time.time()-t0
		normal=cv2.flip(frame,1)
		t1=str(round(t1,2))
		cv2.putText(normal,t1,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)

		inv=255-normal
		
		gray=cv2.cvtColor(normal,cv2.COLOR_BGR2GRAY)

		
		red=normal.copy()
		red[:,:,2]=255
		
		final1 = np.concatenate([normal,red],axis=1)
		final2 = np.concatenate([inv,inv],axis=1)
		final = np.concatenate([final1,final2],axis=0)



		cv2.imshow('webcam',final)
		q=cv2.waitKey(1)
		if q==ord('q'):
			break

cv2.destroyAllWindows()
cap.release()
