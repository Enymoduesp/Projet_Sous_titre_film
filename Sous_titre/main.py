import lire_mkv, Imdb, Resync, telecharge_ST, Extraction, ass_manip
from pymediainfo import MediaInfo

cheminfilm = input("chemin du MKV : ")

Nom_du_film, Annee_du_film, Fps, Id_track_ST_en, Format_ST_en, Id_track_ST_fr, Format_ST_fr = lire_mkv.recupTitreEtSTEtFps(cheminfilm)

Id_Imdb = Imdb.recup_Id(Nom_du_film, Annee_du_film)


while True:
    choix = int(input("1--> Je veux les sous titres FR \n 2 --> Je veux les sous titres EN et FR en dessous \n 3--> Je veux"
                  "les sous titres EN et la traduction des mots + compliqués en dessous\n  Mon choix : "))
    if choix >0 and choix <4:
        break

match choix:
    case 1:
        print("génération du sous titre Fr prêt à l'emploie")
        nomduST = Nom_du_film + "_STFR"
        Chemin_STFR = telecharge_ST.DL_ST(nomduST + "_avSync", Fps, "fr" , Id_Imdb)
        if Id_track_ST_en is not None:      #si ya des ST originaux en anglaison sync avec, sinon avec l'audio
            Chemin_STENG = Extraction.ST(cheminfilm, Id_track_ST_en, Format_ST_en, Nom_du_film)
            ST_final = Resync.ST_STREF(Chemin_STENG, Chemin_STFR, nomduST)
        else:   #si yen a pas...
            ST_final = Resync.ST_NOREF(cheminfilm, Chemin_STFR, nomduST)
        print(ST_final)
    case 2:
        print("Génération du sous titre Fr et anglais en dessous")

        """Partie en RECUP ST ENG"""
        if Id_track_ST_en is not None:
            Chemin_STENG = Extraction.ST(cheminfilm, Id_track_ST_en, Format_ST_en, Nom_du_film) #si ya des ST originaux on les recup sinon Opensub
        else:
            nomduST = Nom_du_film + "_STENG"
            Chemin_STENG = telecharge_ST.DL_ST(nomduST + "_avSync", Fps, "en", Id_Imdb)
            Chemin_STENG = Resync.ST_STREF(cheminfilm, Chemin_STENG, nomduST)

        """Partie en RECUP ST FR"""
        if Id_track_ST_fr is not None:
            Chemin_STFR = Extraction.ST(cheminfilm, Id_track_ST_fr, Format_ST_fr, Nom_du_film)
        else:
            nomduST = Nom_du_film + "_STFR"
            Chemin_STFR = telecharge_ST.DL_ST(nomduST + "_avSync", Fps, "fr", Id_Imdb)
            if Id_track_ST_en is not None:          #faire une fonction de ça car répéter dans le code déjà une fois
                Chemin_STFR = Resync.ST_STREF(Chemin_STENG, Chemin_STFR, nomduST)
            else:
                Chemin_STFR = Resync.ST_STREF(cheminfilm, Chemin_STFR, nomduST)

        """Partie Assemblage Stfr et Eng"""
        chemin_STFR_ass = ass_manip.transforme(Chemin_STFR)
        chemin_STENG_ass = ass_manip.transforme(Chemin_STENG)



   # case 3:
      #  print("Génération du sous titre Anglais avec trad lorsque besoin (pas fini)") #en version final, idée pouvoir avoir la traduction dés que besoin, niv1 = on appuie sur un bouton et c la phrase en trad fr qui spawn, niv 2 = on appuie sur bouton et c le/les mots compliqués qui sont expliqués



#C:\Users\ianpa\Videos\DDLBase.com_Stalker.1979.Criterion.BluRay.Remux.1080p.AVC.FLAC.1.0-HiFi.mkv
