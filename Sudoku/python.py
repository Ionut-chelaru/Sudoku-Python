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
import random as rand

height = '530'
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


        self.mistakes_count = 0  # Track the number of mistakes
        self.entries = []  # Store the entry widgets
        self.global_sudoku_grid = self.generate_random_sudoku_grids(1)

    def curata_ecran(self):
        for widget in self.winfo_children():
            widget.destroy()


    ######## Home screen ############
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
        return value == "" or (value.isdigit() and value != "0")

    def shuffle_subgrids(self):
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

        # Shuffle columns within each subgrid
        for i in range(3):
            cols = [grid[row][i:i + 3] for row in range(9)]
            rand.shuffle(cols)
            for j in range(9):
                grid[j][i:i + 3] = cols[j]
        
        return grid

    def generate_random_sudoku_grids(self,num_grids):
        grids = []
        for _ in range(num_grids):
            shuffled_grid = self.shuffle_subgrids()  # Shuffle the subgrids to generate randomness
            grids.append([row[:] for row in shuffled_grid])  # Append a copy of the shuffled grid
        
        return grids    

    def creare_grila(self, default_count=40):
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
        # style.map("Custom.TEntry",
        #         background=[('active', '#5D6D7E'), ('!active', '#2c4875')])        

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

                        validate_cmd = self.register(lambda value, r=global_row, c=global_col: self.validate_entry(entries, r, c, value))
                        entry = ttk.Entry(
                            subgrid_frame, 
                            width=2, 
                            justify='center', 
                            font=('Arial', 18),
                            style='Custom.TEntry',
                            validate="key", 
                            validatecommand=(validate_cmd, '%P')
                        )
                        entry.bind("<FocusIn>", lambda event, entry=entry: entry.icursor(0))
                        entry.bind("<KeyRelease>", lambda event, entry=entry: self.schimbare_stare_citire(entry))
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
            button = ctk.CTkButton(
                bottom_frame, 
                text=f"{col+1}",
                fg_color='#ffa600',
                text_color='black',
                height=40,
                hover_color='#9e6500',
                font=("Ariel", 14, 'bold'),
                width=60,
                command=lambda num=col+1: self.fill_entry_with_number(entries, num)
            )
            button.grid(row=1, column=col, padx=15, pady=20)
            button1.grid(row=0,column=0,pady = 30,padx = 30,sticky = 'wn')
            col += 1

        self.populate_defaults(entries, default_count)

        self.entries = entries  
        return entries

    def validate_entry(self, entries, row, col, value):
        if value == "":  
            return True

        if not value.isdigit() or not (1 <= int(value) <= 9):  
            return False
        # Check if the value matches the solved grid
        if int(value) != self.test_grid[row][col]:
            # Increment mistakes count and print it to the console
            self.mistakes_count += 1
            print(f"Mistakes: {self.mistakes_count}")
            return False
        
        return self.is_valid_move(entries, row, col, value)

    def is_valid_move(self, entries, row, col, value):
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

    def populate_defaults(self, entries, default_count=15):
        positions = [(r, c) for r in range(9) for c in range(9)]
        
        # Randomly shuffle the list of positions
        rand.shuffle(positions)
        
        # Counter for how many defaults we've populated
        count = 0
        for r, c in positions:
            if count < default_count:
                value = self.test_grid[r][c]  # Get the value from the solved grid
                entries[r][c].delete(0, tk.END)  # Clear any existing value
                entries[r][c].insert(0, str(value))  # Populate the entry with the solved value
                entries[r][c].config(state="disable")  # Disable the entry
                entries[r][c].config(foreground="#ff6361")  # Change text color for default entries
                count += 1
            else:
                break

    def fill_entry_with_number(self, entries, number):
        for row in entries:
            for entry in row:
                if entry.focus_get() == entry:  
                    entry_value = str(number)
                    row_index = entries.index(row)
                    col_index = row.index(entry)

                    if self.is_valid_move(entries, row_index, col_index, entry_value):
                        entry.delete(0, tk.END)  
                        entry.insert(0, entry_value)  
                    return

            

    def resetare_la_meniu(self):
        self.afisare_meniu()
        self.change_background()

    def change_background(self):
            self.config(bg='#282424')

Aplicatie = Sudoku()
Aplicatie.mainloop()