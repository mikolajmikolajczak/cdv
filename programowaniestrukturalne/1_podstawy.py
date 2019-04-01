print("CDV")
print(2)


'''
Komentarz
blokowy
'''

#potegowanie

potega = 2 ** 10
print(potega)

#pobieranie danych

imie = input()

#kontakenacja

print("Imie z klawiatury: " + imie)

nazwisko = input("Podaj nazwisko: ")

print("Nazwisko z klawiatury: " + nazwisko)

print()

print("Twoje imię: " +imie)
print("Twoje nazwisko: " +nazwisko)

print("Twoje imię: " + imie + " Twoje nazwisko: " + nazwisko)

'''
Użytkownik podaje wiek, wyświetl dane w formacie: Twój wiek: ... lat
'''
print("Podaj swój wiek: ",end="")
wiek = input()
print ("Twój wiek: ", wiek, " lat")


nazwisko = "Kowalski"
ostatniZnak = nazwisko[len(nazwisko) - 1]
print(ostatniZnak)

ostatniZnak = nazwisko[-1]
print(ostatniZnak)

print()

y = 4
print(type(y))
y = y /2
print(type(y))
print(y)

print (nazwisko[0:2])
