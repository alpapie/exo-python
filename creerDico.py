#!/usr/bin/env python
#-*- coding:utf8 -*-

import itertools
import os
import sys
import optparse
import gzip


# Symboles possibles que pourraient contenir nos mots de passe
# On aura le choix de composition de nos mots de passe
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'
ISEP='ISEPisep@#&/'
SIGNS = '@#$&%*+'
COMPLEX_SIGN = '!"\'(),-./:;<=>?[\\]^_`{|}~'

Chains = {'full': LETTERS + LETTERS.upper() + NUMBERS + SIGNS + COMPLEX_SIGN,
          'simple': LETTERS + LETTERS.upper(),
          'alphanum': LETTERS + LETTERS.upper() + NUMBERS,
          'complex': LETTERS + LETTERS.upper() + SIGNS + COMPLEX_SIGN,
          'chif':NUMBERS,
          'isep':NUMBERS + ISEP}


def tabPass(chaine, longueur):
    conteneur = []
    listeMots = []

    # Génération des mots de taille 1 à longueur
    # for i in range(longueur + 1):
    autoGenrator = list(itertools.product(chaine, repeat=longueur))
    for elts in autoGenrator:
        conteneur.append(elts)

    # Récuperation et concaténation des tuples générés,
    # le premier tuple est vide, il ne nous interresse pas
    for mot in conteneur[1:]:
        chaineCaracteres =""
        mot = list(mot)
        for parts in mot:
            chaineCaracteres += parts
        listeMots.append(chaineCaracteres)

    return listeMots


# Compression au format Tar.gz, cela reduira la taille du dictionnaire
def makeGzipFile(fichInitial):
    # Récuperation du chemin du fichier crée
    filePath = os.path.abspath(fichInitial)
    fichFinal = filePath + '.gz'  # Nom du fichier final

    # Ouverture du fichier initial.
    with open(fichInitial, "rb") as fileIn:
        # Ouverture du fichier final
        with gzip.open(fichFinal, "wb") as fileOut:
            # Write output.
            fileOut.writelines(fileIn)


# Fonction qui formattera la chaine en enlevant
# les caractères non désirés si renseignés
def formatChain(chaine, caracteres):
    tabChain = list(chaine)

    # Vérification de la presence de chaque caractère non voulus
    # dans la chaîne qui sera retournée pour traitement
    for elts in caracteres:
        if elts in tabChain:
            tabChain.remove(elts)

    # Chaîne formattée sur laquelle se portera le traitement...
    clearChain = "".join(tabChain)
    return clearChain


# Vérification de la validite du type defini
def checkType(args):
    if args in Chains.keys():
        return Chains[args]
    else:
        sys.exit("Le type choisi n'est pas défini... Arrêt !")


# Vérification de la longueur saisie en parametres
def checkLength(args):
    # La fonction isdigit() peut etre remplacée par isnumeric()
    # pour la version 3 de python
    if args.isdigit():
        return args
    else:
        sys.exit("La longueur définie n'est pas conforme... Arrêt !")
# Patientez...l'opération peut prendre plusieurs minutes...

# Verification de l'existence du fichier pour eviter d'ecraser
def checkFile(args):
    if os.path.exists(args):
        print("Le fichier existe... Voulez-vous l'ecraser ?")
        answer = input()
        if answer.lower().startswith('n'):
            sys.exit("Arrêt du programme...")
        elif answer.lower().startswith('o') or answer.lower().startswith('y'):
            return args
        else:
            sys.exit("Réponse incorrecte... Arrêt du programme!")
    else:
        return args


def main():
    # Description et recuperation des arguments passés au programme
    parser = optparse.OptionParser()
    # parser.add_option(
    #     '-t', dest='strCom', type='string', help='type of passwords')
    # parser.add_option('-l', dest='passLength', type='string',
    #                   help='length of password')
    # parser.add_option('-d', dest='dico', type='string',
    #                   help='path of file where write on')
    # parser.add_option('-r', dest='rmChar', type='string',
    #                   help='removable characters separated by (,)')
    # (options, args) = parser.parse_args()

    # # Vérification d'existence des paramètres nécessaires
    # if (options.strCom is None) | (options.passLength is None)\
    #         | (options.dico is None):
    #     Usage()
    # else:
        # Vérification de validité des paramètres
    rmChar = None
    strCom = checkType("chif")
    passLength = int(checkLength('8'))
    dico = checkFile('./mot_de_passe.txt')

    # Petite Manip pour recupérer enfin notre chaîne à traiter
    if rmChar is None:
        chaineFinale = strCom
    else:
        chaineFinale = formatChain(strCom, rmChar.split(","))

    # Juste un petit message pour aider à patienter
    print("Patientez...l'opération peut prendre plusieurs minutes...")

    # Génération de notre Tableau de Password
    monTableau = tabPass(chaineFinale, passLength)

    # Ecriture dans le fichier
    with open(dico, 'w') as fichierDico:
        for elts in monTableau:
            fichierDico.write(elts + '\n')

    # Compression du Dictionnaire généré!
    # On peut Commenter la ligne si on veut pas que le fichier
    # soit compressé, du coup on commentera la ligne suivante
    makeGzipFile(dico)

    # Suppression du fichier crée...
    os.remove(dico)

    # Tout s'est bien déroulé on peut enfin sortir !
    print("Votre Dictionnaire à bien été généré. Merci !")


def Usage():
    print("#################################################################")
    print("###############   Dictionary Generator   ########################")
    print("#################################################################")
    print("-----------------------------------------------------------------")
    print("Usage :")
    print("-----------------------------------------------------------------")
    print("%prog -t <type of words> -l <length of word> "
          "-d <file destination> -r <not be in word>")
    print("")
    print("Options :")
    print("-t full : for all characters...")
    print("-t simple : for letters(upper and lower) only...")
    print("-t alphanum : for letters(upper and lower) and numbers...")
    print("-t complex : for letters(upper and lower) and signs...")
    print("-l length : for words length...")
    print("-d file_full_path : for writing to a file...")
    print("-r caracters which not be in words, separated by coma(,) ... it's "
          "facultative ! ")


# Lancement du programme !
if __name__ == '__main__':
    main()
