import subprocess, os, pysrt

def ST_STREF(STREF, STDECAL, NomRes):
#si on a des sous titres en reference, Recup les chemins du STREF et STDECALé
    os.makedirs("ST_Generes", exist_ok=True) #on fait le dossier ST_Generes si il existe pas
    ST_Sync = os.path.join("ST_Generes", NomRes + ".srt")
    cmd = ["ffsubsync", STREF, "-i", STDECAL, "-o", ST_Sync]
    subprocess.run(cmd)
    print('fichier sync généré')
    return ST_Sync


def ST_NOREF(Film, STDECAL, NomRes):
#si on pas de ST en ref
    os.makedirs("ST_Generes", exist_ok=True) #on fait le dossier ST_Generes si il existe pas
    ST_Sync = os.path.join("ST_Generes", NomRes + ".srt")
    cmd = ["ffsubsync", Film, "-i", STDECAL, "-o", ST_Sync]
    subprocess.run(cmd)
    print('fichier sync généré')
    return ST_Sync


def Manuelle_ST(ST, t):
#décalage de t secondes
    sous_titres=pysrt.open(ST)
    sous_titres.shift(seconds = t)
    sous_titres.save(ST)
    print('fichier sync généré')
    return ST