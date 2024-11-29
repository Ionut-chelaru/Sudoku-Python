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

class Sudoku(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
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
        option1_button = ctk.CTkButton(self, text="Back", command=self.create_editable_grid)
        option1_button.grid(row=1, column=0, padx=0, pady=0)

    def Options(self):
        self.clear_window()
        label = ctk.CTkLabel(self, text="Change options", font=("Century Gothic", 20))
        label.grid(row=0, column=0, padx=0, pady=0)
        
        button = ctk.CTkButton(self, text="Back to Menu", command=self.show_menu)
        button.grid(row=1, column=0, padx=0, pady=0)

    def create_editable_grid(self, grid_size=9, cell_size=20):
        self.clear_window()
        entries = []  # Store Entry widgets for later access if needed
        
        # Create a frame to hold the grid and place it in the center
        frame = tk.Frame(self)
        frame.grid(row=1, column=1, padx=150, pady=10)  # Place the frame at the center of the 3x3 grid
        
        for row in range(grid_size):
            row_entries = []
            for col in range(grid_size):
                cell = tk.Entry(
                    frame,
                    justify="center",  # Center-align text
                    font=("Arial", 16),  # Adjust font size
                )
                cell.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
                row_entries.append(cell)
            entries.append(row_entries)

        # Configure rows and columns to make them resizable and square inside the frame
        for i in range(grid_size):
            frame.grid_rowconfigure(i, weight=1, minsize=cell_size)
            frame.grid_columnconfigure(i, weight=1, minsize=cell_size)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=3)  # Middle row is the largest
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)  # Middle column is the largest
        self.grid_columnconfigure(2, weight=1)
        
        print(row_entries)
        return entries

Aplicatie = Sudoku()
Aplicatie.mainloop()