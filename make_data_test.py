import glob, os
import cv2
# create file train.txt and text.txt
# path_data is folder contain images
# percentage test is a percentage of images to be used for the test set
import shutil 

# Directory where the data will reside, relative to 'darknet.exe'
path = '/data1/huyen/YOLO/darknet/'
path_data = 'data/Coin/'
path_save = 'test_precision/txt/'



with open('test.txt', 'r') as f:
  for line in f:
    print(path + line)
    #img = cv2.imread(path + line[:-1],0)
    source = path + line[:-5] + ".txt"
    destination = path_save + line[10:-5] + ".txt"
    #print(img)
    #img_save = cv2.imwrite(path_save + line[10:-1],img)
    dest = shutil.copyfile(source, destination) 