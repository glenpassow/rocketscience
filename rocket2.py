from ggrocket import Rocket, Planet
from math import radians, sqrt

earth = Planet()

#Constants relating to Earth and physics
Re = 6.371E6 #Earth radius in meters
Me = 5.972E24 #Earth mass in kg
G = 6.674E-11 #Gravitational constant

#escape velocity
Ve = sqrt(2*Me*G/Re
print("Predicted escape velocity is ", Ve," m/s")

rocket = Rocket(earth, heading=radians(90),directiond=90, velocity=20)
earth.run(rocket)