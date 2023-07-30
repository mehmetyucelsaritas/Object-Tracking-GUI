# ----------------------------------------------------------------------------------
# Ghost Fish Tracking Gui  Project - Main Function
# Created on : 22.08.2022
# Author     : Mehmet Yücel Sarıtaş
# Version    : 1.0
# ----------------------------------------------------------------------------------

import pandas as pd
import cv2 as cv
import os
from userinterface import UserInterface   # import UserInterface class from userinterface.py
from browesfileinterface import FileDialog

file_dialog = FileDialog()

# ----------------------------------------------------------------------------------
# MAIN PARAMETERS
# ----------------------------------------------------------------------------------
VIDEO_FPS = 25
video_images = []  # folds all video frames(images) as list
video_format = "avi"
excel_format = "xlsx"

# ----------------------------------------------------------------------------------
# SINGLE FILE ANALYSIS PARAMETERS
# ----------------------------------------------------------------------------------
video_dir_path = file_dialog.filepath[:-4]
video_path = os.path.join(video_dir_path + "." + video_format)
xlsx_path = os.path.join(video_dir_path + "." + excel_format)

# Video Object
cap = cv.VideoCapture(video_path)

# Reading Fish and Cage Coordinates
coordinates_df = pd.read_excel(xlsx_path)  # holds fish and cage coordinates(DataFrame)

# Reading Images to video_images list From Video
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        video_images.append(frame)
    else:
        break
cap.release()

ui = UserInterface(video_images, coordinates_df, video_fps=VIDEO_FPS, xlsx_path=xlsx_path)
ui.initialize_elements()
ui.show_window()
