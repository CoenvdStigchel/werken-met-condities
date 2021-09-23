vraag9 = 0
vraag8 = 0
vraag10 = 0
vraag11= 0
vraag12= 0
print("-------------------------------")
print("leuk dat u solliciteerd voor de")
print("baan van Circus directeur voor")
print("Circus HotelDeBotel.")
print("We zouden u graag een paar vragen willen stellen: ")
print("-------------------------------")
vraag1 = int(input("hoeveel jaar heeft u praktijkervaring met dieren-dressuur? "))
vraag2 = int(input("hoeveel jaar heeft u praktijkervaring met jongleren? "))
vraag3 = int(input("hoeveel jaar heeft u praktijkervaring met acrobatiek? "))
vraag4 = input("bezit u een Diploma MBO-4? J/N ")
vraag5 = input("bezit u een geldig vrachtwagen rijbewijs? J/N ")
vraag6 = input("bezit u een hoge hoed? J/N ")
vraag7 = input("bent u een Man (M) of een Vrouw (V)? M/V ")
if vraag7 == "m" or vraag7 == "M ":
    vraag8 = input("heeft u een snor? J/N ")
    if vraag8 == "j" or vraag8 =="J ":
        vraag9 = int(input("hoelang is uw snor in cm? "))
elif vraag7 == "v" or vraag7 == "V ":
    vraag10 = input("wat is uw haarkleur? (r=rood,b=blond,z=zwart) ")
    vraag11 = input("wat voor haarstijl heeft u? krul=k,staartjes=s,kaal=a ")
    vraag12 = int(input("hoe lang is uw haar in cm? "))
vraag13=int(input("wat is uw lichaamsgewicht in kg? "))
vraag14=int(input("hoe lang bent u in cm? "))

if vraag7 == "m" or vraag7 == "M ":
    if (vraag1 > 4 or vraag2 > 5 or vraag3 > 3) and (vraag4 == "J" or vraag4 == "j") and (vraag5 == "J" or vraag5 == "j") and (vraag6 == "J" or vraag6 == "j") and (vraag8 == "J" or vraag8 == "j") and vraag9 > 10 and vraag13 > 90 and vraag14 > 150:
        print("Gefeliciteerd, u bent een goede kanidaat. U mag uw CV doorsturen")
    else:
        print("Het spijt me, u bent niet in aanmerking gekomen voor deze beropespositie.")
elif vraag7 == "v" or vraag7 == "V":
    if (vraag1 > 4 or vraag2 > 5 or vraag3 > 3) and (vraag4 == "J" or vraag4 == "j") and (vraag5 == "J" or vraag5 == "j") and (vraag6 == "J" or vraag6 == "j") and vraag13 > 90 and vraag14 > 150 and (vraag10 == "r" or vraag10=="R") and (vraag11 == "k" or vraag11=="K") and vraag12 >20:
        print("Gefeliciteerd, u bent een goede kanidaat. u mag uw CV doorsturen")
    else:
        print("Het spijt me, u bent niet in aanmerking gekomen voor deze beropespositie.")