import os
import numpy as np
import matplotlib.pyplot as plt

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

def afficher_structure(repertoire, niveau=0, max_fichiers=2):
    """Affiche récursivement la structure du répertoire avec indentation en limitant à max_fichiers"""
    try:
        # Liste tous les fichiers et dossiers dans le répertoire
        contenu = os.listdir(repertoire)

        # Séparer les fichiers des dossiers
        fichiers = [item for item in contenu if os.path.isfile(os.path.join(repertoire, item))]
        dossiers = [item for item in contenu if os.path.isdir(os.path.join(repertoire, item))]

        # Trier les fichiers par date de modification (le plus récent en premier)
        fichiers.sort(key=lambda x: os.path.getmtime(os.path.join(repertoire, x)), reverse=True)

        # Limiter aux max_fichiers plus récents
        fichiers = fichiers[:max_fichiers]

        # Afficher les dossiers
        for dossier in dossiers:
            print(" " * niveau * 2 + f"📂 {dossier}")
            afficher_structure(os.path.join(repertoire, dossier), niveau + 1, max_fichiers)

        # Afficher les fichiers (seulement les deux plus récents)
        for fichier in fichiers:
            print(" " * niveau * 2 + f"📄 {fichier}")
    
    except PermissionError:
        print("Permission refusée pour", repertoire)
