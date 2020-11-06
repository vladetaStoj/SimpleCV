#Vladeta Stojanovic (vladeta_stojanovic@yahoo.co.uk)
#Version: 200720_01

#Input: PNG image (U8 encoding), with three dots of 1 pixel width, and containing 3 different colors (RGB)
#Output: PNG image with white lines connecting the three RGB dots
#Fail Cases: 1) Less then three dots
#            2) More than three dots
#            3) Dots of a different color apart from red, green and blue 
#            4) Dots are bigger than 1 pixel in size

import cv2
import numpy as np
import argparse

#Allow user to parse in images and set output images
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_image", help = "path to input image")
ap.add_argument("-o", "--output_image", help = "name of output image")
args = vars(ap.parse_args())

img = cv2.imread(args["input_image"],1) #remember the 1 flag for rgb images 

npimage = np.array(img)

#Detect red pixel
red_color = np.array([255,0,0],dtype=np.uint8)
red_pixel = np.where(np.all((npimage==red_color),axis=-1))

print('Red pixel coordintes: ')
print(red_pixel[0], red_pixel[1])

#Detect green pixel
green_color = np.array([0,255,0],dtype=np.uint8)
green_pixel = np.where(np.all((npimage==green_color),axis=-1))

print('Green pixel coordintes: ')
print(green_pixel[0], green_pixel[1])

#Detect blue pixel
blue_color = np.array([0,0,255],dtype=np.uint8)
blue_pixel = np.where(np.all((npimage==blue_color),axis=-1))

print('Blue pixel coordintes: ')
print(blue_pixel[0], blue_pixel[1])

#Draw white lines to connect all detected pixel coordinates and form a triangle
cv2.line(img, (red_pixel[1],red_pixel[0]), (green_pixel[1],green_pixel[0]), (255,255,255), 1)
cv2.line(img, (green_pixel[1],green_pixel[0]), (blue_pixel[1],blue_pixel[0]), (255,255,255), 1)
cv2.line(img, (blue_pixel[1],blue_pixel[0]), (red_pixel[1],red_pixel[0]), (255,255,255), 1)

#Save image
cv2.imwrite(args["output_image"], img) 

#Debug visualization of result (comment out to see triangle)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
