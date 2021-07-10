import numpy as np
from math import cos, sin, atan2, sqrt, pi
from typing import Sequence

from controller import Supervisor

class RectangleArena(object):
    def __init__(self, name, supervisor):
        super(RectangleArena, self).__init__()
        self.name = name
        self.supervisor = supervisor
        
        floorSize = [3,3]
        floorTileSize = [0.25, 0.25]
        wallHeight = 0.05
        
        base_str = ''.join(open('../../protos/rectangle_arena.wbo', 'r').readlines())
        string = base_str.replace('SEEDNAME', self.name)
        string = string.replace('floorSizeX', str(floorSize[0]))
        string = string.replace('floorSizeY', str(floorSize[1]))
        string = string.replace('floorTileSizeX', str(floorTileSize[0]))
        string = string.replace('floorTileSizeY', str(floorTileSize[1]))
        string = string.replace('wallHeightZ', str(wallHeight))
        
        self.supervisor.rootChildren.importMFNodeFromString(-3, string)
        arena = self.supervisor.getFromDef(self.name)
        
        arena.getField('translation').setSFVec3f([0, 0, 0])
        arena.getField('rotation').setSFRotation([0, 1, 0, 0])
        arena.getField('wallThickness').setSFFloat(0.01)

"""
class Wall(object):
    def __init__(self, name, p1: Sequence[float], p2: Sequence[float], supervisor):
        super(Wall, self).__init__()
        self.p1, self.p2 = p1, p2
        x, z = 0.5 * (p1[0] + p2[0]), 0.5 * (p1[1] + p2[1])
        angle = atan2(p2[1] - p1[1], p2[0] - p1[0])
        self.length = np.linalg.norm(np.array(p2) - np.array(p1))
        self.name = name
        self.supervisor = supervisor
        self.rootChildren = supervisor.getRoot().getField("children")

        base_str = ''.join(open('../../protos/wall_base.wbo', 'r').readlines())
        sy = 1.3  # WALL_HEIGHT (meters)
        sx = self.length  # WALL_LENGTH (meters)
        sz = 0.2  # WALLS_WIDTH (meters)
        y = sy / 2
        string = base_str.replace('SEEDNAME', self.name)
        string = string.replace('SEEDX', str(sx))
        string = string.replace('SEEDY', str(sy))
        string = string.replace('SEEDZ', str(sz))
        self.rootChildren.importMFNodeFromString(-3, string)
        wall = self.supervisor.getFromDef(self.name)
        wall.getField('translation').setSFVec3f([x, y, z])
        wall.getField('rotation').setSFRotation([0, 1, 0, angle])
        wallShapeNode = self.supervisor.getFromDef(self.name + '_SHAPE')
        wallShapeNode.getField('geometry').getSFNode().getField("size").setSFVec3f([sx, sy, sz])
        self.handle = wall

    def get_length(self):
        return self.length

    def get_position(self):
        return self.handle.getPosition()

    def get_orientation(self):
        return self.handle.getOrientation()

    def get_handle(self):
        return self.handle

    def remove(self):
        self.handle.remove()

    def check_collision(self):
        return True if self.handle.getField('boundingObject') is not None else False

    def get_model_bounding_box(self):
        return self.handle.getField('boundingObject')
"""
"""
class Goal(object):
    def __init__(self, x, z, supervisor):
        super(Goal, self).__init__()
        self.x, self.z = x, z
        self.supervisor = supervisor
        self.rootChildren = supervisor.getRoot().getField("children")

        self.rootChildren.importMFNode(-3, '../../protos/goal_base.wbo')
        goal = self.supervisor.getFromDef('GOAL')
        y = goal.getField('translation').getSFVec3f()[1]
        goal.getField('translation').setSFVec3f([self.x, y, self.z])
        self.handle = goal

    def get_position(self):
        return self.handle.getPosition()

    def get_orientation(self):
        return self.handle.getOrientation()

    def get_handle(self):
        return self.handle

    def remove(self):
        self.handle.remove()

    @staticmethod
    def check_collision():
        return False

    @staticmethod
    def get_model_bounding_box():
        return None
"""
"""
class Relation(object):
    def __init__(self, name, node1, node2, supervisor):
        super(Relation, self).__init__()
        self.node1, self.node2 = node1, node2
        p1 = self.node1.get_position()
        p1 = [p1[0], p1[2]]
        p2 = self.node2.get_position()
        p2 = [p2[0], p2[2]]
        self.p1, self.p2 = p1, p2

        x, z = 0.5 * (p1[0] + p2[0]), 0.5 * (p1[1] + p2[1])
        self.length = np.linalg.norm(np.array(p2) - np.array(p1))
        cx = (p2[0] - p1[0]) / self.length
        cz = (p2[1] - p1[1]) / self.length
        if cz != 0:
            za = -cx/cz
            xa = 1
        else:
            za = 1
            xa = 0
        self.name = name
        self.supervisor = supervisor
        self.rootChildren = supervisor.getRoot().getField("children")

        base_str = ''.join(open('../../protos/relation_base.wbo', 'r').readlines())
        sx = self.length
        string = base_str.replace('SEEDNAME', self.name)
        string = string.replace('SEEDX', str(sx))

        self.rootChildren.importMFNodeFromString(-3, string)
        relation = self.supervisor.getFromDef(self.name)
        y = relation.getField('translation').getSFVec3f()[1]
        relation.getField('translation').setSFVec3f([x, y, z])
        relation.getField('rotation').setSFRotation([xa, 0, za, pi/2])

        self.handle = relation

    def get_position(self, relative_to=None):
        return self.handle.get_position(relative_to=relative_to)

    def get_orientation(self, relative_to=None):
        return self.handle.get_orientation(relative_to=relative_to)

    def get_handle(self):
        return self.handle._handle

    def remove(self):
        self.handle.remove()

    def check_collision(self, obj):
        return self.handle.check_collision(obj)

    def get_model_bounding_box(self):
        return self.handle.get_model_bounding_box()

    def move(self):
        p1 = self.node1.get_position()
        p1 = [p1[0], p1[2]]
        p2 = self.node2.get_position()
        p2 = [p2[0], p2[2]]
        self.p1, self.p2 = p1, p2
        x, z = 0.5 * (p1[0] + p2[0]), 0.5 * (p1[1] + p2[1])
        self.length = np.linalg.norm(np.array(p2) - np.array(p1))
        cx = (p2[0] - p1[0]) / self.length
        cz = (p2[1] - p1[1]) / self.length
        if cz != 0:
            za = -cx/cz
            xa = 1
        else:
            za = 1
            xa = 0
        y = self.handle.getField('translation').getSFVec3f()[1]
        self.handle.getField('translation').setSFVec3f([x, y, z])
        self.handle.getField('rotation').setSFRotation([xa, 0, za, pi/2])
        self.handle.getField('children').getMFNode(0).getField('geometry').getSFNode().getField("height").setSFFloat(self.length)
"""
"""
class Human(object):
    def __init__(self, handle):
        super(Human, self).__init__()
        self.handle = handle

    def set_position(self, position):
        x, z = position
        y = self.handle.getField('translation').getSFVec3f()[1]
        self.handle.getField('translation').setSFVec3f([x, y, z])

    def set_orientation(self, angle):
        self.handle.getField('rotation').setSFRotation([0, 1, 0, angle])

    def move(self, command):
        controller_arguments = self.handle.getField('controllerArgs')
        trajectory, speed = command
        generator = [(str(p[0]) + " " + str(p[1])) for p in trajectory]
        trajectory_str = "--trajectory="
        for i in generator:
            trajectory_str += i + ","
        trajectory_str = trajectory_str[:-1]
        controller_arguments.insertMFString(0, trajectory_str)
        controller_arguments.insertMFString(1, "--speed=" + str(speed))

    def stop(self):
        controller_arguments = self.handle.getField('controllerArgs')
        controller_arguments.removeMF(0)
        controller_arguments.removeMF(1)

    def get_position(self):
        return self.handle.getPosition()

    def get_orientation(self):
        return self.handle.getOrientation()

    def get_handle(self):
        return self.handle

    def remove(self):
        self.handle.remove()

    def check_collision(self, obj):
        return True if self.handle.getField('boundingObject') is not None else False

    def get_model_bounding_box(self):
        return self.handle.getField('boundingObject')
"""
"""
class Object(object):
    def __init__(self, name, otype, x, z, angle, supervisor):
        super(Object, self).__init__()
        self.supervisor = supervisor
        self.rootChildren = supervisor.getRoot().getField("children")
        if otype == "desk":
            base_str = ''.join(open('../../protos/desk_base.wbo', 'r').readlines())
        elif otype == "plant":
            base_str = ''.join(open('../../protos/plant_base.wbo', 'r').readlines())
        else:
            print("Not valid object type")
            base_str = None

        string = base_str.replace('SEEDNAME', name)
        self.rootChildren.importMFNodeFromString(-3, string)
        obj = self.supervisor.getFromDef(name)
        obj.getField('translation').setSFVec3f([x, 0, z])
        obj.getField('rotation').setSFRotation([0, 1, 0, angle])

        self.handle = obj

    def get_position(self):
        return self.handle.getPosition()

    def get_orientation(self):
        return self.handle.getOrientation()

    def get_handle(self):
        return self.handle

    def remove(self):
        self.handle.remove()

    def check_collision(self):
        return True if self.handle.getField('boundingObject') is not None else False

    def get_model_bounding_box(self):
        return self.handle.getField('boundingObject')
"""
"""
class TiagoRobot(object):
    def __init__(self, handle):
        super(TiagoRobot, self).__init__()
        self.handle = handle

    def set_position(self, position):
        x, z = position
        y = self.handle.getField('translation').getSFVec3f()[1]
        self.handle.getField('translation').setSFVec3f([x, y, z])

    def set_orientation(self, angle):
        self.handle.getField('rotation').setSFRotation([1, 0, 0, angle])

    def stop(self):
        controller_arguments = self.handle.getField('controllerArgs')
        controller_arguments.removeMF(0)
        controller_arguments.removeMF(1)

    def get_position(self):
        return self.handle.getPosition()

    def get_orientation(self):
        return self.handle.getOrientation()

    def get_handle(self):
        return self.handle

    def remove(self):
        self.handle.remove()

    def check_collision(self, obj):
        return True if self.handle.getField('boundingObject') is not None else False

    def get_model_bounding_box(self):
        return self.handle.getField('boundingObject')
"""
class YoubotRobot(object):
    def __init__(self, handle):
        super(YoubotRobot, self).__init__()
        self.handle = handle
        
    def remove(self):
        self.handle.remove()
        
class WebotsAPI(Supervisor):
    def __init__(self):
        super(WebotsAPI, self).__init__()
        self.rootNode = self.getRoot()
        self.rootChildren = self.rootNode.getField("children")
        self.stepTime = int(self.getBasicTimeStep())
        
    def close(self):
        self.simulationQuit(0)
    
    def simulationStep(self):
        self.step(self.stepTime)
        
    def moveForward(self, speed, wheelsNames):
        wheels = []
        for wheel in range(len(wheelsNames)):
            wheels.append(self.getDevice(wheelsNames[wheel]))
            wheels[wheel].setPosition(float('inf'))
            wheels[wheel].setVelocity(speed)
            
    def create_floor(self, name, size):
        self.rootChildren.importMFNodeFromString(-3, "DEF " + name + " Floor {}")  # Add floor
        floorNode = self.getFromDef(name)
        floorNode.getField('size').setSFVec2f(size)  # Floor size [x ,z] in NUE CS
        floorNode.getField('tileSize').setSFVec2f([2, 2])
        floorNode.getField('appearance').getSFNode().getField("type").setSFString("chequered")
        return floorNode
        
    def remove_objects(self):
        while self.getRoot().getField("children").getMFNode(-3) != self.getRoot().getField("children").getMFNode(2):
            self.getRoot().getField("children").getMFNode(3).remove()
    
    def create_rectangleArena(self, name):
        return RectangleArena(name, self)
        
    def create_robot(self, controller):
        base_str = ''.join(open('../../protos/Youbot.wbo', 'r').readlines())
        string = base_str.replace('void', controller)
        
        self.rootChildren.importMFNodeFromString(-3, string)
        robot_handle = self.getFromDef("ROBOT")
        return YoubotRobot(robot_handle)
"""
    def create_wall(self, name, p1: Sequence[float], p2: Sequence[float]):
        return Wall(name, p1, p2, self)
"""
"""
    def create_goal(self, x, y):
        return Goal(x, y, self)
"""
"""
    def create_relation(self, name, node1, node2):
        return Relation(name, node1, node2, self)
"""
"""
    def create_human(self, name, x, y):
        base_str = ''.join(open('../../protos/pedestrian_base.wbo', 'r').readlines())
        string = base_str.replace('SEEDNAME', name)
        string = string.replace('SEEDX', str(x))
        string = string.replace('SEEDZ', str(y))
        self.rootChildren.importMFNodeFromString(-3, string)
        human_handle = self.getFromDef(name)
        return Human(human_handle)
"""
"""
    def create_object(self, name, otype, x, z, angle):
        return Object(name, otype, x, z, angle, self)
"""
"""
    @staticmethod
    def get_transform_matrix(x: float, y: float, z: float, angle: float):
        rotate_matrix = np.matrix([[cos(angle), -sin(angle), 0., 0.],
                                   [sin(angle), cos(angle), 0., 0.],
                                   [0., 0., 1., 0.],
                                   [0., 0., 0., 1.]])
        translate_matrix = np.matrix([[1., 0., 0., x],
                                      [0., 1., 0., y],
                                      [0., 0., 1., z],
                                      [0., 0., 0., 1.]])
        return (translate_matrix @ rotate_matrix).flatten().tolist()[0]
"""
"""
    @staticmethod
    def get_transformation_matrix(x: float, y: float, angle: float):
        M = np.zeros((3, 3))
        M[0][0], M[0][1], M[0][2] = +cos(angle), -sin(angle), x
        M[1][0], M[1][1], M[1][2] = +sin(angle), +cos(angle), y
        M[2][0], M[2][1], M[2][2] = 0., 0., 1.
        return M
"""
