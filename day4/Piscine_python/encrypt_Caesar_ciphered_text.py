import string

alphabet = string.ascii_lowercase

#taper le message + la clé
entree = input("tape un message | une clé :").lower()

#récupérer le message indépendamment de la clé
message, encryption_key = entree.split("|")

#vérifier que la clé est un nombre, puis la convertir en int()
encryption_key = encryption_key.strip()
if not encryption_key.isdigit():
    print("Veuillez taper un chiffre")
    exit()
encryption_key = int(encryption_key)


#décaler l'alphabet de la valeur de la clé
alphabet_décalé = ""
def decaler_alphabet(key):
     alphabet_décalé = alphabet[key:] + alphabet[:key]
     return alphabet_décalé

alphabet_décalé = decaler_alphabet(encryption_key)

lettre_chiffree = ""

for lettre in message:
    if lettre.isalpha() == True:
        index_original = alphabet.index(lettre) 
        lettre_chiffree += alphabet_décalé[index_original]
    else:
        lettre_chiffree += lettre    

print(lettre_chiffree)


