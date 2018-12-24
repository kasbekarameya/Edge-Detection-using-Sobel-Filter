import numpy as np
import cv2

#read in image
img = cv2.imread('D:/University at Buffalo/Computer Vision & Image Processing/Projects/Project 1/images/task1.png', 0)

#create kernel filters
sobely = np.asarray([(-1,0,1),
                     (-2,0,2),
                     (-1,0,1)])
sobelx = np.asarray([(-1,-2,-1),
                     (0,0,0),
                     (1,2,1)])


l, h = sobely.shape
for i in range(0,l):
	for j in range(0,h-1):
		temp = sobely[i][j]
		sobely[i][j] = sobely[i][h-j-1]
		sobely[i][h-j-1] = temp
	
for i in range(0,l-1):
	for j in range(0,h):
		temp = sobely[i][j]
		sobely[i][j] = sobely[l-i-1][j]
		sobely[l-i-1][j] = temp

l, h = sobelx.shape
for i in range(0,l):
	for j in range(0,h-1):
		temp = sobelx[i][j]
		sobelx[i][j] = sobelx[i][h-j-1]
		sobelx[i][h-j-1] = temp

for i in range(0,l-1):
	for j in range(0,h):
		temp = sobelx[i][j]
		sobelx[i][j] = sobelx[l-i-1][j]
		sobelx[l-i-1][j] = temp

#Using Convolution with Sobel Filter 
#cv2.imshow('original_image.png', img)
#cv2.waitKey(0)
Gx = img
Gx = np.asarray([[0 for j in i] for i in Gx])
Gy = img
Gy = np.asarray([[0 for j in i] for i in Gy])
pstimg = img
pstimg = np.asarray([[0 for j in i] for i in pstimg])

size = pstimg.shape
for i in range(1, size[0] - 1):
    for j in range(1, size[1] - 1):
        gx = (sobelx[0][0]*img[i - 1][j - 1] + sobelx[0][1]*img[i][j - 1] + sobelx[0][2]*img[i + 1][j - 1] + sobelx[2][0]*img[i - 1][j + 1] + sobelx[2][1]*img[i][j + 1] + sobelx[2][2]*img[i + 1][j + 1])
        gy = (img[i - 1][j - 1] + 2*img[i - 1][j] + img[i - 1][j + 1]) - (img[i + 1][j - 1] + 2*img[i + 1][j] + img[i + 1][j + 1])
        
        Gx[i-1][j-1]=gx
        Gy[i-1][j-1]=gy
        pstimg[i][j] = min(255, (gx*gx + gy*gy)**0.5)
  
#cv2.imwrite("Ximg.png",Gx)
#cv2.imwrite("Yimg.png",Gy)
#cv2.imwrite("Post_image.png",pstimg)

#Eliminate zero values for X

maxx = Gx[0][0]
for i in Gx:
	for j in i:
		if(maxx < j):
			maxx = j
minx = Gx[0][0]
for i in Gx:
	for j in i:
		if(minx > j):
			minx = j			
			
nonzgx = Gx
nonzgx = np.asarray([[0 for j in i] for i in nonzgx])
nonzgx = (Gx - minx) / (maxx - minx)
#cv2.imwrite("Non_zero_Ximage.jpg",nonzgx)
cv2.imshow('Non_zero_Ximage.jpg',nonzgx)
#cv2.waitKey(0)

#Eliminate zero values for Y
maxy = Gy[0][0]
for i in Gy:
	for j in i:
		if(maxy < j):
			maxy = j
miny = Gy[0][0]
for i in Gy:
	for j in i:
		if(miny > j):
			miny = j			
			
nonzgy = Gy
nonzgy = np.asarray([[0 for j in i] for i in nonzgy])
nonzgy = (Gy - miny) / (maxy - miny)
#cv2.imwrite("Non_zero_Yimage.jpg",nonzgy)
cv2.imshow('Non_zero_Yimage.jpg',nonzgy)
cv2.waitKey(0)
