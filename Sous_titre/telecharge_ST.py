import requests, os, BluRayKestion

#clé API OpenSub : 8PRtkL7RI48NuxYauvAd0BExzKLJjC3N
def recup_Id_ST(idimdb, langue, Fps):
#ON RECUPERE ID DU ST
    URLid = "https://api.opensubtitles.com/api/v1/subtitles"  #url initial pour les soustitres de l'api

    querystring = {"imdb_id": str(idimdb), "languages": langue, "order_by" : "download_count"}     #params (ctrlv de l'ex du site)

    headers = {
        "User-Agent": "Pseudomyne",     #pseudo du compte
        "Accept": "application/json",
        "Api-Key": "8PRtkL7RI48NuxYauvAd0BExzKLJjC3N"       #clé api
    }

    res = requests.get(URLid, headers=headers, params=querystring)        #forme l'url avec url puis headers et params
    donnees = res.json()

    meilleur_ST = None
    liste_mots = ["criterion", "2160p", "4k", "uhd", "remux", "bluray", "brrip", "br", False] #on recup les sous titre les plus proches de la version que je regarde
    for mot in liste_mots:
        for St in donnees['data']:
            print(St)
            motmagiquetrouvé = BluRayKestion.contientUnMotMagique(St['attributes']['release'])
            if  motmagiquetrouvé == mot and St['attributes']['nb_cd'] == 1: #Si ya que un seul CD (sinon faut rassembler après...) et si ya un mot bon
                   print(mot, "<--", St)
                   meilleur_ST = St    #dans donnees, dans tableau data, case St qui correspond
                   break
        if meilleur_ST is not None:
            break

    """
    if not meilleur_ST:         #si on a pasz trouver avec les bons fps, on prend le premier avec 1 CD
        for St in donnees['data']:
            if St['attributes']['nb_cd'] == 1:
                meilleur_ST = St
                break
    """

    FpsST = meilleur_ST['attributes']['fps']
    id_du_ST = meilleur_ST['attributes']["files"][0]['file_id']
    return id_du_ST, FpsST


def DL_ST(nomduST, FpsFilm, Langue, idimdb):
    # ON DL LE ST

    URLdl = "https://api.opensubtitles.com/api/v1/download"
    id_du_ST, FpsST= recup_Id_ST(idimdb, Langue, FpsFilm)

    params = {
        "file_id": id_du_ST,
        "file_name": nomduST,
        "in_fps": FpsST,
        "out_fps": FpsFilm,
    }

    headers = {
        "User-Agent":"Pseudomyne",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Api-Key": "8PRtkL7RI48NuxYauvAd0BExzKLJjC3N"
    }

    res = requests.post(URLdl, headers=headers, json=params)
    donnees = res.json()
    lien = donnees['link']
    fichierSRT = requests.get(lien)

    os.makedirs("ST_Recuperes", exist_ok=True)
    CheminFichierST = os.path.join("ST_Recuperes", nomduST) + ".srt"
    with open (CheminFichierST, 'wb') as fichier:
        fichier.write(fichierSRT.content)

    return CheminFichierST


if __name__ == "__main__":
    print(recup_Id_ST("tt0079944","fr", 23.976))
    id, FpST = recup_Id_ST("tt0079944","fr", 23.976)







