import consts as c

class Drone (object):
    def __init__(self, x=0, y=0, z=0, xVelocity=0, yVelocity=0, zVelocity=0):
        self.x = x
        self.y = y
        self.z = z
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.zVelocity = zVelocity

    def getCurrentXVelocity(self):
        return self.xVelocity

    def getCurrentYVelocity(self):
        return self.yVelocity

    def getCurrentZVelocity(self):
        return self.zVelocity
    
    def updateXVelocity(self):
        self.xVelocity = self.xVelocity + c.xAccelleration

    def updateYVelocity(self):
        self.yVelocity = self.yVelocity + c.yAccelleration

    def updateZVelocity(self):
        self.zVelocity = self.zVelocity + c.zAccelleration

    def step(self):
        self.x += self.xVelocity
        self.y += self.yVelocity
        self.z += self.zVelocity
        self.updateXVelocity()
        self.updateYVelocity()
        self.updateZVelocity()

    def get_position(self):
        return (self.x, self.y, self.z)
    