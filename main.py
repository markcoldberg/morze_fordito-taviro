import tkinter as tk
from tkinter import messagebox
import time
import sys
import subprocess
from sz_morze import SZMorzeKezelo, sz_morze_validalas

class MorzeAlkalmazas:
    def __init__(self, master):
        self.master = master
        self.master.title("Morzekód Fordító és Távíró")
        self.master.geometry("880x550")
        self.master.resizable(False, False)

        self.kezelo = SZMorzeKezelo()
        self.lenyomas_ideje = 0.0

        self.felepites()

    def rendszer_hang(self, idotartam_ms):
        if sys.platform.startswith("win"):
            import winsound
            winsound.Beep(750, idotartam_ms)
        elif sys.platform == "darwin":
            subprocess.Popen(["afplay", "/System/Library/Sounds/Tink.aiff"])
        else:
            self.master.bell()

    def felepites(self):
        fo_keret = tk.Frame(self.master)
        fo_keret.pack(fill=tk.BOTH, expand=True, padx=12, pady=10)

        bal_keret = tk.Frame(fo_keret)
        bal_keret.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        jobb_keret = tk.Frame(fo_keret, bd=2, relief="groove", padx=10, pady=8)
        jobb_keret.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(bal_keret, text="Szöveg -> Morzekód fordítás", font=("Arial", 12, "bold")).pack(pady=(4, 5))

        self.szoveg_bemenet = tk.Entry(
            bal_keret,
            width=45,
            font=("Arial", 11),
            bd=2,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#222222",
            highlightcolor="#cc0000"
        )
        self.szoveg_bemenet.pack(pady=5, ipady=4)

        gomb_keret1 = tk.Frame(bal_keret)
        gomb_keret1.pack(pady=6)

        tk.Button(gomb_keret1, text="Fordítás morzéra", command=self.fordit_morzera, width=18).pack(side=tk.LEFT, padx=5)
        tk.Button(gomb_keret1, text="Villogtatás (Lámpa)", command=self.villogtat, width=18).pack(side=tk.LEFT, padx=5)

        self.lampa_vaszon = tk.Canvas(bal_keret, width=66, height=66, highlightthickness=0)
        self.lampa_vaszon.pack(pady=5)
        self.lampa_kor = self.lampa_vaszon.create_oval(10, 10, 56, 56, fill="#444444", outline="black", width=2)

        tk.Frame(bal_keret, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=10, pady=10)

        tk.Label(bal_keret, text="Morzekód -> Szöveg (Távíró)", font=("Arial", 12, "bold")).pack(pady=5)

        self.morze_bemenet = tk.Entry(
            bal_keret,
            width=45,
            font=("Arial", 12),
            bd=2,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#222222",
            highlightcolor="#cc0000"
        )
        self.morze_bemenet.pack(pady=5, ipady=4)

        self.taviro_gomb = tk.Label(
            bal_keret,
            text="TÁVÍRÓ GOMB (Tartsd lenyomva: rövid = . | hosszú = -)",
            bg="#d92626",
            fg="white",
            font=("Arial", 11, "bold"),
            bd=2,
            relief="raised",
            height=2,
            width=46,
            cursor="hand2"
        )
        self.taviro_gomb.pack(pady=6)
        self.taviro_gomb.bind("<ButtonPress-1>", self.gomb_lenyomva)
        self.taviro_gomb.bind("<ButtonRelease-1>", self.gomb_felengedve)

        gomb_keret2 = tk.Frame(bal_keret)
        gomb_keret2.pack(pady=5)

        tk.Button(gomb_keret2, text="Betűköz ( )", command=self.betukoz_hozzaad, width=14).pack(side=tk.LEFT, padx=3)
        tk.Button(gomb_keret2, text="Szóköz ( / )", command=self.szokoz_hozzaad, width=14).pack(side=tk.LEFT, padx=3)
        tk.Button(gomb_keret2, text="Dekódolás", command=self.fordit_szovegre, width=14).pack(side=tk.LEFT, padx=3)

        tk.Label(bal_keret, text="Napló (Időbélyeggel):", font=("Arial", 10, "bold")).pack(pady=(10, 2))
        self.naplo_lista = tk.Listbox(bal_keret, width=64, height=7, bd=2, relief="solid")
        self.naplo_lista.pack(pady=5)

        tk.Label(jobb_keret, text="Morze ABC", font=("Arial", 12, "bold")).pack(pady=(0, 8))

        abc_racs = tk.Frame(jobb_keret)
        abc_racs.pack()

        elemek = [(k, v) for k, v in self.kezelo.szotar.items() if k != " "]
        sorok_szama = 9
        for index, (betu, kod) in enumerate(elemek):
            oszlop = index // sorok_szama
            sor = index % sorok_szama
            cella = tk.Frame(abc_racs, bd=1, relief="solid", padx=5, pady=3)
            cella.grid(row=sor, column=oszlop, padx=3, pady=3, sticky="ew")
            tk.Label(cella, text=betu, font=("Arial", 10, "bold"), width=2, anchor="w").pack(side=tk.LEFT)
            tk.Label(cella, text=kod, font=("Courier", 10, "bold"), fg="#b30000", width=5, anchor="e").pack(side=tk.RIGHT)

        tk.Label(
            jobb_keret,
            text="Szóköz elválasztó: /",
            font=("Arial", 9, "italic"),
            pady=8
        ).pack(side=tk.BOTTOM)

    def fordit_morzera(self):
        szoveg = self.szoveg_bemenet.get()
        if not szoveg.strip():
            messagebox.showwarning("Figyelem", "Adj meg egy szöveget a fordításhoz!")
            return
        eredmeny = self.kezelo.szovegbol_morze(szoveg)
        self.morze_bemenet.delete(0, tk.END)
        self.morze_bemenet.insert(0, eredmeny)
        self.naplo_frissites()

    def fordit_szovegre(self):
        morze = self.morze_bemenet.get()
        if not sz_morze_validalas(morze):
            messagebox.showerror("Hiba", "Csak pont (.), vonal (-), szóköz és / karakter használható!")
            return
        eredmeny = self.kezelo.morzeból_szoveg(morze)
        self.szoveg_bemenet.delete(0, tk.END)
        self.szoveg_bemenet.insert(0, eredmeny)
        self.naplo_frissites()

    def gomb_lenyomva(self, event):
        self.lenyomas_ideje = time.perf_counter()
        self.lampa_vaszon.itemconfig(self.lampa_kor, fill="#ff1e1e")
        self.taviro_gomb.config(bg="#ff4d4d", relief="sunken")
        self.rendszer_hang(150)

    def gomb_felengedve(self, event):
        eltelt_ido = time.perf_counter() - self.lenyomas_ideje
        self.lampa_vaszon.itemconfig(self.lampa_kor, fill="#444444")
        self.taviro_gomb.config(bg="#d92626", relief="raised")
        jel = "-" if eltelt_ido >= 0.25 else "."
        self.morze_bemenet.insert(tk.END, jel)

    def betukoz_hozzaad(self):
        self.morze_bemenet.insert(tk.END, " ")

    def szokoz_hozzaad(self):
        self.morze_bemenet.insert(tk.END, " / ")

    def villogtat(self):
        morze = self.morze_bemenet.get()
        if not sz_morze_validalas(morze):
            messagebox.showwarning("Figyelem", "Nincs érvényes morzekód a villogtatáshoz!")
            return
        for jel in morze:
            if jel == '.':
                self.lampa_vaszon.itemconfig(self.lampa_kor, fill="#ff1e1e")
                self.taviro_gomb.config(bg="#ff4d4d", relief="sunken")
                self.master.update()
                self.rendszer_hang(150)
                if not sys.platform.startswith("win"):
                    time.sleep(0.15)
            elif jel == '-':
                self.lampa_vaszon.itemconfig(self.lampa_kor, fill="#ff1e1e")
                self.taviro_gomb.config(bg="#ff4d4d", relief="sunken")
                self.master.update()
                self.rendszer_hang(450)
                if not sys.platform.startswith("win"):
                    time.sleep(0.45)
            self.lampa_vaszon.itemconfig(self.lampa_kor, fill="#444444")
            self.taviro_gomb.config(bg="#d92626", relief="raised")
            self.master.update()
            time.sleep(0.15)

    def naplo_frissites(self):
        self.naplo_lista.delete(0, tk.END)
        for sor in reversed(self.kezelo.elozmenyek):
            self.naplo_lista.insert(tk.END, sor)

if __name__ == "__main__":
    root = tk.Tk()
    app = MorzeAlkalmazas(root)
    root.mainloop()