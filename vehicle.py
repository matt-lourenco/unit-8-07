# Created on 22 Nov 2016
# Created by: Matthew Lourenco
# This is a class that defines a generic vehicle
# Edited on: 28 Nov 2016
# Fixed bug that prevents it from working in python 2.7
# Edited on: 1 Dec 2016
# gave functionality to setters other than just changing the numbers
# Edited on: 5 Dec 2016
# created constructors

from numpy import random

class Vehicle:
    #This is a class that creates a generic vehicle
    
    def __init__(self, colour, license_plate_number = '', number_of_wheels = 4):
        #private fields
        
        self.__license_plate_number = 'AAAA000'
        self.__colour = 'white'
        self.__number_of_doors = 4
        self.__speed = 20.0
        self.__gear = 1
        self.__number_of_wheels = 4
        self.__number_of_tires = 4
        
        self.set_colour(colour)
        self.set_license_plate_number(license_plate_number)
        self.__set_number_of_wheels(number_of_wheels)
        print('\n')
    
    # properties
    
    def get_license_plate_number(self):
        #get the license plate number property
        return self.__license_plate_number
    
    def set_license_plate_number(self, new_license_plate_number):
        #set the license plate number property
        if not len(new_license_plate_number) == 7:
            # license plate should not be set
            self.__randomize_license_plate_number()
            print('License plate number must be 7 characters long. New license will be randomized.')
        else:
            self.__license_plate_number = new_license_plate_number
        print('License plate number: ' + str(self.__license_plate_number))
    
    def get_colour(self):
        #get the colour property
        return self.__colour
    
    def set_colour(self, new_colour):
        #set the colour property
        if new_colour == 'nil':
            #Nothing should change
            pass
        else:
            self.__colour = new_colour
        print('Paint colour: ' + str(self.__colour))
    
    def get_number_of_doors(self):
        #get the number of doors property
        return self.__number_of_doors
    
    def get_speed(self):
        #get the speed property
        return self.__speed
    
    def get_gear(self):
        #get the gear property
        return self.__gear
    
    def set_gear(self, new_gear):
        #set the gear property
        if new_gear < 1 or new_gear > 6:
            # nothing happens because this gear is invalid
            pass
        else:
            self.__gear = new_gear
            self.__speed_recalculate()
        print('Gear: ' + str(self.__gear))
        print('Speed: ' + str(self.__speed) + 'km/h')
    
    def get_number_of_wheels(self):
        #get the number of wheels
        return self.__number_of_wheels
    
    def get_number_of_tires(self):
        #get the number of tires
        return self.__number_of_tires
    
    #private methods
    def __speed_recalculate(self):
        #Calculates the speed
        self.__speed = self.__gear * 20
    
    def __set_number_of_wheels(self, new_number_of_wheels):
        #private set the number of wheels
        if new_number_of_wheels == 2:
            self.__number_of_wheels = 2
            self.__number_of_tires = 2
            self.__number_of_doors = 0
            print('This is a 2 wheeled vehicle')
        else:
            self.__number_of_wheels = 4
            self.__number_of_tires = 4
            print('This is a 4 wheeled vehicle')
    
    def __randomize_license_plate_number(self):
        #Randomizes the license plate if nothing is inputted
        element = 0
        string = ''
        for character in range(0, 7):
            element = random.randint(55, 91)
            if element < 65:
                element = str(element - 55)
            else:
                element = str(unichr(element))
            string = string + element
        self.__license_plate_number = string
    
    #public methods
    def brake(self, speed_decrease):
        #decreases the speed
        if speed_decrease < 0:
            #Nothing should happen
            pass
        elif speed_decrease > self.__speed:
            self.__speed = 0
        else:
            self.__speed = self.__speed - speed_decrease
        print('Speed: ' + str(self.__speed) + 'km/h')
