tekst = "Anna, paweł, MIKOŁAJ"
lista = tekst.split(", ")
print(tekst)
print(lista)
print(type(lista))

imie1 = lista[0]
print (imie1)

imieDuze = imie1.upper()
print(imieDuze)

imiemale = imie1.lower()
print(imiemale)

#sprawdzenie zawartosci
print("\nPodaj nazwisko: ", end="")
nazwisko = input()
zawartosc =nazwisko.isalpha()
print(zawartosc)

nazwisko = ""
print(nazwisko.isalpha())

text1 = "Julia"
text2 = "Nowak"
print (text1 + text2)
text1 = text1.rstrip()
print (text1 + text2)
print (text1 + " " +text2)
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

'''text = "{1}, Java i {0}".format("PHP, Python")
print(text)
'''

new = text.replace("PHP", "C#")
print(new)

#wypisywanie danych

rok = 2019
miesiac = "kiwecień"
dzien = 1

print("\nData: ", end="")
print(dzien, miesiac, rok, sep="-")
