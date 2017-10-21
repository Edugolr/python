#!/usr/bin/env python3
"""Plane implementerad enligt uppgiften i kmom01"""

print("Mata in uppgifterna nedan för omvandling till feet , mph samt Fahrenheit")

# användarinmatning av programmets variabler
heightM = input("Höjd över havet (meter): ")
speedKmh = input("Hastighet (km/h): ")
tempC = input("Temperatur utanför flygplanet (Celsius): ")

# omvandling av variablerna till sina nya enheter
heightFeet = float(heightM) * 3.28084
speedMph = float(speedKmh) * 0.62137
tempF = float(tempC) * 9 / 5 + 32

# utskrift utav de nya enheterna
print('Höjd över havet (feet): ', heightFeet)
print('Hastighet (mph): ', speedMph)
print('emperatur utanför flygplanet (Farenheit): ', tempF)
