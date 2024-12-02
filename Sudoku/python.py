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

height = '400'
width = '600'
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

        self.show_home_screen()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)    
        self.grid_rowconfigure(5, weight=1)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()


    ######## Home screen ############
    def show_home_screen(self):
        self.clear_window()
        Welcome_text = ctk.CTkLabel(self,text='SUDOKU',font=('Century Gothic', 40))
        Welcome_text.grid(row=0, column=0, padx=0, pady=0)

        Credits = ctk.CTkLabel(self,text='Made by: Ionut Chelaru\nPersonal project',font=('Century Gothic', 10))
        Credits.grid(row=5, column=0, padx=0, pady=0)

        menu_button = ctk.CTkButton(self, text="Enter game", command=self.show_menu,font=("Ariel",14,'bold'))
        menu_button.grid(row=1, column=0, padx=0, pady=0)
        exist_game = ctk.CTkButton(self, text="Exit game", command=self.close_window,font=("Ariel",14,'bold'))
        exist_game.grid(row=2, column=0, padx=0, pady=10)
    ########### Menu ################
    def show_menu(self):
        self.clear_window()
        Welcome_text = ctk.CTkLabel(self,text='SUDOKU',font=('Century Gothic', 40))
        Welcome_text.grid(row=0, column=0, padx=0, pady=0)


        option1_button = ctk.CTkButton(self, text="Start new game", command=self.Start_game,font=("Ariel",14,'bold'))
        option1_button.grid(row=1, column=0, padx=0, pady=0)
        option2_button = ctk.CTkButton(self, text="Options", command=self.Options,font=("Ariel",14,'bold'))
        option2_button.grid(row=2, column=0, padx=0, pady=10)
        option3_button = ctk.CTkButton(self, text="Exit", command=self.close_window,font=("Ariel",14,'bold'))
        option3_button.grid(row=3, column=0, padx=0, pady=0)

    def close_window(self):
        self.destroy()



    def Start_game(self):
        self.clear_window()
        label = ctk.CTkLabel(self, text="Choose difficuly", font=("Century Gothic", 26,'bold'))
        label.grid(row=0, column=0, padx=0, pady=0)
        button2 = ctk.CTkButton(self, text="Easy", command=lambda: self.Dificulty(1),fg_color='#229954',text_color='#d0d3d4',height=40,hover_color='#145a32',font=("Ariel",14,'bold'))   
        button2.grid(row=1, column=0, padx=0, pady=0)
        button3 = ctk.CTkButton(self, text="Medium", command=lambda: self.Dificulty(2),fg_color='#b7950b',text_color='#d0d3d4',height=40,hover_color='#7d6608',font=("Ariel", 14,'bold'))
        button3.grid(row=2, column=0, padx=0, pady=(10,0))
        button4 = ctk.CTkButton(self, text="Hard", command=lambda: self.Dificulty(3),fg_color='#b03a2e',text_color='#d0d3d4',height=40,hover_color='#641e16',font=("Ariel", 14,'bold'))
        button4.grid(row=3, column=0, padx=0, pady=10)
        button1 = ctk.CTkButton(self, text="Back to Menu", command=self.show_menu,font=("Ariel", 14,'bold'))
        button1.grid(row=4, column=0, padx=0, pady=(30,0))

    def Dificulty(self,value):
        self.clear_window()
        if value == 1:
            label = ctk.CTkLabel(self, text="Difficulty set to easy", font=("Century Gothic", 20,'bold'))
            label.grid(row=0, column=0, padx=0, pady=0)
        if value == 2:
            label = ctk.CTkLabel(self, text="Difficulty set to medium", font=("Century Gothic", 20))
            label.grid(row=0, column=0, padx=0, pady=0)
        if value == 3:
            label = ctk.CTkLabel(self, text="Difficulty set to hard", font=("Century Gothic", 20))
            label.grid(row=0, column=0, padx=0, pady=0)
        option1_button = ctk.CTkButton(self, text="Back", command=self.create_grid)
        option1_button.grid(row=1, column=0, padx=0, pady=0)

    def Options(self):
        self.clear_window()
        label = ctk.CTkLabel(self, text="Change options", font=("Century Gothic", 20))
        label.grid(row=0, column=0, padx=0, pady=0)
        
        button = ctk.CTkButton(self, text="Back to Menu", command=self.show_menu)
        button.grid(row=1, column=0, padx=0, pady=0)

    def on_entry_change(self, entry):
        if entry.get() != "":  
            entry.config(state="readonly")  
    def is_digit(self, value):
        return value == "" or value.isdigit()        

    def create_grid(self):
        self.clear_window()
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
                entry.bind("<KeyRelease>", lambda event, entry=entry: self.on_entry_change(entry))
                entry.grid(
                    row=i,
                    column=j,
                    padx=(2 if j % 3 == 0 else 1, 2 if j == 8 else 1),
                    pady=(2 if i % 3 == 0 else 1, 2 if i == 8 else 1)
                )
                
                row_entries.append(entry)
            entries.append(row_entries)

        self.grid_rowconfigure(0, weight=0)  
        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=0)  
        self.grid_columnconfigure(2, weight=0)

        return entries

Aplicatie = Sudoku()
Aplicatie.mainloop()
