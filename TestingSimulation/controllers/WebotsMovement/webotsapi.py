from controller import Supervisor
from controller import Node

class WebotsAPI(Supervisor, Node):
    def __init__(self):
        super(WebotsAPI, self).__init__()
        self.rootNode = self.getRoot()
        self.rootChildren = self.rootNode.getField("children")
        self.DSDevice = self.getDevice("ds_center")
        self.stepTime = int(self.getBasicTimeStep())
        
    def stepSimulation(self):
        self.step(self.stepTime)
        
    def enableDS(self):
        self.DSDevice.enable(self.stepTime)
        
    def getDistance(self):
        return self.DSDevice.getValue()
        
    def moveForward(self):
        wheels = []
        wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
        for i in range(4):
            wheels.append(self.getDevice(wheelsNames[i]))
            wheels[i].setPosition(float('inf'))
            wheels[i].setVelocity(1.0)

    def close(self):
        self.simulationQuit(0)
        
