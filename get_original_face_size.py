import sys
import json
import os
import cv2

alignment_json = sys.argv[1] #should be used on outputfile of get_alignments.py(in modified faceswap repo), which is run after running faceswap extraction
input_folder =  sys.argv[2] #input folder that corresponds with the alignment_json files, required so the original image can be opened
output_folder = sys.argv[3]

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

with open(alignment_json) as f:
  alignment_dict = json.load(f)

for file in alignment_dict:
    img = cv2.imread(input_folder + '/' + file)
    x = alignment_dict[file]['x']
    y = alignment_dict[file]['y']
    w = alignment_dict[file]['w']
    h = alignment_dict[file]['h']

    img = img[y:y+h,x:x+w]
    cv2.imwrite(output_folder + '/' + file, img)
