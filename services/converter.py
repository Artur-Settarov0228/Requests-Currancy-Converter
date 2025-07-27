def kanvert_qilish(miqdor, dan ,ga , kurslar):
    if dan == "UZS":
        miqdor_uzd = miqdor / kurslar["USD"]
    elif dan =="USD":
        miqdor_uzd = miqdor
    elif dan == "EUR":
        miqdor_uzd = miqdor * (kurslar["USD"] / kurslar["EUR"])
    else :
        raise ValueError("Notugri valuta turi ")
    

    if ga == "UZS":
        return miqdor_uzd * kurslar["USD"]
    elif ga == "USD":
        return miqdor_uzd
    elif ga == "EUR":
        return miqdor_uzd * (kurslar["EUR"] / kurslar["USD"])
    else:
        raise ValueError("notugri kanvartitsiya")
    

def valuta_tanlash(n):
    mapping = {
        "1" : "USD",
        "2" : "EUR",
        "3" : "USZ"
    }    
    return mapping.get(n)
    


