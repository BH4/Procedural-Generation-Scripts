from L_System import L_System
from draw import L_system_image

rules = dict()
rules['X'] = 'F-[[X]+X]+F[+FX]-X'  # reflection
rules['F'] = 'FF'
plant = L_System('X', rules)

s = plant.get_step(6)

im = L_system_image(dist=2, angle=25)
im.draw(s)
