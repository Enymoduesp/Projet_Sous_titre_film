import subprocess

def transforme(Chemin_PGS, Nom_du_film):
    #le PGS est sous la forme "ST_Recuperes/" + Nom_du_film + ".sup"
    cmd = ["pgsrip", Chemin_PGS]
    subprocess.run(cmd) #genere le fichier au meme endroit et remplace .sup en srt

    chemin_srt = Chemin_PGS.replace(".sup", ".srt")
    return chemin_srt