import requests

def kurslarni_olish():
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"

    try:
        javob = requests.get(url)  
        data = javob.json()

        kurslar = {
            "USD": float([v for v in data if v['Ccy'] == 'USD'][0]['Rate']),
            "EUR": float([v for v in data if v['Ccy'] == 'EUR'][0]['Rate']),
            "UZS": 1.0  
        }

        return kurslar

    except Exception as e:
        raise Exception(" API ishlamayapti yoki xatolik yuz berdi:\n" + str(e))
