
from ggrocket import Rocket, Planet

earth = Planet (viewscale=0.0005)
rocket = Rocket(earth, altitude=400000, velocity=1000, timezoom=1)
earth.run(rocket)