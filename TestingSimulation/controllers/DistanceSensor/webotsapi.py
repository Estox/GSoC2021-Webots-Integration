from controller import Supervisor

class WebotsAPI(Supervisor):
    def __init__(self):
        super(WebotsAPI, self).__init__()
        self.rootNode = self.getRobot()
        self.rootChildren = self.rootNode.getField("children")

    def close(self):
        self.simulationQuit(0)
