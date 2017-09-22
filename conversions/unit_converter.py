# unit conversion API

'''
Class: distance
Input: distance in meters
Functions:
    m_to_in -> outputs distance in inches
    m_to_ft -> outputs distance in feet

'''
class distance:
    def __init__(self, x):
        self.x = x

    def m_to_in(self):
        if self.x is None:
            return (self.x)
        else:
            return (self.x * 39.3701)

    def m_to_ft(self):
        if self.x is None:
            return (self.x)
        else:
            return (self.x * 3.28084)


'''
Class: speed
Input: speed in meters per second
Functions:
    mps_to_mph -> outputs speed in miles per hour
    mps_to_fps -> outputs speed in feet per second

'''
class speed:
    def __init__(self, x):
        self.x = x

    def mps_to_mph(self):
        if self.x is None:
            return (self.x)
        else:
            return (self.x * 2.23694)

    def mps_to_fps(self):
        if self.x is None:
            return (self.x)
        else:
            return (self.x * 3.28084)


'''
Class: acceleration
Input: acceleration in meters per second squared
Functions: 
    ms2_to_fs2 -> outputs acceleration in feet per second squared

'''
class acceleration:
    def __init__(self, x):
        self.x = x

    def ms2_to_fs2(self):
        if self.x is None:
            return (self.x)
        else:
            return (self.x * 3.2808399)

'''
Class: angle
Input: angle in radiants
Functions:
    rad_to_deg -> outputs angle in degrees
    m_to_ft -> outputs distance in feet

'''
class angle:
    def __init__(self, x):
        self.x = x

    def rad_to_deg(self):
        if self.x is None:
            return (self.x)
        else:
            return (self.x * 57.2958)


'''
Class: rotation
Input: rotation in revolutions per second
Functions:
    rps_to_rpm -> outputs rotation in revolutions per minute


'''
class rotation:
    def __init__(self, x):
        self.x = x

    def rps_to_rpm(self):
        if self.x is None:
            return (self.x)
        else:
            return(self.x * 60)
