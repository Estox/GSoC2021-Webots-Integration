#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2021 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication
from genericworker import *

sys.path.append('..')
from webotsapi import *

# If RoboComp was compiled with Python bindings you can use InnerModel in Python
sys.path.append('/opt/robocomp/lib')
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel

class SpecificWorker(GenericWorker, WebotsAPI):
    def __init__(self, proxy_map, startup_check=False):
        super(SpecificWorker, self).__init__(proxy_map)
        
        if startup_check:
            self.startup_check()
        else:
            self.timer.timeout.connect(self.compute)
            self.timer.start(self.Period)

    def __del__(self):
        print('SpecificWorker destructor')

    def setParams(self, params):
        try:
            self.WebotsManager = WebotsAPI()
            self.wheelsNames = ['wheel_left_joint', 'wheel_right_joint']
            self.wheelsSolidNames = ['LEFT_WHEEL', 'RIGHT_WHEEL']
            self.wheelTranslation = []
            for wheel in self.wheelsSolidNames:
                self.wheelTranslation.append(self.WebotsManager.getFromDef(wheel)\
                .getField('translation').getSFVec3f())
            self.wheelRadius = self.WebotsManager.getFromDef('WHEEL_SOLID').getField('radius').getSFFloat()
            self.wheelParameters = [self.wheelsNames, self.wheelTranslation, self.wheelRadius]
        except:
            traceback.print_exc()
            print("Error reading config params")
        return True


    @QtCore.Slot()
    def compute(self):
        try:
            self.WebotsManager.simulationStep()
            self.DifferentialRobot_setSpeedBase(0.4, 1.0)
        except Ice.Exception as e:
            traceback.print_exc()
            print(e)
        return True

    def startup_check(self):
        QTimer.singleShot(200, QApplication.instance().quit)



    # =============== Methods for Component Implements ==================
    # ===================================================================

    #
    # IMPLEMENTATION of correctOdometer method from DifferentialRobot interface
    #
    def DifferentialRobot_correctOdometer(self, x, z, alpha):
    
        #
        # write your CODE here
        #
        pass


    #
    # IMPLEMENTATION of getBasePose method from DifferentialRobot interface
    #
    def DifferentialRobot_getBasePose(self):
    
        #
        # write your CODE here
        #
            return [x, z, alpha]
    #
    # IMPLEMENTATION of getBaseState method from DifferentialRobot interface
    #
    def DifferentialRobot_getBaseState(self):
    
        #
        # write your CODE here
        #
        state = RoboCompGenericBase.TBaseState()
        return state
    #
    # IMPLEMENTATION of resetOdometer method from DifferentialRobot interface
    #
    def DifferentialRobot_resetOdometer(self):
    
        #
        # write your CODE here
        #
        pass


    #
    # IMPLEMENTATION of setOdometer method from DifferentialRobot interface
    #
    def DifferentialRobot_setOdometer(self, state):
    
        #
        # write your CODE here
        #
        pass


    #
    # IMPLEMENTATION of setOdometerPose method from DifferentialRobot interface
    #
    def DifferentialRobot_setOdometerPose(self, x, z, alpha):
    
        #
        # write your CODE here
        #
        pass


    #
    # IMPLEMENTATION of setSpeedBase method from DifferentialRobot interface
    #
    def DifferentialRobot_setSpeedBase(self, adv, rot):
        self.WebotsManager.differentialMovement(adv, rot, self.wheelParameters)
        pass


    #
    # IMPLEMENTATION of stopBase method from DifferentialRobot interface
    #
    def DifferentialRobot_stopBase(self):
    
        #
        # write your CODE here
        #
        pass


    # ===================================================================
    # ===================================================================


    ######################
    # From the RoboCompDifferentialRobot you can use this types:
    # RoboCompDifferentialRobot.TMechParams
