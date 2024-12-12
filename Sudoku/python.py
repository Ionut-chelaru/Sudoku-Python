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
from tkinter import messagebox
import random as rand
import json
import os

height = 530
width = 800
class Sudoku(ctk.CTk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position to center the window
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Set the geometry of the window
        self.geometry(f"{width}x{height}+{x}+{y}")

        self.title('Sudoku')
        # self.iconbitmap("icon.ico") 
        self.menu_bar = tk.Menu(self)
        
        self.menu = tk.Menu(self.menu_bar, tearoff=0)
        
        self.menu_bar.add_cascade(label="Menu", menu=self.menu)

        self.config(menu=self.menu_bar)

        self.afisare_acasa()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)    
        self.grid_rowconfigure(5, weight=1)

        self.test_grid = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]
        ]


        self.mistakes_count = 0  
        self.mistakes_var = ctk.StringVar(value=f"Greseli = {self.mistakes_count}")

        self.entries = []  
        self.global_sudoku_grid = self.genereaza_subgridul()

    ########## home screen ##########

    def afisare_acasa(self):
        self.curata_ecran()
        Titlu = ctk.CTkLabel(self,text='SUDOKU',font=('Century Gothic', 40))
        Titlu.grid(row=0, column=0, padx=0, pady=0)

        Credits = ctk.CTkLabel(self,text='Realizat de: Ionut Chelaru\nPersonal project',font=('Century Gothic', 10))
        Credits.grid(row=5, column=0, padx=0, pady=0)

        menu_button = ctk.CTkButton(self, text="Intra in joc", command=self.afisare_meniu,font=("Ariel",14,'bold'))
        menu_button.grid(row=1, column=0, padx=0, pady=0)
        exist_game = ctk.CTkButton(self, text="Iesi din joc", command=self.inchide_fereastra,font=("Ariel",14,'bold'))
        exist_game.grid(row=2, column=0, padx=0, pady=10)

    ########### Menu ################

    def afisare_meniu(self):
        self.curata_ecran()
        self.grid_rowconfigure(2, weight=0)  
        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=0)  
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=1)    
        self.grid_rowconfigure(5, weight=1)
        Titlu = ctk.CTkLabel(self,text='SUDOKU',font=('Century Gothic', 40))
        Titlu.grid(row=0, column=0, padx=0, pady=0)


        option1_button = ctk.CTkButton(self, text="Incepe joc nou", command=self.incepe_jocul,font=("Ariel",14,'bold'))
        option1_button.grid(row=1, column=0, padx=0, pady=0)
        option1_button = ctk.CTkButton(self, text="Continua joc", command=self.save_game,font=("Ariel",14,'bold'),state='active')
        option1_button.grid(row=2, column=0, padx=0, pady=10)

        if os.path.exists("saved_game.json") and os.path.getsize("saved_game.json") > 0:
            option2_button = ctk.CTkButton(self, text="Continua joc", command=self.load_game, font=("Ariel", 14, 'bold'))
            option2_button.grid(row=2, column=0, padx=0, pady=0)
        else:
            option2_button = ctk.CTkButton(self, text="Continua joc", state='disabled', font=("Ariel", 14, 'bold'))
            option2_button.grid(row=2, column=0, padx=0, pady=10)
        option3_button = ctk.CTkButton(self, text="Iesire", command=self.inchide_fereastra,font=("Ariel",14,'bold'))
        option3_button.grid(row=4, column=0, padx=10, pady=0)

    def incepe_jocul(self):
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
            self.after(1000, self.tranzitie_meniu_joc, label,50)
        if value == 2:
            label = ctk.CTkLabel(self, text="Dificultatea medium", font=("Century Gothic", 20,'bold'))
            label.grid(row=1, column=0, padx=0, pady=0)
            self.after(1000, self.tranzitie_meniu_joc, label,40)
        if value == 3:
            label = ctk.CTkLabel(self, text="Dificultatea hard", font=("Century Gothic", 20,'bold'))
            label.grid(row=1, column=0, padx=0, pady=0)
            self.after(1000, self.tranzitie_meniu_joc, label,30)

    def optiuni(self):
        self.curata_ecran()
        label = ctk.CTkLabel(self, text="Optiuni", font=("Century Gothic", 20))
        label.grid(row=0, column=0, padx=0, pady=0)
        
        button = ctk.CTkButton(self, text="Inapoi", command=self.afisare_meniu)
        button.grid(row=1, column=0, padx=0, pady=0)

    ######### Extra ################

    def curata_ecran(self):
        for widget in self.winfo_children():
            widget.destroy()

    def inchide_fereastra(self):
        self.destroy()

    def tranzitie_meniu_joc(self, label,default_count):

        label.grid_forget()
        self.mistakes_count = 0
        self.mistakes_var.set(f"Greseli = {self.mistakes_count}")

        self.creare_grila(default_count)

    def e_numar(self, value):
        return value == "" or (value.isdigit() and value != "0")

    def roteste_subgridul(self):
        grid = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]
        ]
        for i in range(0, 9, 3):
            block = grid[i:i + 3]
            rand.shuffle(block)
            grid[i:i + 3] = block

        for i in range(3):
            cols = [grid[row][i:i + 3] for row in range(9)]
            rand.shuffle(cols)
            for j in range(9):
                grid[j][i:i + 3] = cols[j]
        
        return grid

    def genereaza_subgridul(self):
        base = 3
        side = base * base

        def pattern(r, c): return (base * (r % base) + r // base + c) % side
        def shuffle(s): return rand.sample(s, len(s))

        r_base = range(base)
        rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
        cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
        nums = shuffle(range(1, side + 1))

        board = [[nums[pattern(r, c)] for c in cols] for r in rows]

        return board  

    def opreste_focusarea(self, entry):
        entry.icursor(0)  # Move the cursor to the start
        entry.select_clear()  # Clear any selection

        self.focus_set()

    def schimbare_stare_citire(self, entry):
        if entry.get() != "":  
            entry.config(state="readonly")  

    def la_apasare_tastatura(self, event, entries):
        number = int(event.char)
        if 1 <= number <= 9:
            self.introducere_numar(entries, number)

    def valideaza_intrarea(self, entries, row, col, value):
        if value == "":  
            return True
        if not value.isdigit() or not (1 <= int(value) <= 9):  
            return False
        if int(value) != self.global_sudoku_grid[row][col]:
            return False
        
        return self.introducere_valida(entries, row, col, value)

    def introducere_valida(self, entries, row, col, value):
        value = str(value)
        for c in range(9):
            if c != col and entries[row][c].get() == value:
                return False
        for r in range(9):
            if r != row and entries[r][col].get() == value:
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if (r != row or c != col) and entries[r][c].get() == value:
                    return False
        return True

    def populeaza_intrari(self, entries, default_count,from_load=False):
        self.default_entries = {}  # Track default entries
        positions = [(r, c) for r in range(9) for c in range(9)]
        if from_load is False:
            print('se randomizeaza acum')
            rand.shuffle(positions)
        
        count = 0
        for r, c in positions:
            if count < default_count:
                value = self.global_sudoku_grid[r][c]  
                entries[r][c].delete(0, tk.END)  
                entries[r][c].insert(0, str(value))  
                entries[r][c].config(state="disable")  
                entries[r][c].config(foreground="#ff6361")  
                self.default_entries[(r, c)] = True  
                count += 1
            else:
                self.default_entries[(r, c)] = False  

    def introducere_numar(self, entries, number):
        self.selected_number = number  
        self.evidentiaza_culori(entries)
        for row in entries:
            for entry in row:
                if entry.focus_get() == entry:  
                    entry_value = str(number)
                    row_index = entries.index(row)
                    col_index = row.index(entry)

                    if not self.valideaza_intrarea(entries, row_index, col_index, entry_value):
                        self.mistakes_count += 1
                        self.mistakes_var.set(f"Greseli = {self.mistakes_count}")
                        return

                    entry.delete(0, tk.END)  
                    entry.insert(0, entry_value)  
                    self.schimbare_stare_citire(entry)
                    self.verificare_completare(entries)
                    return
                
    # def update_number_count(self, entries):
    # # Initialize a dictionary to store the count of each number (1-9)
    #     count_dict = {str(i): 0 for i in range(1, 10)}

    # # Count how many times each number appears in the grid
    #     for row in entries:
    #         for entry in row:
    #             value = entry.get()
    #             if value in count_dict:
    #                 count_dict[value] += 1

    #     for i in range(9):
    #     # Update the StringVar with the number and the count
    #        new_text = f"{i + 1}\n{count_dict[str(i + 1)]}"
    #        self.number_vars[i].set(new_text)  # Update the text for this button

    def evidentiaza_culori(self, entries):
        for r, row in enumerate(entries):
            for c, entry in enumerate(row):
                if entry.get() == str(self.selected_number):
                    if self.default_entries.get((r, c), False):
                        entry.config(foreground="white")  
                    else:
                        entry.config(foreground="white")  
                else:
                    if self.default_entries.get((r, c), False):
                        entry.config(foreground="#ff6361")  
                    else:
                        entry.config(foreground="#ffa600")  

    def resetare_la_meniu(self):
        result = messagebox.askyesno("Salvati Progresul", "Doriti sa salvati progresul?",)
        
        if result:  
            self.save_game()  
            self.afisare_meniu()
            self.global_sudoku_grid = self.genereaza_subgridul()
            self.schimba_fundal()
        else:  
            with open("saved_game.json", "w") as file:
                file.truncate()
            self.afisare_meniu()
            self.global_sudoku_grid = self.genereaza_subgridul()
            self.schimba_fundal()

    def load_game(self):
        try:
            with open("saved_game.json", "r") as f:
                game_state = json.load(f)
            
            self.global_sudoku_grid = game_state["board"]
            self.mistakes_count = game_state["mistakes_count"]
            self.mistakes_var.set(f"Greseli = {self.mistakes_count}")
            self.creare_grila(populate_on_create=False, from_load=True)            
            # self.creare_grila()  
            # self.populeaza_intrari(self.entries, 0,from_load=True)  
            print("Game loaded successfully")

        except FileNotFoundError:
            print("No saved game found.")

    def schimba_fundal(self):
            self.config(bg='#282424')

    def verificare_completare(self,entries):
        row_index = 0
        for row in entries:  
            col_index = 0
            for entry in row:  
                if not isinstance(entry, tk.Entry):
                    raise TypeError(f"Expected Entry widget, but got {type(entry)} at row {row_index}, column {col_index}")
                value = entry.get().strip()
                if value == "":  
                    return False
                col_index += 1
            row_index += 1
        self.felicitari()
        return True

    def felicitari(self):
        self.curata_ecran()
        label = ctk.CTkLabel(self,text= 'nice')
        label.grid(row = 0,column = 0)


    def save_game(self):
        game_state = {
            "board": self.global_sudoku_grid,
            "mistakes_count": self.mistakes_count
        }

        with open("saved_game.json", "w") as f:
            json.dump(game_state, f)
        print("Game saved successfully")


    ########## JOCUL ############
    def creare_grila(self, default_count=50,populate_on_create =True,from_load = False):
        self.curata_ecran()
        self.config(bg='#00202e')

        grid_frame = tk.Frame(self, bg="#003f5c", bd=2, relief="solid")
        grid_frame.grid(row=0, column=0, sticky='n', padx=20, pady=20)

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

        for subgrid_row in range(3):  
            for subgrid_col in range(3):  
                subgrid_frame = tk.Frame(grid_frame, bg="#2c4875", bd=1, relief="solid")
                subgrid_frame.grid(row=subgrid_row, column=subgrid_col, padx=5, pady=5)

                for i in range(3): 
                    for j in range(3):
                        global_row = subgrid_row * 3 + i  
                        global_col = subgrid_col * 3 + j  

                        validate_cmd = self.register(lambda value, r=global_row, c=global_col: self.valideaza_intrarea(entries, r, c, value))
                        entry = ttk.Entry(
                            subgrid_frame, 
                            width=2, 
                            justify='center', 
                            font=('Arial', 18),
                            style='Custom.TEntry',
                            validate="key", 
                            validatecommand=(validate_cmd, '%P')
                        )
                        entry.bind("<FocusIn>", lambda event, entry=entry: entry.focus_set())
                        entry.bind("<KeyRelease>", lambda event, entry=entry: self.schimbare_stare_citire(entry))
                        entry.bind("<Escape>", lambda event, e=entry: self.opreste_focusarea(entry))
                        entry.bind("<Key>", lambda event, ents=entries: self.la_apasare_tastatura(event, ents))
                        entry.grid(
                            row=i,
                            column=j,
                            padx=(2 if j % 3 == 0 else 1, 2 if j == 2 else 1),  
                            pady=(2 if i % 3 == 0 else 1, 2 if i == 2 else 1)   
                        )

                        if global_row >= len(entries):
                            entries.append([entry])  
                        else:
                            entries[global_row].append(entry)  

        bottom_frame = ctk.CTkFrame(self, fg_color="#3d5378", border_width=0, corner_radius=5)
        bottom_frame.grid(row=2, column=0, sticky="nsew", rowspan=6)
        label = tk.Label(self, textvariable=self.mistakes_var,bg='#00202e',font=('Arial',16),fg='#9dad7f')
        label.grid(row = 1,column = 0,pady=(0,30))
        button1 = ctk.CTkButton(self,
                                text='Inapoi',
                                command= lambda: self.resetare_la_meniu(),
                                height = 30,
                                width=100,
                                fg_color='#d74a49',
                                text_color='black',
                                font=("Ariel", 14, 'bold'),
                                hover_color='#852a2a'
                                )
        col = 0
        
        for i in range(9):
            # var = ctk.StringVar(value=f"{i+1}\n0")
            # var.set(f"{i+1}\n1")
            button = ctk.CTkButton(
                bottom_frame, 
                # textvariable=var,
                text=f"{col+1}",
                fg_color='#ffa600',
                text_color='black',
                height=30,
                hover_color='#9e6500',
                font=("Ariel", 14, 'bold'),
                width=55,
                command=lambda num=col+1: self.introducere_numar(entries, num)
            )
            button.grid(row=1, column=col, padx=17, pady=20)
            button1.grid(row=0,column=0,pady = 30,padx = 30,sticky = 'wn')
            col += 1
        

        if populate_on_create or from_load:
            self.populeaza_intrari(entries, default_count,from_load=from_load)
        self.entries = entries  
        return entries

Aplicatie = Sudoku()
Aplicatie.mainloop()