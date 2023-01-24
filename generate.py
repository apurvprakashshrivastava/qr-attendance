from MyQR import myqr
import os
import pybase64
import base64

f=open('students.txt','r')
lines = f.read().split("\n")
print(lines)

for i in range(0,len(lines)):
    data=lines[i].encode()
    name=base64.b64encode(data)
    version, level, qr_name=myqr.run(
        str(name),
        level='Q',
        version=15,

    #backgroud
        picture='bg.jpg',
        colorized=True,
        contrast=50.0,
        brightness=20.0,
        save_name=str(lines[i]+'.bmp')
)
