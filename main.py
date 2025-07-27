from utils.api import kurslarni_olish
from services.converter import kanvert_qilish
from datetime import datetime

def asosiy():
    kurslar = kurslarni_olish()
    print(" Valyuta konvertori dasturi")
    print("1 - USD\n2 - EUR\n3 - UZS")

    try:
        miqdor = float(input(" Miqdor: ").strip())

        dan_raqam = input(" Qaysi valyutadan (1-USD, 2-EUR, 3-UZS): ").strip()
        ga_raqam = input(" Qaysi valyutaga (1-USD, 2-EUR, 3-UZS): ").strip()

        dan = valuta_tanlash(dan_raqam)
        ga = valuta_tanlash(ga_raqam)

        if not dan or not ga:
            print("Xatolik: faqat 1 (USD), 2 (EUR), yoki 3 (UZS) tanlang.")
            return

        natija = kanvert_qilish(miqdor, dan, ga, kurslar)
        bugun = datetime.now().strftime("%d.%m.%Y")
        print(f"\n {miqdor:,.2f} {dan} = {natija:,.2f} {ga} ({bugun})")

    except ValueError:
        print(" Xatolik: son kiritilmadi.")
    except Exception as e:
        print(" Kutilmagan xatolik:", e)


def manu():
    while True:
        print("\n Valyuta konvertor menyusi")
        print("1) Konvertatsiya qilish")
        print("2) Dasturdan chiqish")

        tanlov = input(" >> Tanlang  [ 1 yoki 2 ] << ").strip()


        if tanlov == "1":
            asosiy()
        elif tanlov == "2":
            print("dasturdan chiqash")
            break
        else:
            print("Xato! notugri tanlov  siz faqat [1 yoki 2 ] ni tanlang")

if __name__ == "__main__":
    kurslar = kurslarni_olish()
    print("Kurslar:", kurslar)
    manu()
