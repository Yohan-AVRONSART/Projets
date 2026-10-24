import string
alphabet = string.ascii_lowercase
message_encrypté = input("taper le message crypté ")
#mh vxlv xq frgh vhfuhw

mots_courants = ["je", "tu", "il", "elle", "nous", "vous", "ils", "le", "la", "les",
                 "un", "une", "des", "de", "du", "et", "est", "suis", "es", "a",
                 "que", "qui", "pas", "ne", "en", "pour", "dans", "sur", "avec", "ce"]

def decaler_alphabet(key):
     return alphabet[key:] + alphabet[:key]

def dechiffrer(message, key):
    alphabet_décalé = decaler_alphabet(key)
    resultat = ""
    for lettre in message:
        if lettre in alphabet:
            index = alphabet_décalé.index(lettre)
            resultat += alphabet[index]
        else:
            resultat += lettre
    return resultat

def score(phrase):
    total = 0
    for mot in phrase.split():
        if mot in mots_courants:
            total += 1
    return total

meilleure_cle = 1
meilleur_resultat = dechiffrer(message_encrypté, 1)
for key in range(2, 26):
    resultat = dechiffrer(message_encrypté, key)
    if score(resultat) > score(meilleur_resultat):
        meilleure_cle = key
        meilleur_resultat = resultat

print(f"Clé {meilleure_cle} : {meilleur_resultat}")
