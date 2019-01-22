"""
Determines whether current environment is rectangular using edge detection:

1. drives forward until it sees an edge while keeping track of distance
2. try turning, then dry forward
3. repeat four times
4. check for properties of a rectangle
5. Cozmo says what environment it is in
"""

import asyncio
import time
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

'''
#dimensions = {0: distance_mm(0), 1: distance_mm(0), 2: distance_mm(0), 3: distance_mm(0)}
dimensions = [0, 0, 0, 0]
'''


def cozmo_program(robot: cozmo.robot.Robot):
    "robot.enable_stop_on_cliff(True)"
    clockwise = True
    for edge in range(4):
        while not robot.is_cliff_detected:
            robot.drive_wheel_motors(50.0, 50.0, l_wheel_acc=0, r_wheel_acc=0)
        robot.stop_all_motors()
        #dimensions[edge] = distance_mm()#
        "back up"
        time.sleep(0.5)
        robot.drive_straight(distance_mm(-20), speed_mmps(50)).wait_for_completed()
        if clockwise:
            "Check left turn"
            robot.turn_in_place(degrees(90)).wait_for_completed()
            time.sleep(0.5)
            robot.drive_straight(distance_mm(10), speed_mmps(50)).wait_for_completed()
            "left side is edge"
            if robot.is_cliff_detected:
                "back up"
                time.sleep(0.5)
                robot.drive_straight(distance_mm(-10), speed_mmps(50)).wait_for_completed()
                robot.turn_in_place(degrees(-180)).wait_for_completed()
                time.sleep(0.5)
                robot.drive_straight(distance_mm(10), speed_mmps(50)).wait_for_completed()
                if robot.is_cliff_detected:
                    break
                else:
                    clockwise = False
        else:
            robot.turn_in_place(degrees(-90)).wait_for_completed()
            time.sleep(0.5)
            robot.drive_straight(distance_mm(10), speed_mmps(50)).wait_for_completed()
            "left side is edge"
            if robot.is_cliff_detected:
                break
    "checking the dimensions to determine whether it is a rectangle"
    '''print(dimensions[0])
    print(dimensions[1])
    print(dimensions[2])
    print(dimensions[3])
    if dimensions[2] - dimensions[0] <= distance_mm(25) and dimensions[3] - dimensions[1] <= distance_mm(25):
    '''
    robot.say_text("The environment is a rectangle").wait_for_completed()


cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)
