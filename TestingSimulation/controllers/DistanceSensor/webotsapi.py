from controller import Supervisor
from controller import Node

class WebotsAPI(Supervisor, Node):
    def __init__(self):
        super(WebotsAPI, self).__init__()
        self.rootNode = self.getRoot()
        self.rootChildren = self.rootNode.getField("children")
        self.stepTime = int(self.getBasicTimeStep())
        
    def simulationStep(self):
        self.step(self.stepTime)
        
    def enableDistanceSensor(self):
        distanceSensor = self.getDevice("ds_center")
        distanceSensor.enable(self.stepTime)
        
    def getDistance(self):
        distanceSensor = self.getDevice("ds_center")
        return distanceSensor.getValue()
        
    def moveForward(self, speed):
        wheels = []
        wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
        for i in range(4):
            wheels.append(self.getDevice(wheelsNames[i]))
            wheels[i].setPosition(float('inf'))
            wheels[i].setVelocity(speed)

    def close(self):
        self.simulationQuit(0)
        
