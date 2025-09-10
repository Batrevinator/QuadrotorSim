import numpy as np
import matplotlib as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Example data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    z = np.sin(np.sqrt(x**2 + y**2))

    ax.plot3D(x, y, z, 'blue')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Plot Example')

    plt.show()

if __name__ == "__main__":
    main()