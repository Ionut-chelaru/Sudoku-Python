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


    # def creare_grila(self,default_count=10):
    #     self.curata_ecran()
    #     self.config(bg='#00202e')

    #     grid_frame = tk.Frame(self,bg="#003f5c", bd=2, relief="solid")
    #     grid_frame.grid(row=1, column=0,sticky='n', padx=20, pady=20)
    #     style = ttk.Style(self)
    #     style.theme_use('clam')
    #     style.configure("Custom.TEntry", 
    #             fieldbackground="#2c4875",
    #             foreground="#ffa600",             
    #             borderwidth=2
    #             )          
    #     style.map("Custom.TEntry",
    #           background=[('active', '#5D6D7E'), ('!active', '#2c4875')])        
                

    #     for i in range(9):
    #         grid_frame.grid_columnconfigure(i, weight=0)  
    #         grid_frame.grid_rowconfigure(i, weight=0)     

    #     entries = [] 
    #     for subgrid_row in range(3):
    #         for subgrid_col in range(3):
    #             # Create a frame for each 3x3 subgrid
    #             subgrid_frame = tk.Frame(grid_frame, bg="#2c4875", bd=1, relief="solid")
    #             subgrid_frame.grid(
    #                 row=subgrid_row,
    #                 column=subgrid_col,
    #                 padx=5,  # Add spacing between subgrids
    #                 pady=5
    #             )

    #             for i in range(3):
    #                 row_entries = []
    #                 for j in range(3):
    #                     global_row = subgrid_row * 3 + i
    #                     global_col = subgrid_col * 3 + j

    #                     validate_cmd = self.register(lambda value, r=global_row, c=global_col: self.validate_entry(entries, r, c, value))
    #                     entry = ttk.Entry(
    #                         subgrid_frame, 
    #                         width=2, 
    #                         justify='center', 
    #                         font=('Arial', 18),
    #                         style='Custom.TEntry',
    #                         validate="key", 
    #                         validatecommand=(validate_cmd, '%P')
    #                     )
    #                     entry.bind("<FocusIn>", lambda event, entry=entry: entry.icursor(0))
    #                     entry.bind("<KeyRelease>", lambda event, entry=entry: self.schimbare_stare_citire(entry))
    #                     entry.grid(
    #                         row=i,
    #                         column=j,
    #                         padx=(2 if j % 3 == 0 else 1, 2 if j == 8 else 1),
    #                         pady=(2 if i % 3 == 0 else 1, 2 if i == 8 else 1)
    #                         )                   
    #                     row_entries.append(entry)
    #             entries.append(row_entries)     
    #             print("Entries structure after creation:")
    #             for row_index, row in enumerate(entries):
    #                 print(f"Row {row_index}: {[entry for entry in row]}")

    #     self.grid_rowconfigure(2, weight=2)  
    #     self.grid_columnconfigure(0, weight=1)  
    #     self.grid_columnconfigure(1, weight=0)  
    #     self.grid_columnconfigure(2, weight=0)

    #     bottom_frame = ctk.CTkFrame(self, fg_color="#3d5378", border_width=0,corner_radius=5)
    #     bottom_frame.grid(row=2, column=0, sticky="nsew",rowspan=6)
    #     col = 0
    #     for i in range(9):
    #         button = ctk.CTkButton(
    #             bottom_frame, 
    #             text=f"{col+1}",
    #             fg_color='#ffa600',
    #             text_color='black',
    #             height=40,
    #             hover_color='#145a32',
    #             font=("Ariel",14,'bold'),
    #             width=60,
    #             command=lambda num=col+1: self.fill_entry_with_number(entries, num))
    #         button.grid(row=0, column=+col, padx=15, pady=50)
    #         col+=1
    #     self.populate_defaults(entries, default_count)        
    #     print("Entries after populating defaults:")
    #     for row_index, row in enumerate(entries):
    #         print(f"Row {row_index}: {[entry.get() for entry in row]}")
    #     self.entries = entries  
    #     return entries
    def creare_grila(self, default_count=10):
        self.curata_ecran()
        self.config(bg='#00202e')

        grid_frame = tk.Frame(self, bg="#003f5c", bd=2, relief="solid")
        grid_frame.grid(row=1, column=0, sticky='n', padx=20, pady=20)

        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure("Custom.TEntry", 
                        fieldbackground="#2c4875",
                        foreground="#ffa600",             
                        borderwidth=2
                        )          
        style.map("Custom.TEntry",
                background=[('active', '#5D6D7E'), ('!active', '#2c4875')])        

        # Configure grid layout for 9 columns and 9 rows
        for i in range(9):
            grid_frame.grid_columnconfigure(i, weight=0)  
            grid_frame.grid_rowconfigure(i, weight=0)

        entries = []  # To store 9x9 grid of entries

        # Create 9 subgrids (3x3 layout)
        for subgrid_row in range(3):  # Rows of subgrids
            for subgrid_col in range(3):  # Columns of subgrids
                # Create a frame for each 3x3 subgrid
                subgrid_frame = tk.Frame(grid_frame, bg="#2c4875", bd=1, relief="solid")
                subgrid_frame.grid(row=subgrid_row, column=subgrid_col, padx=5, pady=5)

                # Create entries inside each subgrid and add them to the global `entries` list
                for i in range(3):  # 3 rows in a subgrid
                    for j in range(3):  # 3 columns in a subgrid
                        global_row = subgrid_row * 3 + i  # Global row index
                        global_col = subgrid_col * 3 + j  # Global column index

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
                            padx=(2 if j % 3 == 0 else 1, 2 if j == 2 else 1),  # Padding between entries
                            pady=(2 if i % 3 == 0 else 1, 2 if i == 2 else 1)   # Padding between entries
                        )

                        # Ensure `entries` is a 9x9 grid and append entry in the right position
                        if global_row >= len(entries):
                            entries.append([entry])  # Add a new row if it doesn't exist
                        else:
                            entries[global_row].append(entry)  # Append entry to the right row

        print("Entries structure after creation:")
        for row_index, row in enumerate(entries):
            print(f"Row {row_index}: {[entry for entry in row]}")

        # Adjust bottom buttons for controlling the grid
        bottom_frame = ctk.CTkFrame(self, fg_color="#3d5378", border_width=0, corner_radius=5)
        bottom_frame.grid(row=2, column=0, sticky="nsew", rowspan=6)
        col = 0
        for i in range(9):
            button = ctk.CTkButton(
                bottom_frame, 
                text=f"{col+1}",
                fg_color='#ffa600',
                text_color='black',
                height=40,
                hover_color='#145a32',
                font=("Ariel", 14, 'bold'),
                width=60,
                command=lambda num=col+1: self.fill_entry_with_number(entries, num)
            )
            button.grid(row=0, column=col, padx=15, pady=50)
            col += 1

        self.populate_defaults(entries, default_count)

        print("Entries after populating defaults:")
        for row_index, row in enumerate(entries):
            print(f"Row {row_index}: {[entry.get() for entry in row]}")

        self.entries = entries  # Store reference to entries
        return entries
 

    def validate_entry(self, entries, row, col, value):
        if value == "":  # Allow clearing a cell
            return True

        if not value.isdigit() or not (1 <= int(value) <= 9):  
            return False

        return self.is_valid_move(entries, row, col, value)

    def is_valid_move(self, entries, row, col, value):
        """
        Validates whether placing the value at (row, col) is allowed under Sudoku rules.
        """
        # Convert value to string for comparison
        value = str(value)

        # Check the row
        for c in range(9):
            if c != col and entries[row][c].get() == value:
                return False

        # Check the column
        for r in range(9):
            if r != row and entries[r][col].get() == value:
                return False

        # Check the 3x3 subgrid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if (r != row or c != col) and entries[r][c].get() == value:
                    return False

        return True

    def populate_defaults(self, entries, default_count):
        """
        Populates the Sudoku grid with random numbers adhering to Sudoku rules.
        """
        filled_positions = set()  # Track already filled positions

        while len(filled_positions) < default_count:
            row = rand.randint(0, 8)
            col = rand.randint(0, 8)
            if (row, col) in filled_positions:  # Skip already filled cells
                continue

            number = str(rand.randint(1, 9))
            if self.is_valid_move(entries, row, col, number):  # Check validity
                entries[row][col].insert(0, number)
                entries[row][col].configure(state="disabled")  # Lock default cells
                filled_positions.add((row, col))


    def fill_entry_with_number(self, entries, number):
        """
        Inserts the given number into the currently focused entry if it's valid.
        """
        for row in entries:
            for entry in row:
                if entry.focus_get() == entry:  # Check if this entry has focus
                    entry_value = str(number)
                    row_index = entries.index(row)
                    col_index = row.index(entry)

                    if self.is_valid_move(entries, row_index, col_index, entry_value):
                        entry.delete(0, tk.END)  # Clear current value
                        entry.insert(0, entry_value)  # Insert the new number
                    return

    def get_subgrid_index(self, row, col):
        return (row // 3, col // 3)

    def resetare_la_meniu(self):
        self.afisare_meniu()
        self.change_background()

    def change_background(self):
            self.config(bg='#282424')

Aplicatie = Sudoku()
Aplicatie.mainloop()