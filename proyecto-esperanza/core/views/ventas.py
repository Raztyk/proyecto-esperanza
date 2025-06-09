import customtkinter as ctk

class VentasView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        
        label = ctk.CTkLabel(self, text="Vista de Ventas", font=("Arial", 24))
        label.pack(pady=50)