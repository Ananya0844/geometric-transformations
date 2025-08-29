import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import zoom  # for upsampling and downsampling

# -------------------------------
# 1. Define the original square
# -------------------------------
square = np.array([
    [50, 50],
    [150, 50],
    [150, 150],
    [50, 150],
    [50, 50]  # close the loop
])

# Function to plot square
def plot_square(square_coords, title="Square", color='b', label='Transformed'):
    plt.figure(figsize=(5,5))
    plt.plot(square_coords[:,0], square_coords[:,1], color+'-', linewidth=2, label=label)
    plt.plot(square[:,0], square[:,1], 'k--', linewidth=1, label='Original')  # dotted original
    plt.xlim(0, 200)
    plt.ylim(0, 200)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.show()

plot_square(square, title="Original Square")

# -------------------------------
# 2. Translation
# -------------------------------
tx, ty = 30, 20
translated = square + np.array([tx, ty])
plot_square(translated, title="Translation", color='r')

# -------------------------------
# 3. Rotation (Euclidean)
# -------------------------------
theta = np.deg2rad(45)
center = np.array([100, 100])  # rotate about center
rotated = np.dot(square - center, np.array([[np.cos(theta), -np.sin(theta)],
                                            [np.sin(theta),  np.cos(theta)]])) + center
plot_square(rotated, title="Rotation (45°)", color='g')

# -------------------------------
# 4. Similarity (Rotation + Uniform Scaling)
# -------------------------------
scale = 1.5
theta = np.deg2rad(30)
similarity = np.dot(square - center, np.array([[scale*np.cos(theta), -scale*np.sin(theta)],
                                               [scale*np.sin(theta),  scale*np.cos(theta)]])) + center
plot_square(similarity, title="Similarity Transform (Rotate+Scale)", color='m')

# -------------------------------
# 5. Affine Transformation (Shear + Scale)
# -------------------------------
M_affine = np.array([
    [1.2, 0.5, 0],  # a,b,tx
    [0.3, 1.1, 0],  # c,d,ty
])
square_h = np.hstack([square[:4], np.ones((4,1))])  # homogeneous coords
affine = (M_affine @ square_h.T).T
affine = np.vstack([affine, affine[0]])  # close the loop
plot_square(affine, title="Affine Transform (Shear+Scale)", color='c')

# -------------------------------
# 6. Downsampling (reduce size by factor 2)
# -------------------------------
downsample_factor = 0.5  # 50% size
downsampled = square[:4] * downsample_factor
downsampled = np.vstack([downsampled, downsampled[0]])  # close loop
plot_square(downsampled, title="Downsampled (Factor 0.5)", color='y')

# -------------------------------
# 7. Upsampling (enlarge by factor 2)
# -------------------------------
upsample_factor = 2.0
upsampled = square[:4] * upsample_factor
upsampled = np.vstack([upsampled, upsampled[0]])  # close loop
plot_square(upsampled, title="Upsampled (Factor 2)", color='m')
