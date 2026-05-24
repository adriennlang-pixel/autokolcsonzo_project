class Auto:
    def __init__(self, marka, tipus, ar):
        self.marka = marka
        self.tipus = tipus
        self.ar = ar
        self.elerheto = True

    def info(self):
        allapot = "Szabad" if self.elerheto else "Foglalt"
        return f"{self.marka} {self.tipus} - {self.ar} Ft/nap - {allapot}"


class Autokolcsonzo:
    def __init__(self):
        self.autok = []

    def auto_hozzaadas(self, auto):
        self.autok.append(auto)

    def autok_listazasa(self):
        print("\n--- ELÉRHETŐ AUTÓK ---")

        for index, auto in enumerate(self.autok):
            print(f"{index + 1}. {auto.info()}")

    def autoberles(self):
        self.autok_listazasa()

        try:
            valasztas = int(input("\nMelyik autót szeretnéd bérelni? "))

            if valasztas < 1 or valasztas > len(self.autok):
                print("Hibás választás!")
                return

            auto = self.autok[valasztas - 1]

            if auto.elerheto:
                auto.elerheto = False
                print(f"Sikeres bérlés: {auto.marka} {auto.tipus}")
            else:
                print("Ez az autó már foglalt!")

        except:
            print("Hibás adat!")

    def auto_visszahozas(self):
        print("\n--- FOGLALT AUTÓK ---")

        foglalt_autok = []

        for auto in self.autok:
            if not auto.elerheto:
                foglalt_autok.append(auto)

        if len(foglalt_autok) == 0:
            print("Nincs visszahozható autó!")
            return

        for index, auto in enumerate(foglalt_autok):
            print(f"{index + 1}. {auto.info()}")

        try:
            valasztas = int(input("\nMelyik autót hozod vissza? "))

            if valasztas < 1 or valasztas > len(foglalt_autok):
                print("Hibás választás!")
                return

            auto = foglalt_autok[valasztas - 1]
            auto.elerheto = True

            print("Az autó sikeresen visszahozva!")

        except:
            print("Hibás adat!")


kolcsonzo = Autokolcsonzo()

kolcsonzo.auto_hozzaadas(Auto("BMW", "M3", 30000))
kolcsonzo.auto_hozzaadas(Auto("Audi", "A6", 25000))
kolcsonzo.auto_hozzaadas(Auto("Toyota", "Corolla", 18000))


while True:
    print("\n===== AUTÓKÖLCSÖNZŐ =====")
    print("1 - Autók listázása")
    print("2 - Autó bérlése")
    print("3 - Autó visszahozása")
    print("4 - Kilépés")

    valasztas = input("Válassz: ")

    if valasztas == "1":
        kolcsonzo.autok_listazasa()

    elif valasztas == "2":
        kolcsonzo.autoberles()

    elif valasztas == "3":
        kolcsonzo.auto_visszahozas()

    elif valasztas == "4":
        print("Kilépés...")
        break

    else:
        print("Hibás menüpont!")