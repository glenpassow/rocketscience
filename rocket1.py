
from ggrocket import Rocket, Planet

earth = Planet (viewscale=0.0005, color=0Xff0000)
rocket = Rocket(earth, altitude=2000000, velocity=6900, timezoom=3)
earth.run(rocket)