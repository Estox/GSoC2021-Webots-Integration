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
        self.goalNode = None
        self.floorNodes = []
        self.wallNodes = []
        self.peopleNodes = []
        self.objectsNodes = []
        self.relationNodes = []

    def create_scene(self):
        floorSize = [16, 16]
        self.floorNodes.append(self.create_floor("F1", floorSize))
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

        self.robotNode = self.create_robot()
        self.robotNode.set_position([5, 5])


"""
simulation = SceneCreator()
simulation.remove_objects()
simulation.create_scene()

while simulation.simulationStep() != -1:
    simulation.simulationStep()
