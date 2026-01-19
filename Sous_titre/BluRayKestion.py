import re

def nettoie(mot):
    mot = mot.lower() #passe en minuscule
    mot = re.sub("[^a-z0-9]", "", mot) #on enleve tout cqui derange pour comparé
    return mot


def contientUnMotMagique(titre):
    titre = nettoie(titre)
    liste_mots = ["criterion", "2160p", "4k", "uhd", "remux", "bluray", "brrip", "br"]
    for mot in liste_mots:
        if mot in titre:
            return mot
    return False
