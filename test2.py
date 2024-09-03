def läs_data(filnamn):
    """Läser data från en fil rad för rad."""
    with open(filnamn) as fil:
        for rad in fil:
            yield rad.strip()
        
def filtrera_data(rader, nyckelord):
    """Filtrerar bort rader som inte innehåller ett specifikt nyckelord."""
    for rad in rader:
        for word in nyckelord:
            if word in rad:
                yield rad
                break

def analysera_data(rader):
    """Analyserar data genom att räkna ord i varje rad."""
    for rad in rader:
        yield len(rad.split())

def summera_antal_ord(ordantal):
    """Summerar totalt antal ord från analyserade rader."""
    total = 0
    for antal in ordantal:
        total += antal
    return total

# Använda pipelinen
filnamn = 'test1.txt'
nyckelord = ['I', 'the', 'and', 'is', 'at']
# nyckelord = 'Sebastian'

data = läs_data(filnamn)
filtrerad_data = filtrera_data(data, nyckelord) # Generator som tar en generator
analyserad_data = analysera_data(filtrerad_data) # Generator som tar en generator
total_ord = summera_antal_ord(analyserad_data) # Funktion

print(f"Totalt antal ord i filtrerad data: {total_ord}")
