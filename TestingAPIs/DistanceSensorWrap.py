from controller import DistanceSensor

class DistanceSensor(DistanceSensor):
    def __init__(self, lookupTable, type, numberOfRays, aperture, gaussianWidth, resolution):
        self.lookupTable = lookupTable
        self.type = type
        self.numberOfRays = numberOfRays
        self.aperture = aperture
        self.gaussianWidth = gaussianWidth
        self.resolution = resolution

    def enable(self, samplingPeriod):
        return self.DistanceSensor.wb_distance_sensor_enable()

    def disable(self):
        return self.DistanceSensor.wb_distance_sensor_disable()

    def getSamplingPeriod(self):
        return self.DistanceSensor.wb_distance_sensor_get_sampling_period()

    def getValue(self):
        return self.DistanceSensor.wb_distance_sensor_get_value()

    def getMaxValue(self):
        return self.DistanceSensor.wb_distance_sensor_get_max_value()

    def getMinValue(self):
        return self.DistanceSensor.wb_distance_sensor_get_min_value()

    def getAperture(self):
        return self.DistanceSensor.wb_distance_sensor_get_aperture()

    def getLookupTable(self):
        return self.DistanceSensor.wb_distance_sensor_get_lookup_table()

    def getType(self):
        #GENERIC, INFRA_RED, SONAR, LASER
        return self.DistanceSensor.wb_distance_sensor_get_type()
