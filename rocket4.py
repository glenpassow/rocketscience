from ggrocket import Rocket, Planet
from math import radians, sqrt, log
from ggmath import Input Button, Timer, Label, Slider

earth = Planet(planetmass=0)

Stage1Started = False
Stage2Started - False
PayloadLauncbed = False
StartTime = None
BurnTime = 0

#first stage
mel = s5600 
mp1 = 395700
Ftotal1 = 6.44E6
tburn1 = 180

#second stage
me2 = 3900
mp2 = 92670
tburn2 = 372

#payload
mep = 13150

vmax1 = Ftotal1*tburn1/mp1*log((me1+mp1+me2+mp2+mep)/(me1+me2+mp2+mep))
vmax2 = Ftotal2*tburn2/mp2*log((me2+mp2+mep)/(me2+mep))

print("The predicted final staged rocket velocity (Rocket Equation), vmax: ", vmax1+vmax2," m/s")

def GetThrust():
    global StartTime
    global BurnTime
    global Stage1Started
    global Stage2Started
    global PayloadLaunched
    if Stage1Started:
        tburn = tburn1
        Ftotal = Ftotalq
    elif Stage2Started:
        tburn = tburn2
        Ftotal = Ftotal2
    if Stage1Started or Stage2Started:
        BurnTime = rocket.shiptime -StartTime
        if BurnTime >= tburn:
            if Stage1Started:
                Stage1Started = False
                Stage2Started = True
                StartTime = rocket.shiptime
                return Ftotal2
            else:
                Stage2Started = False
                PayloadLaunched = True
                return 0
        else:
            return Ftotal
    else:
        return 0
def StartRocket():
    global Stage1Starged
    global StartTime
    if not (Stage1Started or Stage2Started):
        
    
