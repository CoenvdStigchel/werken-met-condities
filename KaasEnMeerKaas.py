invoer1 = input("is de kaas geel? --> ")
if invoer1 == "ja":
    invoer2 = input("zitten er gaten in? --> ")
    if invoer2 == "ja":
        invoer3 = input("is de kaas belachelijk duur? --> ")
        if invoer3 =="ja":
            print("het is emmenthaler")
        else:
            print("het is leerdammer")
    else:
        invoer4 = input("is de kaas hard als steen? --> ")
        if invoer4 =="ja":
            print("het is pemnigiano reggiano")
        else:
            print("het is goudse kaas")
else:
    invoer5 = input("heeft de kaas blauwe schimmels? ---> ")
    if invoer5 =="ja":
        invoer6 = input("heeft de kaas een korst? --> ")
        if invoer6 =="ja":
            print("het is bleu de rochbaron")
        else:
            print("faume d'ambert")
    else:
        invoer6 = input("heeft de kaas een korst? --> ")
        if invoer6 =="ja":
            print("camembert")
        else:
            print("mozzarella")
