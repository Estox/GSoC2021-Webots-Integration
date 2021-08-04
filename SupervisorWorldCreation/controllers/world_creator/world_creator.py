import sys, os
sys.path.append('..')
from webotsapi import *
import math
import time


class SceneCreator(WebotsAPI):
    def __init__(self):
        super(SceneCreator, self).__init__()

        self.rootNode = self.getRoot()
        self.rootChildren = self.rootNode.getField("children")
        self.robotNode = None
        self.arenaNode = None
        self.boxNodes = []
        self.peopleNodes = []
        self.objectsNodes = []
        self.relationNodes = []

    def create_scene(self):
        self.arenaNode = self.create_rectangleArena("arena")
        self.robotNode = self.create_robot("Ribbit", "void")
        
        translationCameraDevice = [0.255, 0.1, 0]
        rotationCameraDevice = [0, 1, 0, -1.5708]
        self.robotNode.addDevice("Camera", "camera", translationCameraDevice, rotationCameraDevice)
        #self.robotNode.addDevice("Distance_sensor", "DS", translationCameraDevice, rotationCameraDevice,)
        translationLidarSensor = [0.255, 0, 0]
        rotationLidarSensor = [0, 1, 0, -1.5708]
        self.robotNode.addDevice("Lidar", "lidar", translationLidarSensor, rotationLidarSensor)
        size = [0.3, 0.3, 0.3]
        translation1, translation2, translation3, translation4 = [0.7, 0.15, -0.75], [-0.64, 0.15, -0.5],\
        [0.75, 0.15, 0.68],  [-0.89, 0.15, 0.7]
        self.boxNodes.append(self.create_box("B1", translation1, size))
        self.boxNodes.append(self.create_box("B2", translation2, size))
        self.boxNodes.append(self.create_box("B3", translation3, size))
        self.boxNodes.append(self.create_box("B4", translation4, size))
"""
        self.wallNodes.append(self.create_wall("W1", [8, 8], [8, -8]))
        self.wallNodes.append(self.create_wall("W2", [8, -8], [-8, -8]))
        self.wallNodes.append(self.create_wall("W3", [-8, -8], [-8, 8]))
        self.wallNodes.append(self.create_wall("W4", [-8, 8], [8, 8]))

        self.peopleNodes.append(self.create_human("P1", -5, -5))
        command = ([[-5, -5], [-5, 4]], 2)
        self.peopleNodes[0].move(command)

        self.peopleNodes.append(self.create_human("P2", -6.5, -5))
        command = ([[-6.5, -5], [-6.5, 4]], 1)
        self.peopleNodes[1].move(command)

        self.peopleNodes.append(self.create_human("P3", 2, 0.82))
        self.peopleNodes[2].set_orientation(0)

        self.goalNode = self.create_goal(-1.5, -4.5)

        self.objectsNodes.append(self.create_object("O1", "desk", 2, 3, math.pi/2))
        self.objectsNodes.append(self.create_object("O2", "plant", 4.2, -4.2, math.pi / 2))
        self.objectsNodes.append(self.create_object("O3", "plant", -6, -4.2, math.pi / 2))

        self.relationNodes.append(self.create_relation("R1", self.peopleNodes[2], self.objectsNodes[0]))
        self.relationNodes.append(self.create_relation("R2", self.peopleNodes[0], self.peopleNodes[1]))

        
        self.robotNode.set_position([5, 5])
"""

simulation = SceneCreator()
simulation.remove_objects()
simulation.create_scene()

while simulation.simulationStep() != -1:
    simulation.simulationStep()