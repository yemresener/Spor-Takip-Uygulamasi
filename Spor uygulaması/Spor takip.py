

from PIL import Image, ImageTk
from pathlib import Path
from tkinter import messagebox
from tkinter import *
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import ttk
import mysql.connector



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"image\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def login_msgbox(hata_kodu,mesaj_text,icon,pencere):
    mesaj = tk.Toplevel(pencere)

    mesaj.title(hata_kodu)
    mesaj.geometry("300x100")

    l1 = tk.Label(mesaj, image="::tk::icons::"+icon)
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2 = tk.Label(mesaj, text=mesaj_text)
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")

    b1 = Button(mesaj, text="Tamam", command=mesaj.destroy, width=10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")


    mesaj.update_idletasks()
    x = pencere.winfo_rootx() + (pencere.winfo_width() - mesaj.winfo_width()) // 2
    y = pencere.winfo_rooty() + (pencere.winfo_height() - mesaj.winfo_height()) // 2
    mesaj.geometry(f"300x100+{x}+{y}")




window = Tk()

window.geometry("500x500")
window.configure(bg="#A0B2B0")
window.title("FIT")






class Uygulama():
    def __init__(self):
        self.giris_paneli()


    def veritabani(self):

        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python_spor"
            )


##################################  GİRİŞ PENCERESİ VE FONKSİYONLARI  #####################################
    def giris_paneli(self):

        self.canvas = Canvas(
            window,
            bg="#22348f",
            height=500,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)


        self.canvas.create_text(
            33.0,
            19.0,
            anchor="nw",
            text="                                           BE FIT!",
            fill="#ECE4E4",
            font=("JetBrainsMonoRoman ExtraBold", 30 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            130.0,
            135.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=49.0,
            y=119.0,
            width=162.0,
            height=33.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            130.0,
            207.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            show="*",
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=49.0,
            y=190.0,
            width=162.0,
            height=35.0
        )

        self.text2=self.canvas.create_text(
            33.0,
            93.0,
            anchor="nw",
            text="Kullanıcı adı:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )

        self.text1=self.canvas.create_text(
            33.0,
            165.0,
            anchor="nw",
            text="Sifre:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )


        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.hesap_olustur = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.hide,
            relief="flat"
        )
        self.hesap_olustur.place(
            x=144.0,
            y=467.0,
            width=213.0,
            height=22.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.giris_yapma,
            relief="flat"
        )
        self.button_2.place(
            x=33.0,
            y=250.0,
            width=47.643829345703125,
            height=34.0,

        )


        window.resizable(False, False)
        window.mainloop()

    def hide(self):
        self.entry_1.destroy()
        self.entry_2.destroy()
        self.hesap_olustur.destroy()
        self.button_2.destroy()
        self.canvas.delete(self.entry_bg_1)
        self.canvas.delete(self.entry_bg_2)
        self.canvas.delete(self.text1)
        self.canvas.delete(self.text2)

        self.email_resim = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.email_bg = self.canvas.create_image(
            130.0,
            135.5,
            image=self.email_resim
        )
        self.email = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.email.place(
            x=49.0,
            y=119.0,
            width=162.0,
            height=33.0
        )
        self.kilo_resim = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.kilo_bg = self.canvas.create_image(
            368.0,
            134.5,
            image=self.kilo_resim
        )
        self.kilo = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.kilo.place(
            x=280.0,
            y=119.0,
            width=162.0,
            height=33.0
        )
        self.boy_resim = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.boy_bg = self.canvas.create_image(
            365.0,
            207,
            image=self.boy_resim
        )
        self.boy = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.boy.place(
            x=280.0,
            y=190.0,
            width=162.0,
            height=33.0
        )
        self.tarih_resim = PhotoImage(
            file=relative_to_assets("re.png"))
        self.tarih_bg = self.canvas.create_image(
            365.0,
            276.5,
            image=self.tarih_resim
        )
        self.tarih = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.tarih.place(
            x=280.0,
            y=261.0,
            width=162.0,
            height=35.0
        )



        self.numara_resim = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.numara_bg = self.canvas.create_image(
            130.0,
            207.5,
            image=self.numara_resim
        )
        self.numara = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.numara.place(
            x=49.0,
            y=190.0,
            width=162.0,
            height=35.0
        )


        self.sifre_resim = PhotoImage(
            file=relative_to_assets("re.png"))
        self.sifre_bg = self.canvas.create_image(
            130.0,
            276.5,
            image=self.sifre_resim
        )
        self.sifre = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.sifre.place(
            x=49.0,
            y=261.0,
            width=162.0,
            height=35.0
        )
        self.email_text = self.canvas.create_text(
            33.0,
            93.0,
            anchor="nw",
            text="Kullanıcı adı:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.kilo_text = self.canvas.create_text(
            277.0,
            93.0,
            anchor="nw",
            text="Kilo:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.boy_text = self.canvas.create_text(
            277.0,
            165.0,
            anchor="nw",
            text="Boy:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.numara_text = self.canvas.create_text(
            33.0,
            165.0,
            anchor="nw",
            text="Telefon numarası:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.sifre_text = self.canvas.create_text(
            33.0,
            237.0,
            anchor="nw",
            text="Sifre:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.tarih_text = self.canvas.create_text(
            277.0,
            237.0,
            anchor="nw",
            text="Tarih:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.kayit_buton = PhotoImage(
            file=relative_to_assets("kayitbuton.png"))
        self.kayit = Button(
            image=self.kayit_buton,
            borderwidth=0,
            highlightthickness=0,
            command=self.kayit_ol,
            relief="flat"
        )
        self.kayit.place(
            x=33.0,
            y=330.0,
            width=77.643829345703125,
            height=34.0,

        )

        self.gerigel_resim = PhotoImage(
            file=relative_to_assets("geridön.png"))
        self.gerigel = Button(
            image=self.gerigel_resim,
            borderwidth=0,
            highlightthickness=0,
            command=self.giris_paneli,
            relief="flat"
        )
        self.gerigel.place(
            x=200.0,
            y=467.0,
            width=120.0,
            height=20.0,

        )

    def kayit_ol(self):
        self.veritabani()
        self.email_giris = self.email.get()
        self.numara_giris = self.numara.get()
        self.sifre_giris = self.sifre.get()
        self.kilo_giris= self.kilo.get()
        self.boy_giris=self.boy.get()
        self.tarih_giris=self.tarih.get()
        self.mycursor = self.mydb.cursor()
        ################################################
        self.sql_kayit_kontrol = "Select id FROM kullanicilar where kullanici_adi = %s"
        self.sql_kayit = "INSERT INTO kullanicilar (kullanici_adi, sifre, numara,kilo,boy,tarih) VALUES (%s, %s, %s,%s,%s,%s)"

        # Boşluk kontrolü
        if not self.email_giris.strip() or not self.numara_giris.strip() or not self.sifre_giris.strip() or not self.kilo_giris.strip() or not self.boy_giris.strip() or not self.tarih_giris.strip():
            login_msgbox("HATA!", "Boşluk bırakma!", "warning",window)
        else:
            self.mycursor.execute(self.sql_kayit_kontrol, (self.email_giris,))
            self.myresult = self.mycursor.fetchone()

            if self.myresult:  # DEĞER DÖNDÜRÜYORSA
                login_msgbox("HATA!", "Kullanıcı adı zaten mevcut!", "warning",window)
            else:
                try:
                    self.mycursor.execute(self.sql_kayit, (self.email_giris, self.sifre_giris, self.numara_giris,self.kilo_giris,self.boy_giris,self.tarih_giris))
                    self.mydb.commit()
                    print("Kayıt Başarılı")
                    login_msgbox("Tebrikler!", "Tebrikler! Kayıt başarılı.", "information",window)
                except mysql.connector.Error as err:
                    print(err)
                    login_msgbox("Hata!", "Server hatası!", "error",window)

    def giris_yapma(self):
        self.veritabani()
        self.true_kullanici_adi = self.entry_1.get()
        self.true_sifre = self.entry_2.get()

        if self.true_kullanici_adi:
            self.sql_giris = "select * from kullanicilar where kullanici_adi = %s and sifre = %s"
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute(self.sql_giris, (self.true_kullanici_adi, self.true_sifre))
            self.myresult = self.mycursor.fetchone()

            if self.myresult is not None:
                self.id = self.myresult[0]
                window.destroy()
                self.kullanici_pencere()
            else:
                login_msgbox("HATA!", "Kullanıcı adı veya şifre yanlış!", "warning", window)
        else:
            login_msgbox("HATA!", "Kullanıcı adı boş olamaz!", "warning", window)
##################################  KULLANICI PENCERESİ VE FONKSİYONLARI   #####################################
    def kullanici_pencere(self):

        self.antrenman_window = Tk()

        self.antrenman_window.geometry("1100x600")
        self.antrenman_window.configure(bg="#22348f")
        self.antrenman_window.title("Spor Hayattır")


        self.table_frame1 = Frame(self.antrenman_window, bd=10, relief=RIDGE, bg="#70a6cf")
        self.table_frame1.place(x=300, y=10, width=800, height=590)

        self.scroll_x1 = ttk.Scrollbar(self.table_frame1, orient=HORIZONTAL)
        self.scroll_y1 = ttk.Scrollbar(self.table_frame1, orient=VERTICAL)
        self.antrenman_tablo = ttk.Treeview(self.table_frame1, columns=("Gün", "1", "2", "3",
                                                                  "4", "5", "6"),
                                       xscrollcommand=self.scroll_x1.set, yscrollcommand=self.scroll_y1.set)

        self.scroll_x1.pack(side=BOTTOM, fill=X)
        self.scroll_y1.pack(side=RIGHT, fill=Y)

        self.scroll_x1.config(command=self.antrenman_tablo.xview)
        self.scroll_y1.config(command=self.antrenman_tablo.yview)

        self.antrenman_tablo.heading("Gün", text="Gün", anchor=W)
        self.antrenman_tablo.heading("1", text="1.Hareket", anchor=W)
        self.antrenman_tablo.heading("2", text="2.Hareket", anchor=W)
        self.antrenman_tablo.heading("3", text="3.Hareket", anchor=W)
        self.antrenman_tablo.heading("4", text="4.Hareket", anchor=W)
        self.antrenman_tablo.heading("5", text="5.Hareket", anchor=W)
        self.antrenman_tablo.heading("6", text="6.Hareket", anchor=W)

        self.antrenman_tablo.column("Gün", width=80)
        self.antrenman_tablo.column("1", width=150)
        self.antrenman_tablo.column("2", width=150)
        self.antrenman_tablo.column("3", width=160)
        self.antrenman_tablo.column("4", width=150)
        self.antrenman_tablo.column("5", width=150)
        self.antrenman_tablo.column("6", width=150)


        self.antrenman_tablo["show"] = "headings"
        self.antrenman_tablo.pack(fill=BOTH, expand=1)


        self.kalori_buton_image = PhotoImage(
            file=relative_to_assets("kirala.png"))
        self.kalori_buton = Button(
            image=self.kalori_buton_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.kalori_sayfa,
            relief="flat",
        )
        self.kalori_buton.place(
            x=20.0,
            y=15.0,
            width=205.0,
            height=44.0
        )

        self.bilgi_image = PhotoImage(
            file=relative_to_assets("bilgi.png"))
        self.bilgi = Button(
            image=self.bilgi_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.ilerleme,
            relief="flat"
        )
        self.bilgi.place(
            x=20.0,
            y=85.0,
            width=205.0,
            height=44.0
        )

        antrenman_label = Label(self.antrenman_window, text="Antrenman Seviyeleri", fg="black", font=("KumarOne Regular", 15),bg="White").place(x=50, y=230)


        self.giris=IntVar()
        self.orta=IntVar()
        self.ileri=IntVar()

        self.c_giris = tk.Checkbutton(self.antrenman_window, text='Giriş Seviyesi',variable=self.giris,
                                      onvalue=1, offvalue=0,bg='#84db32',command=self.giris_call)
        self.c_giris.place(x=90, y = 300)
        self.c_orta = tk.Checkbutton(self.antrenman_window, text='Orta Seviye  ',variable=self.orta
                                     ,onvalue=1, offvalue=0, bg='#f5e025',command=self.orta_call)
        self.c_orta.place(x=90, y=350)
        self.c_ileri = tk.Checkbutton(self.antrenman_window, text='İleri Seviye    ',variable=self.ileri
                                      , onvalue=1, offvalue=0, bg='#db4223',command=self.ileri_call)
        self.c_ileri.place(x=90, y=400)


        self.antrenman_window.resizable(False, False)
        self.antrenman_window.mainloop()

    def tablo_doldurma(self,veri,):
        self.veritabani()
        self.sql = f"Select * from antrenman where seviye='{veri}'"
        self.my_cursor1 = self.mydb.cursor()
        self.my_cursor1.execute(self.sql, )

        self.rows = self.my_cursor1.fetchall()

        if len(self.rows) >= 0:
            self.antrenman_tablo.delete(*self.antrenman_tablo.get_children())
            for i in self.rows:
                self.antrenman_tablo.insert("", END, values=i)
            self.mydb.commit()

    def giris_call(self):
        if self.giris.get() == 1:
            self.orta.set(0)
            self.ileri.set(0)
            self.tablo_doldurma("giris")

    def orta_call(self):
        if self.orta.get() == 1:
            self.giris.set(0)
            self.ileri.set(0)
            self.tablo_doldurma("orta")

    def ileri_call(self):
        if self.ileri.get() == 1:
            self.giris.set(0)
            self.orta.set(0)
            self.tablo_doldurma("ileri")

    def ilerleme(self):
        self.antrenman_window.destroy()
        self.ilerleme_penceresi()

    ##################################  İLERLEME PENCERESİ VE FONKSİYONLARI   #####################################

    def ilerleme_penceresi(self):
        self.ilerleme_window = Tk()

        self.ilerleme_window.geometry("800x500")
        self.ilerleme_window.configure(bg="#22348f")
        self.ilerleme_window.title("İlerleme Bilgi")


        self.ilerleme_canvas = Canvas(
            self.ilerleme_window,
            bg = "#22348f",
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.ilerleme_canvas.place(x = 0, y = 0)
        self.kilo_resim = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.kilo_bg = self.ilerleme_canvas.create_image(
            130.0,
            135.5,
            image=self.kilo_resim
        )
        self.kilo_ent = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.kilo_ent.place(
            x=49.0,
            y=119.0,
            width=162.0,
            height=33.0
        )
        self.boy_resim = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.boy_bg = self.ilerleme_canvas.create_image(
            130.0,
            207.5,
            image=self.boy_resim
        )
        self.boy_ent = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.boy_ent.place(
            x=49.0,
            y=190.0,
            width=162.0,
            height=35.0
        )
        self.tarih_resim = PhotoImage(
            file=relative_to_assets("re.png"))
        self.tarih_bg = self.ilerleme_canvas.create_image(
            130.0,
            276.5,
            image=self.tarih_resim
        )

        self.tarih_ent = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.tarih_ent.place(
            x=49.0,
            y=261.0,
            width=162.0,
            height=35.0
        )

        self.kilo_text = self.ilerleme_canvas.create_text(
            33.0,
            98.0,
            anchor="nw",
            text=" Kilo:",
            fill="White",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.giveup_text = self.ilerleme_canvas.create_text(
            350.0,
            20.0,
            anchor="nw",
            text=" İLERMENİ KENDİ GÖZÜNLE GÖR!",
            fill="WHITE",
            font=("JetBrainsMonoRoman ExtraBold", 25 * -1)
        )
        self.boy_text = self.ilerleme_canvas.create_text(
            33.0,
            170.0,
            anchor="nw",
            text=" Boy:",
            fill="White",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.tarih_text = self.ilerleme_canvas.create_text(
            33.0,
            237.0,
            anchor="nw",
            text=" Tarih:",
            fill="White",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.kaydet_resim = PhotoImage(
            file=relative_to_assets("gerigel.png"))
        self.kaydet = Button(
            image=self.kaydet_resim,
            borderwidth=0,
            highlightthickness=0,
            command=self.kaydet_button,
            relief="flat"
        )
        self.kaydet.place(
            x=200.0,
            y=370.0,
            width=120.0,
            height=50.0,

        )
        self.geridon_resim = PhotoImage(
            file=relative_to_assets("ana sayfa.png"))
        self.geridon = Button(
            image=self.geridon_resim,
            borderwidth=0,
            highlightthickness=0,
            command=self.ana_sayfa_don,
            relief="flat"
        )
        self.geridon.place(
            x=0.0,
            y=0.0,
            width=120.0,
            height=50.0,

        )



        self.table_frame11 = Frame(self.ilerleme_window, bd=10, relief=RIDGE, bg="#70a6cf")
        self.table_frame11.place(x=340,y=55,width=460,height=400)

        self.scroll_x = ttk.Scrollbar(self.table_frame11, orient=HORIZONTAL)
        self.scroll_y = ttk.Scrollbar(self.table_frame11, orient=VERTICAL)
        self.ilerleme_tablo = ttk.Treeview(self.table_frame11, columns=("boy", "kilo", "tar"),
                                            xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.scroll_x.config(command=self.ilerleme_tablo.xview)
        self.scroll_y.config(command=self.ilerleme_tablo.yview)

        self.ilerleme_tablo.heading("boy", text="Kilonuz", anchor=W)
        self.ilerleme_tablo.heading("kilo", text="Boyunuz", anchor=W)
        self.ilerleme_tablo.heading("tar", text="Tarih", anchor=W)


        self.ilerleme_tablo.column("boy", width=80)
        self.ilerleme_tablo.column("kilo", width=150)
        self.ilerleme_tablo.column("tar", width=150)
        self.ilerleme_veri_aktarimi()
        self.ilerleme_tablo["show"] = "headings"
        self.ilerleme_tablo.pack(fill=BOTH, expand=1)

    def ilerleme_veri_aktarimi(self):
        self.sql_veri_aktarimi=f"select kilo,boy,tarih from kullanicilar where id={self.id} order by tarih asc "
        self.my_cursor = self.mydb.cursor()
        self.my_cursor.execute(self.sql_veri_aktarimi)
        self.rows=self.my_cursor.fetchall()
        if len(self.rows)!=0:
            self.ilerleme_tablo.delete(*self.ilerleme_tablo.get_children())
            for i in self.rows:
                self.ilerleme_tablo.insert("",END,values=i)
            self.mydb.commit()

    def kaydet_button(self):
        kilo = self.kilo_ent.get()
        boy = self.boy_ent.get()
        tarih = self.tarih_ent.get()

        self.my_cursor = self.mydb.cursor()
        if not kilo.strip() or not boy.strip() or not tarih.strip():
            login_msgbox("HATA!", "Tüm alanları doldurun!", "warning", self.ilerleme_window)
        else:
            sql = "INSERT INTO kullanicilar (id, kilo, boy, tarih) VALUES (%s, %s, %s, %s)"
            self.my_cursor.execute(sql, (self.id, kilo, boy, tarih))
            self.mydb.commit()
            login_msgbox("Tebrikler!", "Kayıt başarılı!", "information", self.ilerleme_window)
            self.ilerleme_veri_aktarimi()

    def ana_sayfa_don(self):
        self.ilerleme_window.destroy()
        self.kullanici_pencere()

    def kalori_sayfa(self):
        self.ilerleme_window = Tk()

        self.ilerleme_window.geometry("550x400")
        self.ilerleme_window.configure(bg="#22348f")
        self.ilerleme_window.title("Besin Değerleri")

        self.table_frame_kalori = Frame(self.ilerleme_window, bd=5, relief=RIDGE, bg="#70a6cf")
        self.table_frame_kalori.place(x=0, y=0, width=550, height=400)

        self.scrollx = ttk.Scrollbar(self.table_frame_kalori, orient=HORIZONTAL)
        self.scrolly = ttk.Scrollbar(self.table_frame_kalori, orient=VERTICAL)
        self.kalori_tablo = ttk.Treeview(self.table_frame_kalori, columns=("Yiyecek", "Miktar", "Kalori"),
                                       xscrollcommand=self.scrollx.set, yscrollcommand=self.scrolly.set)

        self.scrollx.pack(side=BOTTOM, fill=X)
        self.scrolly.pack(side=RIGHT, fill=Y)

        self.scrollx.config(command=self.kalori_tablo.xview)
        self.scrolly.config(command=self.kalori_tablo.yview)


        self.kalori_tablo.heading("Yiyecek", text="Yiyecek", anchor=W)
        self.kalori_tablo.heading("Miktar", text="Miktar", anchor=W)
        self.kalori_tablo.heading("Kalori", text="Besin Değerleri", anchor=W)

        self.kalori_tablo.column("Yiyecek", width=0)
        self.kalori_tablo.column("Miktar", width=0)
        self.kalori_tablo.column("Kalori", width=150)

        ##### veri tabanı bağlantısı ########3
        self.veritabani()
        self.sql = f"Select * from kaloriler"
        self.my_cursor1 = self.mydb.cursor()
        self.my_cursor1.execute(self.sql, )

        self.rows = self.my_cursor1.fetchall()
        if len(self.rows) >= 0:
            self.kalori_tablo.delete(*self.kalori_tablo.get_children())
            for i in self.rows:
                self.kalori_tablo.insert("", END, values=i)
            self.mydb.commit()

        self.kalori_tablo["show"] = "headings"
        self.kalori_tablo.pack(fill=BOTH, expand=1)


app=Uygulama()
