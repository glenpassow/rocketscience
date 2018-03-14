from ggrocket import Rocket, Planet
from math import radians, sqrt
from ggmath import Slider

earth = Planet(viewscale = 0.00005)

#Constants relating to Earth and physics
Re = 6.371E6 #Earth radius in meters
Me = 5.972E24 #Earth mass in kg
G = 6.674E-11 #Gravitational constant

#Moon stuff
Rm = 1.737E6
Mm = 7.35E22

#escape velocity moon
Vm = sqrt(2*Mm*G/Rm)
print("Predicted moon escape velocity is ", Vm," m/s")

#escape velocity earth
Ve = sqrt(2*Me*G/Re)
print("Predicted earth escape velocity is ", Ve," m/s")

#Slider for the timezoom
tz = Slider((10,400), 0, 5, 0, positioning="physical")

rocket = Rocket(earth, heading=radians(90),directiond=90, velocity=Ve, timezoom=tz)
earth.run(rocket)