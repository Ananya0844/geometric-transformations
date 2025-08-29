# Geometric Transformations Visualizer

**Author:** Ananya S

## Description
This project demonstrates **basic geometric transformations** on a square using Python and NumPy.  
The transformations included are:

- Translation
- Rotation (Euclidean)
- Similarity Transformation (Rotation + Uniform Scaling)
- Affine Transformation (Shear + Non-uniform Scaling)
- Downsampling & Upsampling

The original square is visualized as a **dotted line**, and the transformed square is overlaid in **color** for clear comparison.

---

## Setup & Usage

### 1. Clone the repository
Open your terminal (Mac/Linux) or Command Prompt/PowerShell (Windows), then run:

```bash
git clone https://github.com/Ananya0844/geometric-transformations.git
cd geometric-transformations

### 2. Install Dependencies
pip install numpy matplotlib

### 3. Run the script
python transformations.py

This will open plots showing each transformation on the square.

Original square: dotted (--)

Transformed square: colored

Transformations included:

Translation

Rotation (Euclidean)

Similarity Transform (Rotate + Scale)

Affine Transform (Shear + Scale)

Downsampling & Upsampling

###How It Works

The original square is defined by its four corners.

Matrix operations (translation, rotation, scaling, shear) are applied to transform the square.

Downsampling and upsampling are implemented by multiplying coordinates by a scaling factor (<1 for downsampling, >1 for upsampling).

Matplotlib is used to plot the original and transformed squares on the same axes with grids and equal aspect ratio.

###Project structure
geometric-transformations/
├── README.md
└── transformations.py


