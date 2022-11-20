####################################################### Aufgabe 1 ############################################################################
# (a) Hallo Ceasar wir haben dein Verschluesselungsverfahren geknackt
# (b) Programmierung ist einfach nur mega gut
# (b') Hallo    ->  OHSSV

###################################################### Aufgabe 2 ##############################################################################
# (a) Ist der Schluessel zu groß geht es ueber den ASCii Wertebereich der Buchstaben hinaus.
# (b)
# zeichen = "T"
# schluessel = 10
# zahl = ord("T")
# code = zahl + schluessel
# if code > 90:                               # nur Grossbuchstaben gefragt, damit ausreichend
#     code -= 26 
# codZ = chr(code)
# print(codZ)

####################################################### Aufgabe 3 ##############################################################################

# def verschiebung(zeichen, schluessel):
#     zahl = ord(zeichen)
#     neueZahl = zahl + schluessel
#     if neueZahl > 90:                       # nur Grossbuchstaben gefragt, damit ausreichend
#         neueZahl -= 26
#     neuesZeichen = chr(neueZahl)
#     return neuesZeichen

# print (verschiebung("P", 7))
# print (verschiebung("A", 3))
# print (verschiebung("T", 10))

###################################################### Aufgabe 4 ##################################################################################

def verschiebungE(zeichen, schluessel):
    zahl = ord(zeichen)
    neueZahl = zahl + schluessel
    if neueZahl > 90:                       # nur Grossbuchstaben gefragt, damit ausreichend
        neueZahl -= 26
    neuesZeichen = chr(neueZahl)
    return neuesZeichen

def verschluesselung(text, schluessel):
    neuerText =[]
    for c in text:
        d = verschiebungE(c, schluessel)
        neuerText.append(d)
    return neuerText

print (verschluesselung("ASTERIX", 3))
print (verschluesselung("OBELIX", 3))

##################################################### Aufgabe 5 ###################################################################################

def verschiebungD(zeichen, schluessel):
    zahl = ord(zeichen)
    neueZahl = zahl - schluessel
    if neueZahl < 65:                       # nur Grossbuchstaben gefragt, damit ausreichend
        neueZahl += 26
    neuesZeichen = chr(neueZahl)
    return neuesZeichen

def entschluesselung(text, schluessel):
    orgText = []
    for c in text:
        d = verschiebungD(c, schluessel)
        orgText.append(d)
    return orgText

print (entschluesselung("DVWHULA", 3))
print (entschluesselung("REHOLA", 3))
