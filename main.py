class Ceg:
    def __init__(self, nev,projekt,szerepkor):
        self._nev = nev
        self._projekt = projekt
        self._szerepkor = szerepkor
        print("-- Developer létrehozva. --")

    def __str__(self):
        return self._nev + " a " + self._projekt + "-en dolgozik" + self._szerepkor + "szerepkörben."

    def __eq__(self, dolgozok):
        if isinstance(dolgozok, Ceg):
            if self._nev == dolgozok._nev and self._szerepkor == dolgozok._szerepkor and self._projekt == dolgozok._projekt:
                print("Duplikált bejegyzés!")
            elif self._projekt == dolgozok._projekt:
                return self._projekt == dolgozok._projekt


def duplika(munkasok):
    for i in range(len(munkasok)):
        for j in range(i+1, len(munkasok)):
            if munkasok[i] == munkasok[j]:
                print()
                print(munkasok[i]._nev + " és " + munkasok[j]._nev + " dolgoznak egy projekten!")

def main():
    munkas1 = Ceg("Ricsi","SolArch","Frontend")
    print(munkas1)
    munkas2 = Ceg("Angéla","ZerTeng","Tesztelő")
    print(munkas2)
    munkas3 = Ceg("Peti","KefERP","Backend")
    print(munkas3)
    munkas4 = Ceg("Éva","KefERP","Frontend")
    print(munkas4)

    munkasok = [munkas1,munkas2,munkas3,munkas4]
    duplika(munkasok)

if __name__ == "__main__":
    main()