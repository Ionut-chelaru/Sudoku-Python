#Sudoku game

#needs to include:
#Multiple dificulties 
#Modern UI
#Sounds
#Server elemtets

#May include:
#Mascot
#Language support
#Leatherboard

import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

height = '500'
width = '800'
class Sudoku(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(width+'x'+height)
        self.title('Sudoku')
        self.iconbitmap("icon.ico") 
        self.menu_bar = tk.Menu(self)
        
        self.menu = tk.Menu(self.menu_bar, tearoff=0)
        
        self.menu_bar.add_cascade(label="Menu", menu=self.menu)

        self.config(menu=self.menu_bar)

        self.afisare_acasa()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)    
        self.grid_rowconfigure(5, weight=1)

    def curata_ecran(self):
        for widget in self.winfo_children():
            widget.destroy()


    ######## Home screen ############
    def afisare_acasa(self):
        self.curata_ecran()
        Welcome_text = ctk.CTkLabel(self,text='SUDOKU',font=('Century Gothic', 40))
        Welcome_text.grid(row=0, column=0, padx=0, pady=0)

        Credits = ctk.CTkLabel(self,text='Realizat de: Ionut Chelaru\nPersonal project',font=('Century Gothic', 10))
        Credits.grid(row=5, column=0, padx=0, pady=0)

        menu_button = ctk.CTkButton(self, text="Intra in joc", command=self.afisare_meniu,font=("Ariel",14,'bold'))
        menu_button.grid(row=1, column=0, padx=0, pady=0)
        exist_game = ctk.CTkButton(self, text="Iesi din joc", command=self.inchide_fereastra,font=("Ariel",14,'bold'))
        exist_game.grid(row=2, column=0, padx=0, pady=10)
    ########### Menu ################
    def afisare_meniu(self):
        self.curata_ecran()
        Welcome_text = ctk.CTkLabel(self,text='SUDOKU',font=('Century Gothic', 40))
        Welcome_text.grid(row=0, column=0, padx=0, pady=0)


        option1_button = ctk.CTkButton(self, text="Incepe joc nou", command=self.Incepe_jocul,font=("Ariel",14,'bold'))
        option1_button.grid(row=1, column=0, padx=0, pady=0)
        option1_button = ctk.CTkButton(self, text="Continua joc", command=self.Incepe_jocul,font=("Ariel",14,'bold'),state='disabled')
        option1_button.grid(row=2, column=0, padx=0, pady=(10,0))
        option2_button = ctk.CTkButton(self, text="Optiuni", command=self.Options,font=("Ariel",14,'bold'))
        option2_button.grid(row=3, column=0, padx=0, pady=10)
        option3_button = ctk.CTkButton(self, text="Iesire", command=self.inchide_fereastra,font=("Ariel",14,'bold'))
        option3_button.grid(row=4, column=0, padx=0, pady=0)

    def inchide_fereastra(self):
        self.destroy()



    def Incepe_jocul(self):
        self.curata_ecran()
        label = ctk.CTkLabel(self, text="Alege dificultatea", font=("Century Gothic", 26,'bold'))
        label.grid(row=0, column=0, padx=0, pady=0)
        button2 = ctk.CTkButton(self, text="Easy", command=lambda: self.dificultate(1),fg_color='#229954',text_color='#d0d3d4',height=40,hover_color='#145a32',font=("Ariel",14,'bold'))   
        button2.grid(row=1, column=0, padx=0, pady=0)
        button3 = ctk.CTkButton(self, text="Medium", command=lambda: self.dificultate(2),fg_color='#b7950b',text_color='#d0d3d4',height=40,hover_color='#7d6608',font=("Ariel", 14,'bold'))
        button3.grid(row=2, column=0, padx=0, pady=(10,0))
        button4 = ctk.CTkButton(self, text="Hard", command=lambda: self.dificultate(3),fg_color='#b03a2e',text_color='#d0d3d4',height=40,hover_color='#641e16',font=("Ariel", 14,'bold'))
        button4.grid(row=3, column=0, padx=0, pady=10)
        button1 = ctk.CTkButton(self, text="Inapoi la meniu", command=self.afisare_meniu,font=("Ariel", 14,'bold'))
        button1.grid(row=4, column=0, padx=0, pady=(30,0))


    def dificultate(self,value):
        self.curata_ecran()
        if value == 1:
            label = ctk.CTkLabel(self, text="Dificultatea easy", font=("Century Gothic", 20,'bold'))
            label.grid(row=1, column=0, padx=0, pady=0)
            self.after(1000, self.tranzitie_meniu_joc, label)
        if value == 2:
            label = ctk.CTkLabel(self, text="Dificultatea medium", font=("Century Gothic", 20,'bold'))
            label.grid(row=1, column=0, padx=0, pady=0)
            self.after(1000, self.tranzitie_meniu_joc, label)
        if value == 3:
            label = ctk.CTkLabel(self, text="Dificultatea hard", font=("Century Gothic", 20,'bold'))
            label.grid(row=1, column=0, padx=0, pady=0)
            self.after(1000, self.tranzitie_meniu_joc, label)

    def tranzitie_meniu_joc(self, label):

        label.grid_forget()

        self.creare_grila()

    def Options(self):
        self.curata_ecran()
        label = ctk.CTkLabel(self, text="Optiuni", font=("Century Gothic", 20))
        label.grid(row=0, column=0, padx=0, pady=0)
        
        button = ctk.CTkButton(self, text="Inapoi", command=self.afisare_meniu)
        button.grid(row=1, column=0, padx=0, pady=0)

    def schimbare_stare_citire(self, entry):
        if entry.get() != "":  
            entry.config(state="readonly")  
    def is_digit(self, value):
        return value == "" or value.isdigit()        

    def creare_grila(self):
        self.curata_ecran()
        self.config(bg='#00202e')

        grid_frame = tk.Frame(self,bg="#003f5c", bd=2, relief="solid")
        grid_frame.grid(row=1, column=0,sticky='n', padx=20, pady=20)
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure("Custom.TEntry", 
                fieldbackground="#2c4875",
                foreground="#ffa600",             
                borderwidth=2
                )          
        style.map("Custom.TEntry",
              background=[('active', '#5D6D7E'), ('!active', '#2c4875')])        
                

        for i in range(9):
            grid_frame.grid_columnconfigure(i, weight=0)  
            grid_frame.grid_rowconfigure(i, weight=0)     

        entries = []
        for i in range(9):
            row_entries = []
            for j in range(9):
                validate_cmd = self.register(self.is_digit)
                entry = ttk.Entry(grid_frame, width=2, justify='center', font=('Arial', 18),style='Custom.TEntry',validate="key", validatecommand=(validate_cmd, '%P'))
                entry.bind("<FocusIn>", lambda event, entry=entry: entry.icursor(0))
                entry.bind("<KeyRelease>", lambda event, entry=entry: self.schimbare_stare_citire(entry))
                entry.grid(
                    row=i,
                    column=j,
                    padx=(2 if j % 3 == 0 else 1, 2 if j == 8 else 1),
                    pady=(2 if i % 3 == 0 else 1, 2 if i == 8 else 1)
                )
                
                row_entries.append(entry)
            entries.append(row_entries)

        self.grid_rowconfigure(2, weight=2)  
        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=0)  
        self.grid_columnconfigure(2, weight=0)

        bottom_frame = ctk.CTkFrame(self, fg_color="#ffa600", border_width=0,corner_radius=3)
        bottom_frame.grid(row=2, column=0, sticky="nsew",rowspan=6)
        return entries

Aplicatie = Sudoku()
Aplicatie.mainloop()
