import customtkinter as ctk

class VentasView(ctk.CTkFrame):
    def __init__(self, parent, data=None):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        
        label = ctk.CTkLabel(self, text="Vista de Ventas", font=("Arial", 24))
        label.pack(pady=20)

        if data is not None:
            textbox = ctk.CTkTextbox(self, width=800, height=400)
            textbox.pack(pady=10)
            textbox.insert("end", data.head().to_string(index=False))
            textbox.configure(state="disabled")