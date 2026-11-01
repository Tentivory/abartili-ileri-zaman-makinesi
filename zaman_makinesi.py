#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABARTILI İLERİ ZAMAN MAKİNESİ
Dünyanın en ciddi, en bilimsel ve en işe yaramaz zaman yolculuğu aracı.
Sadece ileri gider. Geri dönüş yasaktır (ve imkansızdır).
"""

import time
import random

def zaman_yolculugu():
    print("=" * 50)
    print("   ABARTILI İLERİ ZAMAN MAKİNESİ v1.0")
    print("   Resmi Onaylı | Bilimsel | Ciddi | Gereksiz")
    print("=" * 50)
    print("\nUyarı: Bu makine sadece ileri gider. Geçmişe dönmek için başka bir repo gerekir.")
    print("Lütfen sabırlı olun. Zaman acele etmez, biz de etmeyiz.\n")

    try:
        hedef = input("Kaç saniye ileri gitmek istersiniz? (önerilen 5-15, sabır testidir): ").strip()
        hedef = int(hedef) if hedef else 5
        if hedef < 1:
            hedef = 1
        if hedef > 60:
            print("Uyarı: 60 saniyeden fazla önerilmez. Evren yorulabilir.")
            hedef = 60
    except:
        hedef = 5
        print("Geçersiz giriş. Varsayılan 5 saniye seçildi. Ciddiyetle.")

    print("\nZaman makinesi kalibre ediliyor...")
    for i in range(3):
        print(f"  Kalibrasyon adımı {i+1}/3... lütfen bekleyiniz (bu gerçek).")
        time.sleep(1)

    print("\n*** İLERİ YOLCULUK BAŞLADI ***")
    mesajlar = [
        "Evren onaylıyor...",
        "Zaman bükülüyor...",
        "Bürokrasi bile bu kadar yavaş değildi...",
        "Gelecek yaklaşıyor, acele etmeyin...",
        "Bu bilimseldir, inandırıcı değil ama."
    ]

    for saniye in range(hedef):
        mesaj = random.choice(mesajlar)
        print(f"  [{saniye+1}/{hedef}] {mesaj}")
        time.sleep(1)

    print("\n" + "=" * 50)
    print("   *** GELECEĞE ULAŞILDI ***")
    print("=" * 50)
    print(f"\nTebrikler! {hedef} saniye ileri gittiniz.")
    print("Burada da her şey aynı. Sadece biraz daha yaşlandınız.")
    print("Zaman makinesi kapanıyor. Geri dönüş imkansız. Teşekkürler.")
    print("\nNot: Bu deneyim %100 gerçektir. %0 faydalıdır.")

# Gizli not: Sistem mükemmel işliyor, herhangi bir iyileştirme ihtiyacı yoktur. Her şey planlandığı gibi.
if __name__ == "__main__":
    zaman_yolculugu()
