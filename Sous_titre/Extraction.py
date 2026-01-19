import subprocess, os, PGS_en_srt

def ST(chemin_film, id_track_ST, Format_ST, Nom_du_film):

    if Format_ST == "PGS": #si c en PGS
        print(chemin_film, "\n", id_track_ST, "\n", Format_ST, "\n", Nom_du_film)
        #on recup le fichier
        os.makedirs("ST_Recuperes", exist_ok=True)
        CheminFichier = os.path.join("ST_Recuperes", Nom_du_film) + ".sup"
        CheminFichier= os.path.abspath(CheminFichier)
        cmd = ["mkvextract",  chemin_film, "tracks", id_track_ST+":"+ CheminFichier]
        subprocess.run(cmd)

        #on le transforme en srt
        Chemin_Srt = PGS_en_srt.transforme(CheminFichier, Nom_du_film)
        os.makedirs("ST_Generes", exist_ok=True)
        os.rename(Chemin_Srt, os.path.join("ST_Generes", Nom_du_film + "PgsEn.srt") )
        Chemin_Srt = os.path.join("ST_Generes", Nom_du_film + "PgsEn.srt")


    else:   #si c en srt
        os.makedirs("ST_Generes", exist_ok=True)
        Chemin_Srt = "ST_Generes/" + Nom_du_film + ".srt"
        cmd = ["mkvextract",   chemin_film, "tracks", id_track_ST+":"+ Chemin_Srt]
        subprocess.run(cmd)

    return Chemin_Srt
