##
## Hoofdbestand met globale functies om uit te voeren
## Uitgebreide functies hebben hun eigen bestand
## Opbouw:
##      - tamagotchi.py
##          Main functie wordt hier aangeroepen, I/O gebeurt hier
##      - fileio.py
##          Het genereren van initiele bestanden zoals de databank en voedselinformatie. Het opslaan en verwerken van informatie in de bestanden
##      - voeding.py
##          Het controleren van voeding en het verwerken van ingevoerde informatie.
##      - interface.py
##          Interface en UI elementen worden hier geregeld. Bevat informatie benodigd voor het weergeven van een menu en informatie om de tamagotchi weer te geven
##      - score.py
##          Puntentelling en status van de tamagotchi worden hier berekend en verwerkt.
##

import generate
import interface
import shelve


def main():
    ## vraag naam via interface functie
    x = interface.name()
    ## clear shell
    interface.clear_window()
    ## Geef hoofdmenu
    interface.main_menu(x)
    interface.handle(main, interface.pick_number(1,4))


main()
