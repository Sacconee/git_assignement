# prova per commit nel main branch
a = 67



class Brano:
    # Creazione di un metodo/funzione, in questo caso con il costruttore
    def __init__(self, autore: str, titolo: str, durata: int): #questi sono i parametri di una funzione
        self.autore = autore
        self.titolo = titolo
        self.durata = durata
    
    def __str__(self)
        return f"{self.titolo}"


if __name__ == "__main__":
    newBrano = Brano("Gue", "Scooteroni", "180")
    print(newBrano)    