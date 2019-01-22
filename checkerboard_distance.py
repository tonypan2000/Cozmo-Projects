import asyncio
import sys
import cv2 as cv
import numpy as np
import cozmo

from cozmo.util import degrees, distance_mm

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

try:
    from PIL import ImageDraw, ImageFont, Image, ImageTk
except ImportError:
    sys.exit('run `pip3 install --user Pillow numpy` to run this example')


def cozmo_program(robot: cozmo.robot.Robot):
    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(degrees(0)).wait_for_completed()

    image = robot.world.latest_image.raw_image
    img = np.array(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7, 6), None)
    if ret:
        corners_pos = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        print(corners_pos)
        asyncio.sleep(10)
    cv.destroyAllWindows()


cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
