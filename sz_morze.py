import time

def sz_morze_validalas(morze_szoveg):
    engedelyezett = {'.', '-', ' ', '/'}
    tisztitott = morze_szoveg.strip()
    if not tisztitott:
        return False
    return all(karakter in engedelyezett for karakter in tisztitott)

class SZMorzeKezelo:
    def __init__(self):
        self.szotar = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', ' ': '/'
        }
        self.forditott_szotar = {v: k for k, v in self.szotar.items()}
        self.elozmenyek = []

    def szovegbol_morze(self, szoveg):
        ekezetek = {'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ö': 'O', 'Ő': 'O', 'Ú': 'U', 'Ü': 'U', 'Ű': 'U'}
        eredmeny = []
        for karakter in szoveg.upper():
            alap_karakter = ekezetek.get(karakter, karakter)
            if alap_karakter in self.szotar:
                eredmeny.append(self.szotar[alap_karakter])
        morze_kimenet = ' '.join(eredmeny)
        if morze_kimenet:
            idopont = time.strftime("%H:%M:%S")
            self.elozmenyek.append(f"[{idopont}] {szoveg} -> {morze_kimenet}")
        return morze_kimenet

    def morzeból_szoveg(self, morze_szoveg):
        if not sz_morze_validalas(morze_szoveg):
            return "Érvénytelen morze karakterek!"
        szavak = morze_szoveg.strip().split(' / ')
        dekodolt_szavak = []
        for szo in szavak:
            betuk = szo.split(' ')
            dekodolt_betuk = [self.forditott_szotar.get(b, '?') for b in betuk if b]
            dekodolt_szavak.append(''.join(dekodolt_betuk))
        szoveg_kimenet = ' '.join(dekodolt_szavak)
        idopont = time.strftime("%H:%M:%S")
        self.elozmenyek.append(f"[{idopont}] {morze_szoveg} -> {szoveg_kimenet}")
        return szoveg_kimenet