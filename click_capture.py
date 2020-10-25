import cv2
import numpy as np

ix,iy = -1,-1
filename  = 'test1.png'
filename1 = 'test1.txt'
f1 = open(filename1, 'w+')
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    # Check if the event was right click 
    if event==cv2.EVENT_RBUTTONDOWN:
        # create a circle at that position # of radius 30 and color red
        cv2.circle(img,(x,y),5,(0,0,255),-1)
        ix,iy = x,y
        print(ix,iy)
        f1.write("%s %s \n" % (ix,iy))

    # Check if the event was left click 
    if event==cv2.EVENT_LBUTTONDBLCLK:
        # create a circle at that position         # of radius 30 and color blue
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        ix,iy = x,y
        print(ix,iy)
        f1.write("%s %s \n" % (ix,iy))

    #  check if the event was scrolling 
    if event==cv2.EVENT_MBUTTONDBLCLK:
        # create a circle at that position         # of radius 30 and color green
        cv2.circle(img,(x,y),5,(0,255,0),-1)
        ix,iy = x,y
        print(ix,iy)
        f1.write("%s %s \n" % (ix,iy))


img=cv2.imread(filename)
# Create a black image, a window and bind the function to window
#img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("test.png")
cv2.setMouseCallback("test.png",draw_circle)

while(1):
    cv2.imshow('test.png',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(ix,iy)
f1.close()
cv2.destroyAllWindows()
