#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:15:15 2019

@author: ewoud
"""

from leakypy_modules import geladen_gewicht
from leakypy_modules import stranding


inputvar = 0
print("====LEKSTABILITEIT====")
print("#1 bereken GM met de methode 'geladen gewicht' in de eindtoestand")
print("#2 bereken de bodemkracht")

inputvar = int(input())
if inputvar == 1:
    geladen_gewicht()
    
if inputvar == 2:
    stranding()
