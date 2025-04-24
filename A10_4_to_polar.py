import numpy as np

def cartesian_to_polar(points):
    r = np.sqrt(points[:, 0]**2 + points[:, 1]**2)  # Radius
    theta = np.arctan2(points[:, 1], points[:, 0])  # Angle in radians
    return np.column_stack((r, theta))

def main():
    N = 10  # Change this to any value >= 10
    cartesian_points = np.random.uniform(-10, 10, (N, 2))  # Generate N random 2D points
    print("Cartesian Coordinates:")
    print(cartesian_points)
    
    polar_points = cartesian_to_polar(cartesian_points)
    print("\nPolar Coordinates:")
    print(polar_points)

if __name__ == "__main__":
    main()
