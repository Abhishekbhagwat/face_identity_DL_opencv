import cv2
import os
import time

total_pic = 0
print('Enter the name of the person to capture training images')
name = input()
os.chdir('train_img')
os.makedirs(name)

# change the cascader file path to the absolute path on your system
fa = cv2.CascadeClassifier('/Users/abhishek.bhagwat/Desktop/facial_attendance/faces.xml')

# Start image capture on webcam. Port 0
cap = cv2.VideoCapture(0)
# sleep for 2 seconds to warm up camera
time.sleep(2)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = fa.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # cropped=frame[y:2*(y+h),x:2*(x+w)]
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2,cv2.LINE_AA)
        total_pic += 1
        cv2.imwrite(name + '/' + 'ActiOn_' + str(total_pic) + '.jpg', frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(100)

    if total_pic > 50:
        break

cap.release()
cv2.destroyAllWindows()
