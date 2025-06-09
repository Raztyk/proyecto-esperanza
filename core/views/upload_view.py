import customtkinter as ctk
import pandas as pd
from tkinter import filedialog

class UploadView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        self.pack(fill="both", expand=True)
        
        # Frame principal
        content_frame = ctk.CTkFrame(self)
        content_frame.pack(pady=50, padx=50, fill="both", expand=True)
        
        # Título
        ctk.CTkLabel(
            content_frame, 
            text="Cargar Archivo de Ventas", 
            font=("Arial", 24)
        ).pack(pady=20)
        
        # Botones
        btn_frame = ctk.CTkFrame(content_frame)
        btn_frame.pack(pady=20)
        
        ctk.CTkButton(
            btn_frame,
            text="Seleccionar CSV",
            command=self.load_csv,
            width=200,
            height=40
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            btn_frame,
            text="Seleccionar Excel",
            command=self.load_excel,
            width=200,
            height=40
        ).pack(side="left", padx=10)
    
    def load_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filepath:
            try:
                df = pd.read_csv(filepath)
                self.controller.process_data(df)
            except Exception as e:
                print(f"Error: {e}")
    
    def load_excel(self):
        filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if filepath:
            try:
                df = pd.read_excel(filepath)
                self.controller.process_data(df)
            except Exception as e:
                print(f"Error: {e}")

    def load_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filepath:
            try:
                df = pd.read_csv(filepath)
                self.controller.process_data(df)  # Esto debe llamar a show_dashboard()
            except Exception as e:
                print(f"Error: {e}")
                # Mostrar mensaje de error en la interfaz
                error_label = ctk.CTkLabel(self, text=f"Error: {str(e)}", text_color="red")
                error_label.pack()