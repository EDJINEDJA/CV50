import cv2
import os
from pathlib import Path
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

from cv50.utils import WORKDIR, kernels

def kernel(kernels: dict):
    """
    Affiche chaque noyau (kernel) contenu dans le dictionnaire `kernels` comme une image 
    avec un titre correspondant au nom du noyau.

    Cette fonction prend un dictionnaire de noyaux de convolution, où chaque clé est le nom du noyau
    et chaque valeur est la matrice du noyau. Chaque noyau est affiché dans une fenêtre avec un titre 
    représentant le nom du noyau, et l'image est affichée en niveaux de gris.

    Paramètres:
    - kernels (dict) : Un dictionnaire où les clés sont des chaînes de caractères représentant 
      les noms des noyaux, et les valeurs sont des matrices de convolution (ndarray) à afficher 
      sous forme d'images. Les matrices doivent être des tableaux 2D de type `numpy.array` ou similaires.

    Exemple:
    >>> kernels = {
    >>>     "Sobel Horizontal": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
    >>>     "Sobel Vertical": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    >>> }
    >>> kernel(kernels)

    Cette fonction crée une figure pour chaque noyau, l'affiche en niveaux de gris et supprime 
    les axes pour une meilleure visibilité de la matrice du noyau.
    """
    for name, image in kernels.items():

        plt.figure(figsize=(8,8))

        plt.imshow(image, cmap='gray')

        plt.title(label=f"kernel: {name}")

        plt.axis("off")

        plt.show()



def con2D(kernel: str, imageName: Path, kernels: dict):
    """
    Applique un noyau de convolution sur une image et affiche l'image originale 
    ainsi que l'image filtrée (après convolution) dans des fenêtres séparées.

    Cette fonction prend un nom de noyau sous forme de chaîne de caractères, 
    charge une image à partir d'un chemin donné, applique une opération de 
    convolution à l'aide du noyau spécifié et affiche à la fois l'image originale 
    et l'image filtrée.

    Paramètres:
    - kernel (str) : Le nom du noyau de convolution à utiliser, qui doit être 
      une clé valide dans le dictionnaire `kernels`.
    - imageName (Path) : Le nom de l'image à traiter, donné sous forme de chemin 
      relatif ou absolu. L'image est chargée depuis le répertoire `WORKDIR` 
      et son chemin complet est construit à l'aide de `imageName`.
    - kernels (dict) : Un dictionnaire de noyaux de convolution où chaque clé 
      est le nom d'un noyau (chaîne de caractères) et chaque valeur est une 
      matrice de noyau (tableau `numpy.ndarray`) utilisée pour appliquer la 
      convolution sur l'image.

    Effets secondaires:
    - Affiche deux fenêtres avec OpenCV :
        1. L'image originale avec ses dimensions (`W * H * C`).
        2. L'image résultante après application de la convolution avec le noyau spécifié, 
           accompagnée de ses dimensions (`W1 * H1 * C1`).
    
    Exemple d'utilisation:
    >>> kernels = {
    >>>     "Sobel": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
    >>>     "Gaussian": np.array([[1/16, 2/16, 1/16], [2/16, 4/16, 2/16], [1/16, 2/16, 1/16]])
    >>> }
    >>> con2D("Sobel", Path("image.png"), kernels)

    La fonction attend un chemin d'image valide et un noyau qui existe dans le dictionnaire `kernels`.
    """
    imagePath = Path(os.path.join(WORKDIR, imageName))

    # Chargement de l'image depuis le chemin spécifié
    image = cv2.imread(imagePath)

    # Récupérer les dimensions de l'image originale
    W, H, C = image.shape
    
    # Appliquer la convolution avec le noyau spécifié
    imgFiltered = cv2.filter2D(image, -1, kernels[kernel])

    # Récupérer les dimensions de l'image filtrée
    W1, H1, C1 = imgFiltered.shape

    # Affichage des images avec OpenCV
    cv2.imshow(f"Marie size : {W} * {H} * {C}", image)
    cv2.imshow(f'Convolved with Kernel:{kernel} size : {W1} * {H1} * {C1}', imgFiltered)

    # Attente d'une touche pour fermer les fenêtres
    cv2.waitKey(0)
    cv2.destroyAllWindows()

   

if __name__ == "__main__":

    #Afficher les noyaux de convolution

    # kernel(kernels)


    #Afficher les images obtenues après la convolution

    imageName = "inputs/ex.jpg"

    imagePath = Path(os.path.join(WORKDIR, imageName))


    # Chargement de l'image depuis le chemin spécifié
    image = cv2.imread(imagePath)

    print(image.flatten().astype(np.float32))

    # kernel = {1: "Détection de bords (Sobel)",2: "Augmentation de contraste",
    #           3: "Flou gaussien",4: "Détection de bords (Prewitt)", 4: "Moyenne pondérée (dilatation)", 5: "Laplacien" }
    # type = 3
    # con2D(kernel[type], imageName, kernels)