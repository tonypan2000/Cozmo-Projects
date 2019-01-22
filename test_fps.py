import datetime
import sys
import cv2 as cv
import numpy as np
import cozmo

from cozmo.util import degrees
try:
    from PIL import ImageDraw, ImageFont, Image, ImageTk
except ImportError:
    sys.exit('run `pip3 install --user Pillow numpy` to run this example')


def cozmo_program(robot: cozmo.robot.Robot):
    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(degrees(0)).wait_for_completed()
    start_time = datetime.datetime.now()
    count = 0
    prev_img = robot.world.latest_image.raw_image
    while (datetime.datetime.now() - start_time).seconds < 1:
        #print(datetime.datetime.now())
        image = robot.world.latest_image.raw_image
        if prev_img != image:
            prev_img = image;
            raw_rgb_conv = cv.cvtColor(np.array(image), cv.COLOR_BGR2RGB)
            #cv.imwrite('test.png', raw_rgb_conv)
            count = count + 1
            #print(count)
    print(count)


cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
