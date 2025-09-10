import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import consts as c
import drone

drone = drone.Drone(c.initialXPosition, c.initialYPosition, c.initialZPosition)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x_coord = c.initialXPosition
y_coord = c.initialYPosition
z_coord = c.initialZPosition

point, = ax.plot(x_coord, y_coord, z_coord, marker='o', markersize=8)

ax.set_xlim([-1000, 1000])
ax.set_ylim([-1000, 1000])
ax.set_zlim([-1000, 1000])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Quadrotor')
xVelocityText = plt.figtext(0.8, 0.5, "xVelocity: \n" + str(drone.getCurrentXVelocity()), rotation=0, verticalalignment='center')
yVelocityText = plt.figtext(0.8, 0.4, "yVelocity: \n" + str(drone.getCurrentYVelocity()), rotation=0, verticalalignment='center')
zVelocityText = plt.figtext(0.8, 0.3, "zVelocity: \n" + str(drone.getCurrentZVelocity()), rotation=0, verticalalignment='center')


def update(frames):
    drone.step()  # Move the drone
    x_coord, y_coord, z_coord = drone.get_position()
    point.set_data([x_coord], [y_coord])
    point.set_3d_properties([z_coord])
    xVelocityText.set_text("xVelocity: " + str(drone.getCurrentXVelocity()))
    yVelocityText.set_text("yVelocity: " + str(drone.getCurrentYVelocity()))
    zVelocityText.set_text("zVelocity: " + str(drone.getCurrentZVelocity()))
    return point,

animation = animation.FuncAnimation(fig, update, frames=100, interval=1000)

plt.show()