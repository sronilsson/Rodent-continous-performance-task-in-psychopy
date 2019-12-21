from scipy import ndimage, misc
import numpy as np
import os
import cv2
folder_contrast = 100
image_contrast = 0
x = 0

contrast_change = 1.27     # 1.27 = generates stimuli 100 stimuli groups at 1% iterations
stimuli_format = ".jpg"

while x < 100:
    folder_contrast = (folder_contrast - 1)
    folder_path = ('/Directory of stimuli files/')
    save_path = ('/Stimuli_') + str(folder_contrast) + str('/')
    folder = folder_path + save_path
    if not os.path.exists(folder):
        os.mkdir(folder)
    image_contrast = (image_contrast - contrast_change)
    x = x + 1
    for filename in os.listdir(folder_path):
        if filename.__contains__(stimuli_format):
            img = cv2.imread(filename)
            img = np.int16(img)
            img = img * (image_contrast / 127 + 1) - image_contrast
            img = np.clip(img, 0, 255)
            img = np.uint8(img)
            save_img_as = folder + filename
            cv2.imwrite(save_img_as, img)
