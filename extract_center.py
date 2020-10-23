import sys
import os
import cv2

folders = sys.argv[1:]

for folder in folders:
    output_directory = folder + '_cent'
    if not os.path.isdir(output_directory+'/'):
        os.mkdir(output_directory)
    for image in os.listdir(folder):
        img = cv2.imread(folder + '/' + image, cv2.IMREAD_UNCHANGED)
        cent_x = len(img)//2
        cent_y = len(img[0])//2
        cent_cut = img[cent_x-128:cent_x+128,cent_y-128:cent_y+128]

        cv2.imwrite(output_directory + '/' + image, cent_cut)
