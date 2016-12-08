# Created on 22 Nov 2016
# Created by: Matthew Lourenco
# This is a program that creates a custom vehicle
# Edited on: 28 Nov 2016
# Fixed bug that prevents it from working in python 2.7
# Edited on: 1 Dec 2016
# gave functionality to setters other than just changing the numbers
# Edited on: 5 Dec 2016
# created constructors

from vehicle import *
from cubevan import *

#create a vehicle
car1 = Vehicle('blue', '', 2)
car2 = Cubevan('red', 'ABCD908')

print('Car 1:')
print('Paint colour: ' + str(car1.get_colour()))
print('License plate number: ' + str(car1.get_license_plate_number()))
car1.set_license_plate_number('7letter')
print('Speed: ' + str(car1.get_speed()) + 'km/h')
car1.set_gear(3)
car1.set_gear(5)
car1.set_gear(7)
car1.brake(50)
car1.brake(100)

print('\nCar 2:')
print('Paint colour: ' + str(car2.get_colour()))
print('License plate number: ' + str(car2.get_license_plate_number()))
car2.set_license_plate_number('7letter')
car2.set_license_plate_number('7things')
car2.set_colour('nil')
car2.set_license_plate_number('8letters')
car2.set_colour('green')
print('Trunk space: ' + str(car2.get_volume()) + ' cubic feet')
