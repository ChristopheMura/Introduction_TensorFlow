import os
import shutil

# Chemin vers le répertoire contenant les images
repertoire_images = "/Users/christophemura/Documents/Git/Introduction_TensorFlow/Datasets/Trains/train"

# Parcourir tous les fichiers dans le répertoire
for filename in os.listdir(repertoire_images):
    if filename.endswith(".png"):
        # Séparer le nom du fichier en utilisant le séparateur "_"
        parts = filename.split("_")
        if len(parts) >= 2:
            # La catégorie est la deuxième partie du nom du fichier
            categorie = parts[1]

            # Créer le dossier de la catégorie s'il n'existe pas
            dossier_categorie = os.path.join(repertoire_images, categorie)
            if not os.path.exists(dossier_categorie):
                os.makedirs(dossier_categorie)

            # Déplacer le fichier vers le dossier de la catégorie
            ancien_chemin = os.path.join(repertoire_images, filename)
            nouveau_chemin = os.path.join(dossier_categorie, filename)
            shutil.move(ancien_chemin, nouveau_chemin)
            print(f"Image {filename} déplacée vers {dossier_categorie}")
        else:
            print(f"Le fichier {filename} n'a pas le bon format de nom.")
    else:
        print(f"Ignorer le fichier {filename}, n'est pas une image.")

print("Terminé !")