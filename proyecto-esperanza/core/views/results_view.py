import customtkinter as ctk

class ResultsView(ctk.CTkFrame):
    def __init__(self, parent, analysis):
        super().__init__(parent, fg_color="transparent")
        self.pack(fill="both", expand=True)
        
        # Contenido de ejemplo
        ctk.CTkLabel(
            self,
            text="Análisis de Ventas Cargado Correctamente",
            font=("Arial", 20)
        ).pack(pady=50)