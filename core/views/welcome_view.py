import customtkinter as ctk

class WelcomeView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(
            parent,
            fg_color="#2a2d2e",  # Color de fondo
            corner_radius=10
        )
        self.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Contenido visible
        title = ctk.CTkLabel(
            self,
            text="Bienvenido al Sistema de Ventas",
            font=("Arial", 24),
            text_color="#ffffff"
        )
        title.pack(pady=40)
        
        btn = ctk.CTkButton(
            self,
            text="Comenzar",
            command=controller.show_upload,
            height=40,
            width=200,
            fg_color="#3a7ebf"
        )
        btn.pack(pady=20)