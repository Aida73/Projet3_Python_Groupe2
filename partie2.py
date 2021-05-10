import os

#Question1:

"""
On va créé une fonction qui nous permettra de compter
l'ensemble des commentaires multilignes.Et on va soustraire cela pour
avoir le nombre exact de lignes de code.
NB: On a utilisé le package dic2021

"""
def liste_comm(liste):
    comments = []
    comm = [i for i, v in enumerate(liste) if v=='"""']
    for i, j in enumerate(range(0, len(comm), 2)):
        for k in range(comm[j], comm[j+1]+1):
            comments.append(liste[k])
    return len(comments)


def count_lign(module):
    for path, dirs, files in os.walk("Projet3_FG_AS/dic2021"):
        for filename in files:
            if filename == module:
                file = open(f"{path}/{filename}")
                file1 = file.read().splitlines()
                for i in range(0,3):
                    for elt in file1:
                        if (elt == '' or elt.startswith('#')):
                            file1.remove(elt)
                file.close()
    return len(file1)-liste_comm(file1)



def get_modules(chemin):
    list_modules=[]
    for module in os.listdir(chemin):
        if module.endswith(".py"):
            liste_modules.append(module)
    return liste_modules
#get_modules("Projet3_FG_AS/dic2021")



def get_packages(chemin):
    liste_packages=[]
    for dossier in os.listdir(chemin):
        if not dossier.endswith(".py"):
            liste_packages.append(dossier)
    return liste_packages
#get_packages("Projet3_FG_AS/dic2021")



def get_all_modules(chemin):
    list_all_modules=[]
    for path, dirs, files in os.walk(chemin):
        list_all_modules.extend(get_modules(path))     
    return list_all_modules
#get_all_modules("Projet3_FG_AS/dic2021")


def count_all_lign(chemin):
    return (sum([count_lign(file) for file in get_all_modules(chemin)]))   
#count_all_lign("Projet3_FG_AS/dic2021")












