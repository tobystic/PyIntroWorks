import os
import re
import os.path

fragment = 1

userUrl = input("Lien de l'extrait: \n")
usernbFrag  = int(input("Nombre de Fragments a télécharger: \n"))
userNameFile = input("Nom du fichier fini: \n")

os.remove("list.txt")
os.system("touch list.txt")
os.system("rm *.ts")
# Ouvrir le fichier en mode append
with open("list.txt", "a") as fd:
    while fragment != usernbFrag:
        # Télécharger le fragment avec wget
        url = re.sub(r'frag\((\d+)\)', f'frag({fragment})', userUrl)
        os.system(f"wget -O 'fragment_{fragment}.ts' '{url}'")
        
        # Ajouter le nom du fichier à "list.txt"
        fd.write(f"file 'fragment_{fragment}.ts'\n")
        
        fragment += 1

# Concaténer les fragments en un seul fichier vidéo
os.system(f"ffmpeg -f concat -safe 0 -i list.txt -c copy {userNameFile}.mp4")