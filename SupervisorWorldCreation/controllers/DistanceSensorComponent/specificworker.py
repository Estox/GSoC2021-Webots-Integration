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
from rich.console import Console
from genericworker import *

sys.path.append('..')
from webotsapi import *

sys.path.append('/opt/robocomp/lib')
console = Console(highlight=False)


# If RoboComp was compiled with Python bindings you can use InnerModel in Python
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
        console.print('SpecificWorker destructor')

    def setParams(self, params):
        try:
            self.WebotsManager = WebotsAPI()
            self.LaserData = TLaserData()
            
            self.DistanceSensorName = self.WebotsManager.getFromDef("Distance_Sensor")\
            .getField("children").getMFNode(-1).getField("name").getSFString()
            
            self.WebotsManager.enableDevice(self.DistanceSensorName)
            self.TempLaserData = RoboCompLaser.TData()
        except:
            traceback.print_exc()
            print("Error reading config params")
        return True


    @QtCore.Slot()
    def compute(self):
        try:
            self.WebotsManager.simulationStep()
            self.TempLaserData.angle = 0.0
            self.TempLaserData.dist = self.WebotsManager.getDistance(self.DistanceSensorName)
            self.LaserData.append(self.TempLaserData)
        except Ice.Exception as e:
            traceback.print_exc()
            print(e)

        # The API of python-innermodel is not exactly the same as the C++ version
        # self.innermodel.updateTransformValues('head_rot_tilt_pose', 0, 0, 0, 1.3, 0, 0)
        # z = librobocomp_qmat.QVec(3,0)
        # r = self.innermodel.transform('rgbd', z, 'laser')
        # r.printvector('d')
        # print(r[0], r[1], r[2])

        return True

    def startup_check(self):
        QTimer.singleShot(200, QApplication.instance().quit)



    # =============== Methods for Component Implements ==================
    # ===================================================================

    #
    # IMPLEMENTATION of getLaserAndBStateData method from Laser interface
    #
    def Laser_getLaserAndBStateData(self):
        ret = self.LaserData #RoboCompLaser.TLaserData()
        bState = 0
        return [ret, bState]
    #
    # IMPLEMENTATION of getLaserConfData method from Laser interface
    #

    def Laser_getLaserConfData(self):
        ret = RoboCompLaser.LaserConfData()
        return ret
    #
    # IMPLEMENTATION of getLaserData method from Laser interface
    #
    def Laser_getLaserData(self):
        ret = self.LaserData #RoboCompLaser.TLaserData()
        return ret
    # ===================================================================
    # ===================================================================


    ######################
    # From the RoboCompLaser you can use this types:
    # RoboCompLaser.LaserConfData
    # RoboCompLaser.TData
