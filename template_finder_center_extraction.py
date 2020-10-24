#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import sys

template_folder = sys.argv[1] #Folder extracted faces from get_original_face_size.py
image_folders = sys.argv[2]#Folder with original file names
output_dir = sys.argv[3] # puts the bounding box images in this directory
cropped_dir = sys.argv[4] #crops images and save here

translation_factor_x = int(sys.argv[5])
translation_factor_y = int(sys.argv[6]) #used to ensure that a true 256x256 square is captured and is not cut out of the image

def extract_face(template_path: str, base_image_path: str, output_dir: str, output_name: str):

    img_rgb = cv2.imread(base_image_path)
    clean = cv2.imread(base_image_path)
    img_rgb = cv2.copyMakeBorder(img_rgb, 300,300,300,300,cv2.BORDER_CONSTANT, value=(0,0,0))
    clean = cv2.copyMakeBorder(clean, 300,300,300,300,cv2.BORDER_CONSTANT, value=(0,0,0))
    template = cv2.imread(template_path)
    height, width = template.shape[0], template.shape[1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_SQDIFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = min_loc  #Change to max_loc for all except for TM_SQDIFF
    bottom_right = (top_left[0] + width, top_left[1] + height)

    center = (top_left[0] + width//2, top_left[1] + height//2)

    top_left_256 = (center[0]-128 + translation_factor_x ,center[1]-128 + translation_factor_y)
    bottom_right_256 = (center[0]+128 + translation_factor_x, center[1]+128 + translation_factor_y)

    #cv2.rectangle(img_rgb, top_left, bottom_right, (255, 0, 0), 2)
    cv2.rectangle(img_rgb, top_left_256, bottom_right_256, (255, 0, 0), 2)
    cv2.imwrite( output_dir + '/' + original_name, img_rgb)
    cropped = clean[top_left_256[1]:top_left_256[1]+256, top_left_256[0]:top_left_256[0]+256]
    print(top_left_256[1],top_left_256[1]+256, top_left_256[0],top_left_256[0]+256)
    cv2.imwrite(cropped_dir+'/' + original_name, cropped)

if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
if not os.path.isdir(cropped_dir):
    os.mkdir(cropped_dir)

for temp_name in os.listdir(template_folder):
    # #temp_name is of form {original_file_name}_0.png
    # suffix_index = temp_name.find('_0.png')
    # original_name = temp_name[:suffix_index] + '.png'
    original_name = temp_name
    extract_face(template_folder + '/' + temp_name, image_folders + '/' + original_name, output_dir, original_name)



# %%
