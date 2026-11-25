# Morzekód Fordító és Távíró

**Hallgató:** Sidó Zoltán

## Feladat leírása
A program egy grafikus felülettel rendelkező morzekód-fordító és interaktív távíró alkalmazás. Képes a beírt magyar ékezetes vagy ékezet nélküli szöveget morzekóddá alakítani, a jeleket vizuálisan elvillogtatni egy jelzőlámpán, valamint a felhasználó által egérkattintásokkal (rövid és hosszú gombnyomásokkal) leadott morzejeleket visszafordítani olvasható szöveggé. Minden fordítást időbélyeggel ellátva naplóz.

## Modulok és a modulokban használt függvények

### Beépített / tanult modulok:
* **tkinter** (grafikus felület és eseménykezelés):
  * `Tk()`, `mainloop()`, `Label()`, `Entry()`, `Button()`, `Frame()`, `Canvas()`, `Listbox()`
  * `messagebox.showwarning()`, `messagebox.showerror()`
* **time** (bemutatandó modul - időmérés és időzítés):
  * `time.perf_counter()` – a távíró gomb lenyomása és felengedése között eltelt idő pontos mérésére (pont és vonal megkülönböztetése).
  * `time.sleep()` – a vizuális morze-villogtatás jel- és szünetidejének időzítésére.
  * `time.strftime()` – az aktuális óra:perc:másodperc formátumú időbélyeg generálásához a naplózáskor.

### Saját modul:
* **sz_morze.py**:
  * `sz_morze_validalas(morze_szoveg)` – ellenőrzi, hogy a megadott karakterlánc kizárólag érvényes morze karaktereket (`.`, `-`, szóköz, `/`) tartalmaz-e.

## Osztályok
* **`SZMorzeKezelo`** (`sz_morze.py`): A morze szótár tárolásáért, a kétirányú fordításért (`szovegbol_morze`, `morzeból_szoveg`) és az előzmények listájának kezeléséért felelős osztály.
* **`MorzeAlkalmazas`** (`main.py`): A `tkinter` grafikus felület felépítéséért, az események (`<ButtonPress-1>`, `<ButtonRelease-1>`) kezeléséért és a vizuális jelzőlámpa vezérléséért felelős fő osztály.
