import subprocess, fileinput

#On fais en sorte que à chaque ligne, le premier "Default" soit remplacé par FR ou ENG selon ce à quoi il appartient pour que le style soit bien associé
#Dialogue: 0,0:00:28.27,0:00:32.06,Default,,0,0,0,,MOSFILM --> Dialogue: 0,0:00:28.27,0:00:32.06, FR,...
#avec donc Style: Default,Arial,--> Style: FR,Arial,..
def Associer_Style(chemin_ass, langue):   #langue = langue à inserer plutot que default
    for ligne in fileinput.input(chemin_ass, inplace=True):
        ligne = ligne.replace('Default', langue, 1) #on remplace tous les premier Default de chaque ligne par le nouveau blaz
        print(ligne, end='')


def Fusionner_ST(chemin_ass1, chemin_ass2): #met le style du deuxieme juste après le premier puis tous les ST du ass2 à la fin
    Associer_Style(chemin_ass1, "FR")
    Associer_Style(chemin_ass2, "ENG")
    dialogue2=[]
    iciBis = -1

    for ligne2 in fileinput.input(chemin_ass2, "r"):
        if ligne2.startswith('Style'):
            Style2 = ligne2 #on recup la ligne style du fichier 2
        if iciBis == 1:  # on recopie tout mtn
            dialogue2.append(ligne2)
        if iciBis == 0:  # dans une ligne
            iciBis = 1
        if ligne2.startswith('[Events]'):  # dans 2 lignes
            iciBis = 0

    ici = 0
    for ligne1 in fileinput.input(chemin_ass1, inplace=True):
        if  ici == 1:
            print(Style2, end='') #on ecrit le style du fichier 2
            ici = 2
        if ici == 0 and ligne1.startswith('Style'): ##si on est sur le premier style de la ligne
           ici = 1 #le prochain sera le style 2
        if ici == 4: #il faut réécrire tout les dialogues ici
            for ligne2 in dialogue2:
                print(ligne2, end='')
            ici = -1
        if ici == 3:
            ici = 4 #on est sur la ligne format après event
        if ligne1.startswith('[Events]'):
            ici = 3 # dans 2 ligne on ecrit les dialogues du fichiers 2.
        print(ligne1, end='') #on réecrit la ligne


