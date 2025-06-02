# fehlerhafter_python_code.py

def addiere_zahlen(a, b):
    summe = a + b
    # ❗ Keine Rückgabe (Code Smell)
    return

def drucke_nachricht():
    print("Dies ist eine Nachricht")

def nutzer_eingabe():
    name = input("Gib deinen Namen ein: ")
    if name == "admin":
        print("Willkommen Admin")
    elif name == "user":  # kein Bug mehr, aber if/elif können z. B. zu toten Pfaden führen
        print("Willkommen Nutzer")
    else:
        print("Willkommen", name)

def nie_genutzt():
    x = 5 + 6  # ❗ Toter Code: Funktion wird nie aufgerufen

def fehlerhafte_berechnung():
    return 5 / 0  # ❗ Bug: Division durch 0

drucke_nachricht()
nutzer_eingabe()
addiere_zahlen(3, 4)
