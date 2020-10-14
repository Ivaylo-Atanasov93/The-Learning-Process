from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    @abstractmethod
    def sensors_count(self):
        pass

class Android(Robot):

    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.sensor = 4

    def sensors_count(self):
        return self.sensor


class Chappie(Robot):

    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self.sensor = 6

    def sensors_count(self):
        return self.sensor


def count_robot_sensors(robots: list):
    for robot in robots:
        print(robot.sensors_count())


robots = [Android('Robocop'), Chappie('XIX')]
count_robot_sensors(robots)

#--------------Initial Code---------------
# Problem:
# 3.	Robots
# Refactor the provided code, so it is in line with the Liskov Substitution Principle.
# Define a method in the parent class. The subclasses should implement the method, so it
# returns the count of sensors for each type of robot.


# class Robot:
#     def __init__(self, type):
#         self.type = type
#
#     def get_type(self):
#         return self.type
#
#
# class Android(Robot):
#     def android_senzors_count(self):
#         return 4
#
#
# class Chappie(Robot):
#     def chappie_senzors_count(self):
#         return 6
#
#
# def count_robot_senzors(robots: list):
#     for robot in robots:
#         if isinstance(robot, Android):
#             print(robot.android_senzors_count())
#         elif isinstance(robot, Chappie):
#             print(robot.chappie_senzors_count())
#
#
# robots = [Android('Robocop'), Chappie('XIX')]
# count_robot_senzors(robots)
