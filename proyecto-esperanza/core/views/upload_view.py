import customtkinter as ctk
import pandas as pd
from tkinter import filedialog

class UploadView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.setup_ui()
    
    def setup_ui(self):
        ctk.CTkLabel(self, text="Cargar Datos de Ventas", font=("Arial", 20)).pack(pady=20)
        
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=10)
        
        ctk.CTkButton(
            btn_frame,
            text="CSV",
            command=lambda: self.load_file("csv")
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            btn_frame,
            text="Excel",
            command=lambda: self.load_file("excel")
        ).pack(side="left", padx=10)
        
        self.info_label = ctk.CTkLabel(self, text="")
        self.info_label.pack(pady=10)
    
    def load_file(self, file_type):
        filetypes = (
            ("CSV files", "*.csv") if file_type == "csv" else 
            ("Excel files", "*.xlsx *.xls")
        )
        
        filepath = filedialog.askopenfilename(filetypes=[filetypes])
        if filepath:
            try:
                df = pd.read_csv(filepath) if file_type == "csv" else pd.read_excel(filepath)
                self.controller.process_data(df)
                self.info_label.configure(text=f"Archivo cargado: {filepath.split('/')[-1]}")
            except Exception as e:
                self.info_label.configure(text=f"Error: {str(e)}", text_color="red")