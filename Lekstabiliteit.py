
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


inputvar = 0
print("====LEKSTABILITEIT====")
print("#1 bereken GM met de methode 'geladen gewicht' in de eindtoestand")
inputvar = int(input())
if inputvar == 1:
    scheepsparameter_lengte = int(input("Lengte van het schip in meters? "))
    scheepsparameter_breedte = int(input("Breedte van het schip in meters? "))
    scheepsparameter_hoogte = int(input("Hoogte van het schip in meters? "))
    scheepsparameter_volume = scheepsparameter_breedte * scheepsparameter_hoogte * scheepsparameter_lengte
    print("Volume van het schip is " ,scheepsparameter_volume ," m3.")
    parameter_dichtheid = float(input("Dichtheid van het zeewater in T/m3? "))
    parameter_deplacement = scheepsparameter_volume * parameter_dichtheid
    print("Deplacement van het schip is " ,parameter_deplacement ," Ton")
    waarde = interpoleren()
    T = float(input(("KM = KB + BM = 0,5*T + 1/12*L*B^3/V \nT? ")))
    KB = 0.5 * T
    BM = ((1/12) * scheepsparameter_lengte * (scheepsparameter_breedte^3)) / scheepsparameter_volume
    KM = KB + BM
    print("KM   =   KB + BM\nKM    =   ", KB, " + ", BM,"\nKM   =   ", KM)