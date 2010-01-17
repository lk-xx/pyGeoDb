#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
from sqlobject import *
import pygeodb
from pprint import pprint

geodata = {}

for line in sys.stdin:
    if line[0] == "#":
        continue

    values = line.strip().decode('utf-8').split(";")

    # Feld 1: eindeutiger Schlüssel (Primary Key)
    # Felder 2 bis 8: hierarchische Verwaltungsgliederung, hier:
    #      Feld  2: Staat (DE == Deutschland)
    #      Feld  3: Bundesland, s.o.
    #      Feld  4: Regierungsbezirk
    #      Feld  5: Landkreis
    #      Feld  6: Verwaltungszusammenschluss
    #      Feld  7: Ort
    # Felder 8 und 9: Koordinaten:
    #      Feld 8: Längengrad
    #      Feld 9: Breitengrad
    # Feld 10: Postleitzahl

    zipcode=str(values[9])
    city=values[6]
    country=str(values[1])
    longitude=float(values[7])
    latitude=float(values[8])
    if not country in geodata:
        geodata[country] = {}
    geodata[country][zipcode] = (longitude, latitude, city)

print "# autogenerated - do not edit"
print "geodata = ",
pprint(geodata)