# extremer_test_code.py
# BBm

import os
import sys
import math

def add(a, b):
    summe = a + b
    # ❗ Rückgabe fehlt
    # ❗ Variable wird nicht verwendet

def add(a, b):  # ❗ Doppelte Definition
    return a + b

def unused_func():
    temp = 42  # ❗ Niemals verwendet

def open_file():
    f = open("datei.txt", "r")  # ❗ Datei wird geöffnet, aber nie geschlossen

def string_vergleich():
    if "abc" is "abc":  # ❗ 'is' statt '=='
        print("Strings sind gleich")

def dangerous_eval():
    code = input("Code eingeben: ")
    eval(code)  # ❗ Unsicher: eval

def falscher_typ():
    return "fünf" + 5  # ❗ Typfehler

def division_durch_null():
    return 10 / 0  # ❗ Laufzeitfehler

def endlos_schleife():
    while True:
        pass  # ❗ Endlos ohne Break

def fehlerhafte_logik(a, b):
    if a > b:
        return b
    else:
        return a  # ❗ Sinnlose Logik

def nutzlose_if():
    if True:
        return 1
    else:
        return 2  # ❗ Wird nie erreicht

def print_zahl():
    for i in range(5):
        print(i)
        i += 1  # ❗ Kein Effekt, da i von for-Schleife gesteuert wird

def magic_numbers():
    if 42 == 3.14:  # ❗ Unnötiger Vergleich
        return True
    return False

def shadowing_example():
    list = [1, 2, 3]  # ❗ Überschreibt eingebauten Typ 'list'
    print(list)

print("Programmstart")
add(1, 2)
division_durch_null()
