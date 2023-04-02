import cv2
import imutils
import numpy as np
import math 
import os
import os.path
import sys
import glob 
# mouse callback function

def draw_grid(img, line_color=(187, 187, 187), thickness=1, type_=cv2.LINE_AA, pxstep=20):
    '''(ndarray, 3-tuple, int, int) -> void
    draw gridlines on img
    line_color:
        BGR representation of colour
    thickness:
        line thickness
    type:
        8, 4 or cv2.LINE_AA
    pxstep:
        grid line frequency in pixels
    '''
    x = pxstep
    y = pxstep
    while x < img.shape[1]:
        cv2.line(img, (x, 0), (x, img.shape[0]), color=line_color, lineType=type_, thickness=thickness)
        x += pxstep

    while y < img.shape[0]:
        cv2.line(img, (0, y), (img.shape[1], y), color=line_color, lineType=type_, thickness=thickness)
        y += pxstep

def draw_circle(event,x,y,flags,param):
    global ix,iy, ic,noart,x2,y2,nobrpt, nobrpt2
    # Check if the event was right click 
    # Check if the event was left click 
    if event==cv2.EVENT_LBUTTONDBLCLK or event==cv2.EVENT_RBUTTONDOWN:
        # create a circle at that position         # of radius 5 and color blue
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        ix,iy = x,y
        ic = ic + 1
        xc.append(x)
        yc.append(y)
        print(ic, x, y)
        if ic > 2:
    # 10 cm - length for normalization (point3)
    #    normd = 0.1*math.sqrt((xc[1]-xc[0])**2 + (yc[1]-yc[0])**2.0)
         normd = abs(yc[1]-yc[0])
        if ic == 5:
        # width of the vastus medialis  (point3)
         vswidth = abs(xc[4]-xc[3])
         f1.write("%s %f \n" % ("point3",vswidth/normd))
         #f1.write("%s %s %s %s \n" % ("point3: vastus",vswidth/normd, xc[4]/normd,xc[3]/normd))
         print("point3_vastus",vswidth/normd, xc[4]/normd,xc[3]/normd)
        if ic == 3:
        # offset (point 2)
         ymid = (yc[0] + yc[1])/2.0
         offs = ymid - yc[2]
         f1.write("%s %f \n" % ("point1", normd))
         f1.write("%s %f \n" % ("point2", offs/normd))
         #f1.write("%s %s %s %s \n" % ("point2:Proximal/distal distance from the middle of the patella to the end", offs/normd, ymid/normd, yc[2]/normd))
         print("point1:length of the patella", normd)
         print("point2:Proximal/distal distance from the middle of the patella to the end", offs/normd, ymid/normd, yc[2]/normd)
        if ic == 6: 
         arent = abs(yc[5] - yc[2])
         f1.write("%s %f \n" % ("point5", arent/normd))
         #f1.write("%s %s %s %s \n" % ("point5:Distance from the end of the vastus to where the artery (ies) enter the musc", arent/normd, yc[5]/normd, yc[2]/normd))
         print("point5:Distance from the end of the vastus to where the artery (ies) enter the musc", arent/normd, yc[5]/normd, yc[2]/normd)
        if ic == 7:
        # distance from the popliteal (point 6)
         pwidth = abs(xc[6]-xc[5])
         f1.write("%s %f \n" % ("point6", pwidth/normd))
         #f1.write("%s %s %s %s \n" % ("point6:Distance from the popliteal artery to the muscle", pwidth/normd, xc[6]/normd, xc[5]/normd))
         print("point6:Distance from the popliteal artery to the muscle", pwidth/normd, xc[6]/normd, xc[5]/normd)
        if ic == 8:
        # distance from the edge of the muscle (point 7)
         ewidth = abs(xc[5]-xc[7])
         f1.write("%s %f\n" % ("point7", ewidth/normd))
         #f1.write("%s %s %s %s \n" % ("point7", ewidth/normd, xc[5]/normd, xc[7]/normd))
         print("point7:Distance from the edge of the muscle to where the artery makes its first significant turn distally", ewidth/normd, xc[5]/normd, xc[7]/normd)
        if ic > 9:
        # disyance from where the artery enters the muscle (point 9)
         dis = abs(xc[5]-xc[ic-1])
         br2 = 9 + int(nobrpt) 
         print("no of arteries", noart,ic,nobrpt)
         if noart > str(1) and ic > int(br2) :
            dis2 = abs(xc[8] - xc[ic-1])
            f1.write("%s %d %f\n" % ("point9 artery 2", ic-9-int(nobrpt), dis2/normd))
            #f1.write("%s %d %s %s %s\n" % ("point9:Distance from where the artery 2 enters the muscle to the various branch points", ic-9-int(nobrpt), dis2/normd, xc[8]/normd,xc[ic-1]/normd))
            print("point9:Distance from where the artery 2 enters the muscle to the various branch points", ic-9-int(nobrpt), dis2/normd, xc[8]/normd,xc[ic-1]/normd)
         else :
            f1.write("%s %d %f \n" % ("point9 artery 1", (ic-9), dis/normd))
            #f1.write("%s %s %s %s %s\n" % ("point9:Distance from where the artery enters the muscle to the various branch points", str(ic-8), dis/normd, xc[5]/normd, xc[ic-1]/normd))
            print("point9:Distance from where the artery enters the muscle to the various branch points", ic-9, dis/normd, xc[5]/normd, xc[ic-1]/normd)



#    #  check if the event was scrolling 
    if event==cv2.EVENT_MBUTTONDBLCLK:
        # create a circle at that position         # of radius 5 and color green
        cv2.circle(img,(x,y),5,(0,255,0),-1)
        ix,iy = x,y
        ic = ic + 1
        xc.append(x)
        yc.append(y)
        print(ic, x, y)

ix,iy = -1,-1
x2,y2 = -1,-1
#read png files in VMO_images folder 
#for file_name in glob.glob('VMO_Scan_images/*.png'):
for file_name in glob.glob('VMO_images/*.png'):
   src_file = str(file_name)
   xc = [] 
   yc = []
   ic = 0 
   noart = 0
   nobrpt = 1 
   nobrpt2 = 1 
   # output file name 
   outfile  = src_file+".txt"
   img=cv2.imread(str(src_file))
   img = imutils.resize(img, width=800)
   draw_grid(img) 
   cv2.namedWindow(str(src_file))
   # open outfile for writing x ,y 
   f1 = open(str(outfile), 'w+')
   # draw circles 
   cv2.setMouseCallback(str(src_file),draw_circle)
   #sys.exit()
   print(src_file) 
   
   while(True):
   # show the image 
      cv2.imshow(str(src_file),img)
      k = cv2.waitKey(20) & 0xFF 
      # press q to quit 
      if k == ord('q'):
         cv2.waitKey(0)
         break
      if k == ord('r'): 
         noart  = input("Number of arteries:\n")
         nobrpt = input("Number of branch points:\n")
         if noart > str(1): 
            nobrpt2 = input("Enter number of branch points in second artery \n")
        # f10.write("%s %s \n" % ("point4:Number of arteries entering the vastus medialis from the popliteal", noart))
         f1.write("%s %s \n" % ("point4", noart))
         f1.write("%s %s \n" % ("point8", nobrpt))
        # f1.write("%s %s \n" % ("point8:Number of branch points leading from the main artery (ies)", nobrpt))
         print("point4:Number of arteries entering the vastus medialis from the popliteal", noart)
         print("point8:Number of branch points leading from the main artery (ies)",nobrpt)
      elif k == ord('a'):
         print("completed")
   # close outfile 
   print(xc,yc)
   f1.close()
   # distroy all windows 
   cv2.destroyAllWindows()
import cv2
