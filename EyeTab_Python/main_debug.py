import cv2
import moviepy.editor as mpy
import numpy as np
import os
import socket
import gaze_system as gaze_system
import device_constants
from datetime import datetime


vid_path = r"C:\Users\amitaid\Documents\private\studies\gaze_track\data\videos\VID_20170921_161601186.avi"

use_network_stream = False
use_webcam = False
use_local_video = not (use_network_stream or use_webcam)

debug = False
recording = False

marker_flags_ms = [3500] + [x for x in range(7500, 50000, 4000)]

device_control_socket = None
stream_open = False

video = mpy.VideoFileClip(vid_path)

#
# For managing marker movement
#
if use_local_video:
    active_marker_ind = 0

device = device_constants.Device(
    device_constants.WEBCAM if use_webcam else device_constants.NEXUS_7_INV
)

g_sys = gaze_system.GazeSystem(device, debug, recording)

for frame in video.iter_frames():
    #frame = np.rot90(frame, device.rot90s)
    frame = frame[..., ::-1]
    gaze_pt = g_sys.get_gaze_from_frame(frame)

    key = cv2.waitKey(5)
