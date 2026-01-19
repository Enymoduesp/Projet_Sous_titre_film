import requests

#clé API OMdb : fa74fa1f
def recup_Id(Nom_du_film, Annee_du_film):
    URL = "https://www.omdbapi.com/?apikey=fa74fa1f&t=" + Nom_du_film + "&y=" + Annee_du_film
    res = requests.get(URL) #on fait la requette avec l'url qu'on a crée
    donnees = res.json() #transforme le json en dictionnaire/annuaire python utilisable
    ID_IMDB = donnees["imdbID"]
    return ID_IMDB

if __name__ == "__main__":
    print(recup_Id("Stalker", "1979"))

