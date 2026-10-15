# prova per commit nel main branch
a = 67



class Brano:
    # Creazione di un metodo/funzione, in questo caso con il costruttore
    def __init__(self, autore: str, titolo: str, durata: int):  # questi sono i parametri di una funzione
        self._autore = None
        self._titolo = None
        self._durata = None
        self.autore = autore
        self.titolo = titolo
        self.durata = durata

    @property
    def autore(self):
        return self._autore

    @autore.setter
    def autore(self, value: str):
        if not isinstance(value, str):
            raise TypeError("L'autore deve essere una stringa.")
        self._autore = value

    @property
    def titolo(self):
        return self._titolo

    @titolo.setter
    def titolo(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Il titolo deve essere una stringa.")
        self._titolo = value

    @property
    def durata(self):
        return self._durata

    @durata.setter
    def durata(self, value: int):
        try:
            self._durata = int(value)
        except (TypeError, ValueError):
            raise TypeError("La durata deve essere un numero intero.")

    def __str__(self):
        return f"{self.titolo}"

class CD:
    def __init__(self, autore:str , titolo:str, listabrani:list, duratacomplessiva:int):
        self.titolo=titolo
        self.autore=autore
        self.listabrani=listabrani
        self.duratacomplessiva=duratacomplessiva

    @property
    def titolo(self):
        return self.titolo

    @property
    def autore(self):
        return self.autore

    @property
    def listabrani(self):
        return self.listabrani

    @property       
    def duratacomplessiva(self):
        return self.duratacomplessiva
    
    def __str__(self):
        return f"{self.titolo} - {self.autore} - {self.listabrani} - {self.duratacomplessiva}"


if __name__ == "__main__":
    newBrano = Brano("Gue", "Scooteroni", 180)
    print(newBrano)     
    newCD = CD("Gue", "Squalo", ["Scooteroni", "Lamborghini"], 360)
    print(newCD)    
      