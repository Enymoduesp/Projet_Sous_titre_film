from pymediainfo import MediaInfo
import re


def recupTitreEtSTEtFps(cheminfilm):

    Donnees_film = MediaInfo.parse(cheminfilm)

    Id_track_ST_en = None
    Id_track_ST_fr = None
    Format_ST_en = None
    Format_ST_fr = None

    for track in Donnees_film.tracks:       #on parcourt chaque track
        if track.track_type == 'General':           #si c la base, on recup le nom
            Nom_du_film_annee = track.file_name
        elif track.track_type == 'Video':
            Fps = track.frame_rate
        elif track.track_type == 'Text':
            langue = track.language
            if  Id_track_ST_en is None and (langue == "en" or langue == "eng" or langue == "English" or langue == "english"): #car trop chiant de gerer pgs pour l'instant
                Id_track_ST_en = str(track.track_id - 1)
                Format_ST_en = track.format
            elif Id_track_ST_fr is None and (langue == "fr" or langue == "fra" or langue == "French" or langue == "Français"):
                Id_track_ST_fr = str(track.track_id - 1)
                Format_ST_fr = track.format


    #fichier sous la forme DDLBase.come_Nom.du.film.DATE.BlurayE[ETC]
    Nom_du_film_annee = Nom_du_film_annee.replace("DDLBase.com_", "")  #on enleve le truc de dl
    Nom_du_film_annee = re.sub("([0-9]{4}).*", "\\1", Nom_du_film_annee)    #on recup juste Nomdufilm.annee
    Nom_du_film_annee = Nom_du_film_annee.replace(".", " ") #on met des espaces à la place des points

    Nom_du_film = re.sub("(.*)[0-9]{4}", "\\1", Nom_du_film_annee).strip() #strip enleve espace debut et fin
    Annee_du_film = re.search("[0-9]{4}", Nom_du_film_annee).group()        #recup la date, .group permet de recup la partie regex trouvée

    return Nom_du_film, Annee_du_film, Fps, Id_track_ST_en, Format_ST_en, Id_track_ST_fr, Format_ST_fr

if __name__ == "__main__":
    cheminfilm = input("chemin du MKV : ")
    Nom_du_film, Annee_du_film, Fps, Id_track_ST_en, Format_ST_en, Id_track_ST_fr, Format_ST_fr = recupTitreEtSTEtFps(cheminfilm)
    print("nom du film est : ", Nom_du_film, "\n", "sortie en : ", Annee_du_film, "\n","FPS :", Fps,
          "\n les langues dispos sont :", Id_track_ST_en, Format_ST_en,  Id_track_ST_fr, Format_ST_fr)

    #C:\Users\ianpa\Videos\DDLBase.com_Stalker.1979.Criterion.BluRay.Remux.1080p.AVC.FLAC.1.0-HiFi.mkv