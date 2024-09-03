import time
import random

def producer():
    """Producerar slumpmässiga tal."""
    while True:
        data = random.randint(1, 100)
        # data = input('Skriv något!')
        print(f"Producerade: {data}")
        
        yield data
        time.sleep(1)

def consumer(generator):
    """Bearbetar data från en generator."""
    for data in generator:
        print(f"Konsumerade: {data * 2}")
        time.sleep(2)

# Kör producer-konsumer-modellen
producent = producer()
consumer(producent)
