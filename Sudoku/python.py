#Sudoku game

#needs to include:
#Multiple dificulties 
#Modern UI
#Sounds
#Server elemtets

#May include:
#Mascot
#Leatherboard

import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import random as rand
import json
import os
import pywinstyles
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.mixer.init()
pygame.mixer.music.load("game_background.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)

height = 530
width = 800

class Sudoku(ctk.CTk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        pywinstyles.apply_style(style='aero',window=Sudoku)

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
        self.mistakes_var = ctk.StringVar(value=f"Greseli: {self.mistakes_count}")
        self.scor_count = 0
        self.scor_var = ctk.StringVar(value=f"Scor: {self.scor_count}")
        self.time_count = 0
        self.time_var = ctk.StringVar(value=f"Timp: {self.time_count}")

        self.entries = []  
        self.shuffle_positons = []
        self.global_sudoku_grid = self.genereaza_subgridul()
        self.music_slider_value = tk.DoubleVar(value=50)
        self.sound_slider_value = tk.DoubleVar(value=50)

    ########## home screen ##########

    def afisare_acasa(self):
        self.curata_ecran()
        Titlu = ctk.CTkLabel(self,text='SUDOKU',font=('Century Gothic', 40))
        Titlu.grid(row=0, column=0, padx=0, pady=0)

        Credits = ctk.CTkLabel(self,text='Realizat de: Ionut Chelaru\nProiect',font=('Century Gothic', 10))
        Credits.grid(row=5, column=0, padx=0, pady=0)

        menu_button = ctk.CTkButton(self, text="Intra in joc", command=lambda:[self.sounds(1),self.afisare_meniu()],font=("Ariel",14,'bold'))
        menu_button.grid(row=1, column=0, padx=0, pady=0)
        exist_game = ctk.CTkButton(self, text="Iesi din joc", command=lambda:[self.sounds(1),self.inchide_fereastra()],font=("Ariel",14,'bold'))
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


        option1_button = ctk.CTkButton(self, text="Incepe joc nou", command=lambda: [self.sounds(1),self.incepe_jocul()],font=("Ariel",14,'bold'))
        option1_button.grid(row=1, column=0, padx=0, pady=0)
        option1_button = ctk.CTkButton(self, text="Continua joc", command=lambda: [self.sounds(1),self.save_game()],font=("Ariel",14,'bold'),state='active')
        option1_button.grid(row=2, column=0, padx=0, pady=10)
        option1_button = ctk.CTkButton(self, text="Optiuni", command=lambda:[self.sounds(1),self.optiuni()],font=("Ariel",14,'bold'),state='active')
        option1_button.grid(row=3, column=0, padx=0, pady=0)

        if os.path.exists("saved_game.json") and os.path.getsize("saved_game.json") > 0:
            option2_button = ctk.CTkButton(self, text="Continua joc", command=lambda:[self.sounds(1),self.load_game()], font=("Ariel", 14, 'bold'))
            option2_button.grid(row=2, column=0, padx=0, pady=0)
        else:
            option2_button = ctk.CTkButton(self, text="Continua joc", state='disabled', font=("Ariel", 14, 'bold'))
            option2_button.grid(row=2, column=0, padx=0, pady=10)
        option3_button = ctk.CTkButton(self, text="Iesire", command=lambda:[self.sounds(1),self.inchide_fereastra()],font=("Ariel",14,'bold'))
        option3_button.grid(row=4, column=0, padx=10, pady=10)

    def incepe_jocul(self):
        self.curata_ecran()
        label = ctk.CTkLabel(self, text="Alege dificultatea", font=("Century Gothic", 26,'bold'))
        label.grid(row=0, column=0, padx=0, pady=0)
        button2 = ctk.CTkButton(self, text="Easy", command=lambda: [self.sounds(1),self.dificultate(1)],fg_color='#229954',text_color='#d0d3d4',height=40,hover_color='#145a32',font=("Ariel",14,'bold'))   
        button2.grid(row=1, column=0, padx=0, pady=0)
        button3 = ctk.CTkButton(self, text="Medium", command=lambda: [self.sounds(1),self.dificultate(2)],fg_color='#b7950b',text_color='#d0d3d4',height=40,hover_color='#7d6608',font=("Ariel", 14,'bold'))
        button3.grid(row=2, column=0, padx=0, pady=(10,0))
        button4 = ctk.CTkButton(self, text="Hard", command=lambda: [self.sounds(1),self.dificultate(3)],fg_color='#b03a2e',text_color='#d0d3d4',height=40,hover_color='#641e16',font=("Ariel", 14,'bold'))
        button4.grid(row=3, column=0, padx=0, pady=10)
        button1 = ctk.CTkButton(self, text="Inapoi la meniu", command=lambda: [self.sounds(1),self.afisare_meniu()],font=("Ariel", 14,'bold'))
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
        
        button = ctk.CTkButton(self, text="Teme", command=lambda:[self.sounds(1),self.afisare_meniu()])
        button.grid(row=1, column=0, padx=0, pady=0)
        button = ctk.CTkButton(self, text="Audio", command=lambda:[self.sounds(1),self.audio()])
        button.grid(row=2, column=0, padx=0, pady=10)
        button = ctk.CTkButton(self, text="Inapoi", command=lambda:[self.sounds(1),self.afisare_meniu()])
        button.grid(row=3, column=0, padx=0, pady=0)

    ######### Extra ################
    def scor(self,dificultate):
        print(self.time_count)
        print(self.mistakes_count)
        if dificultate == 30:
            difficulty_multiplier = 2
        elif dificultate == 40:
            difficulty_multiplier = 1.5
        elif dificultate == 80:
            difficulty_multiplier = 1
        
        base_points = 1000
        mistake_weight = 100
        min_score = 1000
        scale_factor = 1000000
        if self.time_count != 0:
            scor = int(scale_factor * (base_points / (self.time_count + (self.mistakes_count * mistake_weight))) * difficulty_multiplier + min_score)
            print(scor)
        


    def start_timer(self,from_load=False):
        if not hasattr(self, 'timer_running'):
            self.timer_running = False
        if not self.timer_running:
            if from_load:
                self.timer_running = True
                self.timer()
            else:
                self.timer_running = True
                self.time_count = 0
                self.timer()

    def stop_timer(self):
        self.timer_running = False

    def timer(self):
        if not self.timer_running:
            return
        self.time_count += 1
        hours = self.time_count // 3600
        minutes = (self.time_count % 3600) // 60
        seconds = self.time_count % 60
        self.time_var.set(f"Timp: {hours:02d}:{minutes:02d}:{seconds:02d}")
        self.after(1000, self.timer)

    def audio(self):
        self.curata_ecran()
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=2)
        self.grid_rowconfigure(6, weight=1)

        label = ctk.CTkLabel(self, text="Audio", font=("Century Gothic", 20))
        label.grid(row=0, column=0, padx=0, pady=0)
        label = ctk.CTkLabel(self, text="Volum muzica", font=("Century Gothic", 12))
        label.grid(row=1, column=0, padx=0, pady=10)
        slider_music = ctk.CTkSlider(
            master=self, from_=0, to=100,command=lambda value: pygame.mixer.music.set_volume(int(value)/100),variable=self.music_slider_value
        )
        slider_music.grid(row=2, column=0, padx=0, pady=0)
        label= ctk.CTkLabel(self,text="Volum sunete",font=('Century Gothic', 12))
        label.grid(row=3,column=0,padx=0,pady=0)
        slider_sounds = ctk.CTkSlider(
            master=self, from_=0, to=100,command=lambda value: self.set_volume_sounds(int(value)/100),variable=self.sound_slider_value
        )
        slider_sounds.grid(row=4, column=0, padx=0, pady=10)
        button = ctk.CTkButton(self, text="Inapoi", command=lambda:[self.sounds(1),self.optiuni()])
        button.grid(row=5, column=0, padx=0, pady=0) 

    def set_volume_sounds(self,volume=0.5):
        global volume_sounds
        volume_sounds = volume
        pygame.mixer.Channel(0).set_volume(volume_sounds)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("button_click.mp3"))

    def sounds(self,value):
        # 1 - button click
        # 2 - positive sound
        # 3 - negative sound
        if value == 1:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("button_click.mp3"))
        if value == 2:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("positive.mp3"))
        if value == 3:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound("negative.mp3"))

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
            self.sounds(3)
            return True
        if not value.isdigit() or not (1 <= int(value) <= 9):  
            self.sounds(3)
            return False
        if int(value) != self.global_sudoku_grid[row][col]:
            self.sounds(3)
            return False
        return self.introducere_valida(entries, row, col, value)

    def introducere_valida(self, entries, row, col, value):
        value = str(value)
        for c in range(9):
            if c != col and entries[row][c].get() == value:
                self.sounds(3)
                return False
        for r in range(9):
            if r != row and entries[r][col].get() == value:
                self.sounds(3)
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if (r != row or c != col) and entries[r][c].get() == value:
                    self.sounds(3)
                    return False
        self.sounds(2) 
        return True

    def populeaza_intrari(self, entries, default_count, from_load=False, user_entries=None, defaults=None):
        self.default_entries = {}  # Track default entries
        if not from_load:
            positions = [(r, c) for r in range(9) for c in range(9)]
            rand.shuffle(positions)
            self.shuffle_positons = positions
        else:
            positions = self.shuffle_positons

        count = 0
        for r, c in positions:
            if from_load:
                if defaults and defaults[r][c] is not None:
                    value = defaults[r][c]
                    entries[r][c].delete(0, tk.END)
                    entries[r][c].insert(0, str(value))
                    entries[r][c].config(state="disable", foreground="#61aeff")  
                    self.default_entries[(r, c)] = True
                elif user_entries and user_entries[r][c] is not None:
                    entries[r][c].delete(0, tk.END)
                    entries[r][c].insert(0, str(user_entries[r][c]))
                    entries[r][c].config(state="normal", foreground="#ffa600")  
                    self.default_entries[(r, c)] = False
                else:
                    entries[r][c].delete(0, tk.END)
                    entries[r][c].config(state="normal", foreground="#ffa600") 
                    self.default_entries[(r, c)] = False
            else:
                if count < default_count:
                    value = self.global_sudoku_grid[r][c]  
                    entries[r][c].delete(0, tk.END)
                    entries[r][c].insert(0, str(value))
                    entries[r][c].config(state="disable", foreground="#61aeff")  
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
                
    def evidentiaza_culori(self, entries):
        for r, row in enumerate(entries):
            for c, entry in enumerate(row):
                if entry.get() == str(self.selected_number):
                    if self.default_entries.get((r, c), False):
                        entry.config(foreground="#61ff63")  
                    else:
                        entry.config(foreground="#61ff63")  
                else:
                    if self.default_entries.get((r, c), False):
                        entry.config(foreground="#61aeff")  
                    else:
                        entry.config(foreground="#ffa600")  

    def resetare_la_meniu(self,default_count):
        result = messagebox.askyesno("Salvare", "Doriti sa salvati progresul?",)
        if result:  
            self.save_game(default_count)  
            self.afisare_meniu()
            self.global_sudoku_grid = self.genereaza_subgridul()
            self.schimba_fundal()
        else:  
            self.time_count = 0
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
            default_count = game_state["difficulty_level"]
            self.shuffle_positons = game_state["shuffled_positions"]
            defaults = game_state.get("defaults", [[None]*9 for _ in range(9)])
            user_entries = game_state.get("user_entries", [[None]*9 for _ in range(9)])
            self.time_count = game_state.get("time", 0)

            self.creare_grila(
                default_count=default_count, 
                from_load=True, 
                user_entries=user_entries,
                defaults=defaults
            )
        except FileNotFoundError:
            print("No saved game found.")
        except Exception as e:
            print(f"Error loading game: {e}")

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
        self.after(250,self.felicitari())
        return True

    def felicitari(self):
        self.curata_ecran()

        # Create the canvas
        canvas = ctk.CTkCanvas(self, width=width, height=height,bg='#2c4875')
        canvas.pack()
        # canvas.create_rectangle(0, 0, width, height, fill="#2c4875")
        button = ctk.CTkButton(canvas, text="Inapoi la meniu",font=("Ariel",14,'bold'))
        button.place(x=width/2, y=height/2+20, anchor="center")
        
        canvas.create_text(width / 2, height / 4, text="This text is visible through the hole", font=("Arial", 22), fill="white")

        # Initialize hole coordinates
        hole_width = 0  # Start with a tiny hole
        hole_height = 0
        self.hole_x1 = (width - hole_width) / 2
        self.hole_y1 = (height - hole_height) / 2
        self.hole_x2 = self.hole_x1 + hole_width
        self.hole_y2 = self.hole_y1 + hole_height

        # Create the initial mask
        self.left_rect = canvas.create_rectangle(0, 0, self.hole_x1, height, fill="black", outline="black")  # Left side
        self.right_rect = canvas.create_rectangle(self.hole_x2, 0, width, height, fill="black", outline="black")  # Right side
        self.top_rect = canvas.create_rectangle(self.hole_x1, 0, self.hole_x2, self.hole_y1, fill="black", outline="black")  # Top side
        self.bottom_rect = canvas.create_rectangle(self.hole_x1, self.hole_y2, self.hole_x2, height, fill="black", outline="black")  # Bottom side

        # Start animation
        self.animate_zoom_in(canvas, width, height)

    def animate_zoom_in(self, canvas, width, height):
        # Update hole coordinates
        if self.hole_x1 > 0 or self.hole_y1 > 0 or self.hole_x2 <= width or self.hole_y2 <= height:
            self.hole_x1 = max(0, self.hole_x1 - 10)
            self.hole_y1 = max(0, self.hole_y1 - 10)
            self.hole_x2 = min(width, self.hole_x2 + 10)
            self.hole_y2 = min(height, self.hole_y2 + 10)

            # Update the mask rectangles
            canvas.coords(self.left_rect, 0, 0, self.hole_x1, height)
            canvas.coords(self.right_rect, self.hole_x2, 0, width, height)
            canvas.coords(self.top_rect, self.hole_x1, 0, self.hole_x2, self.hole_y1)
            canvas.coords(self.bottom_rect, self.hole_x1, self.hole_y2, self.hole_x2, height)

            # Schedule the next animation frame
            self.after(10, lambda: self.animate_zoom_in(canvas, width, height))
    
    def save_game(self, default_count):
        user_entries = [[None for _ in range(9)] for _ in range(9)]
        defaults = [[None for _ in range(9)] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if self.default_entries.get((r, c), False):
                    defaults[r][c] = self.entries[r][c].get()
                else:
                    user_entries[r][c] = self.entries[r][c].get()

        game_state = {
            "board": self.global_sudoku_grid,
            "mistakes_count": self.mistakes_count,
            "difficulty_level": default_count,
            "shuffled_positions": self.shuffle_positons,
            "defaults": defaults,
            "user_entries": user_entries,
            'time': self.time_count
        }

        with open("saved_game.json", "w") as f:
            json.dump(game_state, f)

    ########## JOCUL ############
    def creare_grila(self, default_count=50,from_load = False,user_entries = None,defaults=None):
        self.curata_ecran()
        self.config(bg='#00202e')
        if not from_load:
            self.time_count = 0
            self.start_timer()
        elif from_load:
            self.start_timer(from_load=True)
        

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
                                command= lambda: [self.sounds(1),self.resetare_la_meniu(default_count)],
                                height = 30,
                                width=100,
                                fg_color='#d74a49',
                                text_color='black',
                                font=("Ariel", 14, 'bold'),
                                hover_color='#852a2a'
                                )
        button1.grid(row=0,column=0,pady = 30,padx = 30,sticky = 'wn')
        label2 =tk.Label(self,textvariable=self.scor_var,font=('Arial',14),bg='#00202e',fg='#9dad7f')
        label2.grid(row=0,column=0,pady=80,padx=30,sticky='wn')
        label3 = tk.Label(self,textvariable=self.time_var,font=('Arial',14),bg='#00202e',fg='#9dad7f')
        label3.grid(row=0,column=0,pady=130,padx=30,sticky='wn')
        col = 0
        
        for i in range(9):
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
                command=lambda num=col+1: [self.sounds(1),self.introducere_numar(entries, num)]
            )
            button.grid(row=1, column=col, padx=17, pady=20)
            col += 1
        

        if not from_load:
            self.populeaza_intrari(entries, default_count, from_load=from_load)
        else:
            self.populeaza_intrari(entries, default_count, from_load=from_load, user_entries=user_entries, defaults=defaults) 
        self.entries = entries  
        return entries

Aplicatie = Sudoku()
Aplicatie.mainloop()