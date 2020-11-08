import cv2
import imutils
import numpy as np
import os
import os.path
import sys
import glob 
file_list = os.listdir("VMO_images")

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    # Check if the event was right click 
    if event==cv2.EVENT_RBUTTONDOWN:
        # create a circle at that position # of radius 30 and color red
        cv2.circle(img,(x,y),5,(0,0,255),-1)
        ix,iy = x,y
        print(ix,iy)
        f1.write("%s %s %s \n" % ("red",ix,iy))

    # Check if the event was left click 
    if event==cv2.EVENT_LBUTTONDBLCLK:
        # create a circle at that position         # of radius 30 and color blue
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        ix,iy = x,y
        print(ix,iy)
        f1.write("%s %s %s \n" % ("blue",ix,iy))

    #  check if the event was scrolling 
    if event==cv2.EVENT_MBUTTONDBLCLK:
        # create a circle at that position         # of radius 30 and color green
        cv2.circle(img,(x,y),5,(0,255,0),-1)
        ix,iy = x,y
        print(ix,iy)
        f1.write("%s %s %s \n" % ("green",ix,iy))


ix,iy = -1,-1
#f1 = open(filename1, 'w+')

#for file_name in file_list:
for file_name in glob.glob('VMO_images/*.png'):
   src_file = str(file_name)
#   src_file = "VMO_images/" + str(file_name)
   outfile  = src_file +  ".txt"
   img=cv2.imread(str(src_file))
   img = imutils.resize(img, width=800)
   cv2.namedWindow(str(src_file))
   f1 = open(str(outfile), 'w+')
   cv2.setMouseCallback(str(src_file),draw_circle)
   #sys.exit()
   print(src_file) 

   while(True):
      cv2.imshow(str(src_file),img)
      k = cv2.waitKey(20) & 0xFF 
      if k == ord('q'):
         cv2.waitKey(0)
         break
      elif k == ord('a'):
         print(ix,iy)
   f1.close()

   cv2.destroyAllWindows()
