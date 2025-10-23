import copy


class Gemi:
    def __init__(self, numara, boyut, ulasma_suresi, kalma_suresi):
        self.numara = numara
        self.boyut = boyut
        self.ulasma_suresi = ulasma_suresi
        self.kalma_suresi = kalma_suresi


gemiler = [
    Gemi(1, 17, 21, 9),
    Gemi(2, 29, 28, 15),
    Gemi(3, 39, 39, 36),
    Gemi(4, 18, 12, 19),
    Gemi(5, 11, 24, 46),
    Gemi(6, 35, 58, 34),
    Gemi(7, 21, 69, 46),
    Gemi(8, 34, 24, 9),
    Gemi(9, 36, 61, 46),
    Gemi(10, 9, 1, 2),
    Gemi(11, 5, 67, 47),
    Gemi(12, 11, 65, 43),
    Gemi(13, 13, 16, 27),
    Gemi(14, 29, 24, 42),
    Gemi(15, 16, 25, 5),
    Gemi(16, 13, 30, 49),
    Gemi(17, 6, 24, 26),
    Gemi(18, 4, 27, 14),
    Gemi(19, 14, 72, 20),
    Gemi(20, 32, 62, 13),
]

liman_uzunlugu = 70
liman_listesi = []
toplam_sure = 0
time = 1


def liman_durumu():
    return sum(gemi.boyut for gemi in liman_listesi)


def tabu_kontrol(gemi1, gemi2):
    return (gemi1.numara, gemi2.numara) in tabu_listesi or (gemi2.numara, gemi1.numara) in tabu_listesi


def tabu_listeye_ekle(gemi1, gemi2):
    tabu_listesi.append((gemi1.numara, gemi2.numara))


def gemi_yerlestir():
    global liman_listesi
    global toplam_sure
    global time
    while time < 350:
        for gemi in sorted(gemiler, key=lambda x: x.ulasma_suresi):

            if gemi.ulasma_suresi == time:
                if liman_durumu() + gemi.boyut <= liman_uzunlugu:
                    liman_listesi.append(gemi)
                    print(
                        f"Gemi {gemi.numara} limana yerleştirildi. Liman Durumu = {liman_durumu()}, Toplam Süre = {time}")
                else:
                    gemi.ulasma_suresi += 1

            """print(time)
            print(f"Gemi {gemi.numara}")"""
            for gemi in liman_listesi:
                if gemi.ulasma_suresi + gemi.kalma_suresi == time:

                    target_numara = gemi.numara
                    for gemi2 in gemiler:
                        if gemi2.numara == target_numara:
                            gemiler.remove(gemi2)
                    liman_listesi.remove(gemi)
                    print(f"Gemi {gemi.numara} limandan ayrıldı. Süre = {time}")
        time += 1


tabu_listesi = []
gemi_yerlestir()

