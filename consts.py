import math


# X,Y,Z inertial plane based on X facing "forward", y facing "left" and z facing "up"

droneMass = 1
gravitationalConstant = 9.8
thrustCoefficient = 1
momentOfInertia = 1
motorCenterOfMassLength = 6

# These will not be constant eventually
# Orientation about drone facing away from us:
# Top left motor
motorOneRotationalVelocity = 1
# Top right motor
motorTwoRotationalVelocity = 1
# Bottom left motor
motorThreeRotationalVelocity = 1
# Bottom right motor
motorFourRotationalVelocity = 1

initialXVelocity = 0
initialYVelocity = 0
initialZVelocity = 0

phi = 0 # angular rotation in degrees about ex "roll"
theta = 0 # angular rotation in degrees about ey "pitch"
psi = 0 # angular rotation in degrees about ez "yaw"

F1 = (thrustCoefficient)*(motorOneRotationalVelocity)
F2 = (thrustCoefficient)*(motorTwoRotationalVelocity)
F3 = (thrustCoefficient)*(motorThreeRotationalVelocity)
F4 = (thrustCoefficient)*(motorFourRotationalVelocity)

forces = [F1, F2, F3, F4]

u1 = sum(forces)
uPhi = (F2+F4)-(F1 + F3)
uTheta = (F1 + F2)-(F3+F4)

# This will work for a 2d drone for now
xAccelleration = -u1/droneMass*math.cos(phi)
yAccelleration = u1/droneMass*math.sin(phi)-gravitationalConstant
phiAccelleration = uPhi/momentOfInertia*motorCenterOfMassLength
thetaAccelleration = uTheta/momentOfInertia*motorCenterOfMassLength
