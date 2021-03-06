#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:15:15 2019

@author: ewoud
"""

rnddigit = 2


def interpoleren():
    if input("moet er geinterpoleerd worden? y/n") == "y":
        x1 = float(input("x1  y1 \nx2 ? \nx3  y3\n\nWaarde van x1? "))
        x2 = float(input("waarde van x2? "))
        x3 = float(input("waarde van x3? "))
        y1 = float(input("waarde van y1? "))
        y3 = float(input("waarde van y3? "))
        y2 = (((x2 - x1) * (y3 - y1)) / (x3 - x1)) + 1
        print("Geinterpoleerde waarde = ", y2)
        return y2
    else:
        return float(input("Waarde? "))


def geladen_gewicht():

    scheepspar_l = int(input("Lengte van het schip in meters? "))
    scheepspar_b = int(input("Breedte van het schip in meters? "))
    scheepspar_t = int(input("Diepgang van het schip in meters? "))
    scheepspar_v = scheepspar_b * scheepspar_t * scheepspar_l
    print("Volume van het schip is ", scheepspar_v, " m3.")
    par_dichtheid = float(input("Dichtheid van het zeewater in T/m3? "))
    par_deplacement = scheepspar_v * par_dichtheid
    print("Deplacement van het schip is ", par_deplacement, " Ton")
    par_l_compart = float(input("\n\n==Na lek worden==\n\nLengte compartiment? "))
    parameter_uv = float(input("Uv? "))
    variabele_l_cor1 = (scheepspar_l- par_l_compart) + ((1 - parameter_uv) * par_l_compart)
    variabele_t_cor1 = scheepspar_v/(variabele_l_cor1*scheepspar_b)
    print("lengte waterlijn na lek worden = ", variabele_l_cor1, " M\nDiepgang na lek worden = ", variabele_t_cor1, " M")
    var_ingestroomd = par_l_compart * scheepspar_b * variabele_t_cor1 * parameter_uv * par_dichtheid
    var_depl_cor1 = par_deplacement + var_ingestroomd
    var_t_cor2 = (var_depl_cor1 / par_dichtheid) * (1 / (scheepspar_l * scheepspar_b))
    print("Ingestroomd = ", var_ingestroomd, " Ton\nDeplacement gecorrigeerd = ", var_depl_cor1, " Ton \nT = ", var_t_cor2, " M\n")
    scheepspar_kg = float(input("KG? "))
    var_kg_cor1 = ((par_deplacement * scheepspar_kg) + (var_ingestroomd * (var_t_cor2 / 2))) / (par_deplacement + var_ingestroomd)
    var_km_cor1 = (0.5 * var_t_cor2) + ((scheepspar_b ** 2) / (12 * var_t_cor2))
    var_gm_cor1 = var_km_cor1 - var_kg_cor1
    print("Nieuwe KG = ", var_kg_cor1, " M\nNieuwe KM = ", var_km_cor1, " M\nNieuwe GM = ", var_gm_cor1, " M")
    vvc1 = ((1/12) * par_l_compart * scheepspar_b ** 2) / (par_deplacement + var_ingestroomd)
    var_gm_cor2 = var_gm_cor1 + vvc1
    print("Vrije vloeistof correctie = ", vvc1, " M\nG'M = ", var_gm_cor2)
    var_km_cor2 = (0.5 * var_t_cor2) + (1/12 * (scheepspar_l - par_l_compart) * (scheepspar_b ** 3)) / scheepspar_v
    var_kg_cor2 = var_km_cor2 - scheepspar_kg
    print("KM = ", var_km_cor2, " M\nGM volgens methode 'gelijkblijvend deplacement' = ", var_kg_cor2, " M")


def stranding():
    tcm = float(input('t/cm='))  # 20,02
    tv = float(input('Tv1='))  # 4.5
    ta = float(input('Ta1='))  # 5
    tvn = float(input('Tv2='))  # 4.3
    tan = float(input('Ta2='))  # 5
    tgn = ((tvn + tan) / 2)
    tg = ((tv + ta) / 2)
    dtg = (tg - tgn)
    pb = (tcm * dtg * 100)
    print(pb)
    etm = float(input('ETM='))  # 142.6
    lcf = float(input('LCF='))  # 66.67
    lll = float(input('Lll='))  # 127.14
    alcf = (dtg * etm / pb * 200)
    aall = (alcf + lcf)
    ap = (aall - lll / 2)
    print('tov LCF', alcf)
    print('tov ALL', aall)
    print('tov plimsol', ap)  # plimsol = 1/2*lll
    tb = (tg - (ap * (tg - tv) / (0.5 * lll)))
    tbn = (tgn - (ap * (tgn - tvn) / (0.5 * lll)))
    print('tb=', tb)
    print('tbn=', tbn)
    dtb = ((tb - tbn) * 100)  # scheepstra neemt 13,33
    print('dtb=', dtb)
    lcf2 = (aall - lcf)
    print('lcf2=', lcf2)
    pl = ((etm * lll * dtb * tcm) / (lcf2 * dtb * tcm + etm * lll))
    print('pl=', pl)

def test():
    m1 = 12300
    m2 = 4100
    kg1 = 10.5
    kg2 = 2.67
    print(((m1 * kg1) + (m2 * kg2)) / (m1 + m2))




inputvar = 0
print("====LEKSTABILITEIT====")
print("#1 bereken G'M met de methode 'geladen gewicht' in de eindtoestand")
print("#2 bereken de bodemkracht")

inputvar = int(input())
if inputvar == 1:
    geladen_gewicht()
    
if inputvar == 2:
    stranding()
