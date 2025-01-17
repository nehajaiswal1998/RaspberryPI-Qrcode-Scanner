import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_PLAIN

while(True):
	_,sucess = cap.read()
	
	decodeobj = decode(frame)
	for obj in decodeobj:
		cv2.putText(frame,str(obj.data),(50,50),font,3,(255,0,0),3)
	
	cv2.imshow('Frame',frame)
	
	key = cv2.waitKey(1)
	if key==27:
		break
