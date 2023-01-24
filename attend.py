import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64 
from pyzbar.pyzbar import decode


#start the web cam
cap=cv2.VideoCapture(0)
names=[]

#function for attendance file


fob=open('attendance.txt','a+')  
def enterData(z):
  if z in names:
    pass
  else:    
    names.append(z)
    z=''.join(str(z))     
    fob.write(z+'\n')
    return names

#function data present or not

def checkData(data):
  data=str(data)
  if data in names:
    print("Already Present")
  else:
    print("\n"+str(len(names)+1)+'\n'+'Present Done')
    enterData(data)

#function for Frame of Web-Cam

while True:
	check,frame = cap.read()
	d=decode(frame)
	try:
		for obj in d:
			checkData(obj.data)
	except:
		print("error.....")

	cv2.imshow("attendance",frame)
	key = cv2.waitKey(1)
	if key ==ord("q"):
		print(names)
		break
cap.release()
cv2.destroyAllWindows()

#   while True:
#     _,frame=cap.read()  
#     decodedObject=decode(frame)
#     for obj in decodedObject:
#       checkData(obj.data)
#       time.sleep(1)
  
#     cv2.imshow("Frame",frame)
  
  
# #close 
  
#     if cv2.waitKey(1)==ord("s"):
#       break
# cap.release()
# cv2.destroyAllWindows()
#   #  fob.close()