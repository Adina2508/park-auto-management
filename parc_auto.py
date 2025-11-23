import datetime

class Masina:
    def __init__(self, marca, model, an_fabricatie, kilometraj):
        self.marca = marca
        self.model = model
        self.an_fabricatie = an_fabricatie
        self.kilometraj = kilometraj

# În constructor, validați că kilometraj este un număr pozitiv.
        # Dacă nu este, ridicați o excepție de tip ValueError.
        if kilometraj < 0:
            raise ValueError("Kilometrajul trebuie sa fie pozitiv.")

# descriere() – returnează un text cu toate informațiile despre mașină
    def descriere(self):
        return f"Masina {self.marca} cu modelul {self.model} a fost fabricata in anul {self.an_fabricatie} si dispune de un kilometraj de {self.kilometraj}."

# vechime() – calculează și returnează vechimea mașinii în ani.
    def vechime(self):
        an_curent = datetime.datetime.now().year
        return an_curent - self.an_fabricatie

# actualizeaza_kilometraj(distanta) – adaugă distanța la kilometraj, dar doar dacă distanța este pozitivă.
    def actualizeaza_kilometraj(self, distanta):
        if distanta < 0:
            print("Distanta trebuie sa fie un numar pozitiv.")
        else:
            self.kilometraj += distanta

# get_datetime() – metodă statică ce furnizează data și ora curentă.
    @staticmethod
    def get_datetime():
        return datetime.datetime.now()




parc_auto = [
    Masina("Volvo", "Combi", 2010, 10000),
    Masina("Audi", "A4", 2016, 250000),
    Masina("Renault", "Clio", 2018, 18000),
    Masina("Seat", "Ibiza", 2009, 145000),
    Masina("Kia", "Ceed", 2022, 10000)
]

rezultat = []
def filtreaza_dupa_vechime(depozit, ani_minimi):
    for masina in depozit:
        if masina.vechime() > ani_minimi:
            rezultat.append(masina)
    return rezultat

masini_vechi = filtreaza_dupa_vechime(parc_auto, 10)

print("Aceasta este lista cu masinile mai vechi de 10 ani:\n")
for m in masini_vechi:
    print(m.descriere())