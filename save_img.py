import cv2 as cv
import numpy as np
import cozmo
from cozmo.util import degrees


def cozmo_program(robot: cozmo.robot.Robot):
    robot.move_lift(-3)
    robot.set_head_angle(degrees(0)).wait_for_completed()
    image = robot.world.latest_image.raw_image
    img = np.array(image)
    cv.imwrite('test.jpg', img)


cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
