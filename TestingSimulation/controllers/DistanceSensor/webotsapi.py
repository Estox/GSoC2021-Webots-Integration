from controller import Supervisor
from controller import Node

class WebotsAPI(Supervisor, Node):
    def __init__(self):
        super(WebotsAPI, self).__init__()
        self.rootNode = self.getRoot()
        self.rootChildren = self.rootNode.getField("children")
        self.DSDevice = self.getDevice("ds_center")
        
    def EnableDS(self, step_time):
        self.DSDevice.enable(step_time)
        return 0
        
    def DistanceCall(self):
        return self.DSDevice.getValue()
        
    def close(self):
        self.simulationQuit(0)
