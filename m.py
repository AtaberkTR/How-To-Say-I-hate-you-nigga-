import pycountry
import time

countries = list(pycountry.countries)

for country in countries:
    time.sleep(0.05)
    print(f"Hate from {country.name}")