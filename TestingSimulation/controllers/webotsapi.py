from controller import Supervisor
from controller import Node

class WebotsAPI(Supervisor, Node):
    def __init__(self):
        super(WebotsAPI, self).__init__()
        #self.rootNode = self.getRoot()
        #self.rootChildren = self.rootNode.getField("children")
        self.stepTime = int(self.getBasicTimeStep())
        
    def simulationStep(self):
        self.step(self.stepTime)
        
    def enableDevice(self, name):
        device = self.getDevice(name)
        device.enable(self.stepTime)
        
    def getDistance(self, name):
        distanceSensor = self.getDevice(name)
        return distanceSensor.getValue()
    
    def getImage(self, name):
        camera = self.getDevice(name)
        return camera.getImage()
            
    def moveForward(self, speed, wheelsNames):
        wheels = []
        for wheel in range(len(wheelsNames)):
            wheels.append(self.getDevice(wheelsNames[wheel]))
            wheels[wheel].setPosition(float('inf'))
            wheels[wheel].setVelocity(speed)

    def close(self):
        self.simulationQuit(0)
        
