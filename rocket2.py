from ggrocket import Rocket, Planet
from math import radians

earth = Planet()
rocket = Rocket(earth, heading=radians(90),directiond=90, velocity=20)
earth.run(rocket)