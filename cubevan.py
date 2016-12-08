# Created by: Matthew Lourenco
# Created on: 8 Dec 2016
# This is a child class of the vehicle program

from vehicle import *

class Cubevan(Vehicle):
    # This is a child class of the vehicle program
    
    def __init__(self, colour, license_plate_number = ''):
        #import init from Vehicle
        Vehicle.__init__(self, colour, license_plate_number = '')
        #Read only fields
        self.__volume = 400
    
    def get_volume(self):
        # setter for volume property
        return self.__volume
