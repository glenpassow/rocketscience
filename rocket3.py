from ggrocket import Rocket, Planet
from math import radians, sqrt, log
from ggmath import InputButton, Timer

earth = Planet(planetmass=0)

RocketStarted = False
StartTime = None
BurnTime = 0

#Rocket Specs
me = 25600
mp = 395700
F1D = 716000

N1D = 9

Ftotal = F1D*N1D
tburn = 180

vmax = Ftotal*tburn/(me+mp)
print("Predicted final velocity (Newson't 2nd Las), vmax: " vmax, "m/s")

def GetThrust():
    global RocketStarted
    if RocketStarted:
        BurnTime = rocket.shiptime - StartTime
        if BurnTime >= tburn:
            RocketStarted = False
            return 0
        else:
            return Ftotal
    else:
        return 0
        
def StartRocket():
    global RocketStarted
