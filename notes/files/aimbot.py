import math
from scipy.optimize import fsolve

#Given the position of a target together with the launch velocity and gravity of a projectile, this returns the requires pitch (in degrees as seen in the F3 menu) needed to hit the target

#SETTINGS (default for hitting block 100 blocks away with bow):
v = 1.5 #launch velocity of projectile
g = 0.03 #gravity of projectile
y = 0 #relative vertical position of target
r = 50 #relative horizontal position of target

#CONSTANTS:
h = 1.52 #height of player
a = 0.01 #air resistance

def phi_func(phi):
    rad = math.pi/180*phi
    return (h-y)+g/a**2*math.log(1-a/(v*math.cos(rad))*r)+((g-a*v*math.sin(rad))/(a*v*math.cos(rad)))*r

print(fsolve(phi_func, 0)[0])