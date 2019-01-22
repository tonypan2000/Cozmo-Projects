'''Make Cozmo drive in a square.

This script combines the two previous examples (02_drive_and_turn.py and
03_count.py) to make Cozmo drive in a square by going forward and turning
left 4 times in a row.
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    # Use a "for loop" to repeat the indented code 4 times
    # Note: the _ variable name can be used when you don't need the value
    for _ in range(4):
        robot.drive_straight(distance_mm(320), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()


cozmo.run_program(cozmo_program)
