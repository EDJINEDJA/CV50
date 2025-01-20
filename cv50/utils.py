import os
import numpy as np

WORKDIR  = os.getcwd()

kernels = {
    "Augmentation de contraste": np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]]), 
    "Détection de bords (Sobel)": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
    "Flou gaussien": np.array([[1/16, 2/16, 1/16], [2/16, 4/16, 2/16], [1/16, 2/16, 1/16]]),
    "Flou moyen": np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]),
    "Détection de bords (Prewitt)": np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]),
    "Moyenne pondérée (dilatation)": np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
    "Laplacien": np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
}