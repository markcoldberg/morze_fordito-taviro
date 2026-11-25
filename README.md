{\rtf1\ansi\ansicpg1250\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Morzek\'f3d Ford\'edt\'f3 \'e9s T\'e1v\'edr\'f3\
\
**Hallgat\'f3:** Sid\'f3 Zolt\'e1n\
\
## Feladat le\'edr\'e1sa\
A program egy grafikus fel\'fclettel rendelkez\uc0\u337  morzek\'f3d-ford\'edt\'f3 \'e9s interakt\'edv t\'e1v\'edr\'f3 alkalmaz\'e1s. K\'e9pes a be\'edrt magyar \'e9kezetes vagy \'e9kezet n\'e9lk\'fcli sz\'f6veget morzek\'f3dd\'e1 alak\'edtani, a jeleket vizu\'e1lisan elvillogtatni egy jelz\u337 l\'e1mp\'e1n, valamint a felhaszn\'e1l\'f3 \'e1ltal eg\'e9rkattint\'e1sokkal (r\'f6vid \'e9s hossz\'fa gombnyom\'e1sokkal) leadott morzejeleket visszaford\'edtani olvashat\'f3 sz\'f6vegg\'e9. Minden ford\'edt\'e1st id\u337 b\'e9lyeggel ell\'e1tva napl\'f3z.\
\
## Modulok \'e9s a modulokban haszn\'e1lt f\'fcggv\'e9nyek\
\
### Be\'e9p\'edtett / tanult modulok:\
* **tkinter** (grafikus fel\'fclet \'e9s esem\'e9nykezel\'e9s):\
  * `Tk()`, `mainloop()`, `Label()`, `Entry()`, `Button()`, `Frame()`, `Canvas()`, `Listbox()`\
  * `messagebox.showwarning()`, `messagebox.showerror()`\
* **time** (bemutatand\'f3 modul - id\uc0\u337 m\'e9r\'e9s \'e9s id\u337 z\'edt\'e9s):\
  * `time.perf_counter()` \'96 a t\'e1v\'edr\'f3 gomb lenyom\'e1sa \'e9s felenged\'e9se k\'f6z\'f6tt eltelt id\uc0\u337  pontos m\'e9r\'e9s\'e9re (pont \'e9s vonal megk\'fcl\'f6nb\'f6ztet\'e9se).\
  * `time.sleep()` \'96 a vizu\'e1lis morze-villogtat\'e1s jel- \'e9s sz\'fcnetidej\'e9nek id\uc0\u337 z\'edt\'e9s\'e9re.\
  * `time.strftime()` \'96 az aktu\'e1lis \'f3ra:perc:m\'e1sodperc form\'e1tum\'fa id\uc0\u337 b\'e9lyeg gener\'e1l\'e1s\'e1hoz a napl\'f3z\'e1skor.\
\
### Saj\'e1t modul:\
* **sz_morze.py**:\
  * `sz_morze_validalas(morze_szoveg)` \'96 ellen\uc0\u337 rzi, hogy a megadott karakterl\'e1nc kiz\'e1r\'f3lag \'e9rv\'e9nyes morze karaktereket (`.`, `-`, sz\'f3k\'f6z, `/`) tartalmaz-e.\
\
## Oszt\'e1lyok\
* **`SZMorzeKezelo`** (`sz_morze.py`): A morze sz\'f3t\'e1r t\'e1rol\'e1s\'e1\'e9rt, a k\'e9tir\'e1ny\'fa ford\'edt\'e1s\'e9rt (`szovegbol_morze`, `morzeb\'f3l_szoveg`) \'e9s az el\uc0\u337 zm\'e9nyek list\'e1j\'e1nak kezel\'e9s\'e9\'e9rt felel\u337 s oszt\'e1ly.\
* **`MorzeAlkalmazas`** (`main.py`): A `tkinter` grafikus fel\'fclet fel\'e9p\'edt\'e9s\'e9\'e9rt, az esem\'e9nyek (`<ButtonPress-1>`, `<ButtonRelease-1>`) kezel\'e9s\'e9\'e9rt \'e9s a vizu\'e1lis jelz\uc0\u337 l\'e1mpa vez\'e9rl\'e9s\'e9\'e9rt felel\u337 s f\u337  oszt\'e1ly.}