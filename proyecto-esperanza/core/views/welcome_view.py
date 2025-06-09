import customtkinter as ctk

class WelcomeView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller
        
        # Contenido de bienvenida
        ctk.CTkLabel(
            self,
            text="Bienvenido al Sistema de Análisis de Ventas",
            font=("Arial", 24)
        ).pack(pady=50)
        
        ctk.CTkButton(
            self,
            text="Comenzar",
            command=lambda: controller.show_upload(),
            height=40,
            width=200
        ).pack()