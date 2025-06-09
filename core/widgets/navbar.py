import customtkinter as ctk

class Navbar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=10)
        self.parent = parent
        
        self.configure(fg_color="#2e2e2e")
        self.setup_ui()
    
    def setup_ui(self):
        # Logo
        logo = ctk.CTkLabel(
            self,
            text="Proyecto Esperanza",
            font=("Arial", 18, "bold"),
            text_color="#4e79a7"
        )
        logo.pack(pady=20)
        
        # Botones de navegación
        buttons = [
            ("🏠 Dashboard", "show_dashboard"),
            ("📈 Ventas", "show_ventas"),
            ("📊 Gráficos", "show_graficos"),
            ("💡 Consejos", "show_consejos"),
            ("❓ Ayuda", "show_ayuda")
        ]
        
        for text, command in buttons:
            btn = ctk.CTkButton(
                self,
                text=text,
                command=lambda cmd=command: getattr(self.parent, cmd)(),
                corner_radius=8,
                height=40,
                anchor="w",
                fg_color="transparent",
                hover_color="#3e3e3e"
            )
            btn.pack(fill="x", padx=5, pady=2)
        
        # Botón de salir
        exit_btn = ctk.CTkButton(
            self,
            text="🚪 Salir",
            command=self.parent.quit,
            corner_radius=8,
            height=40,
            fg_color="#e15759",
            hover_color="#c04648"
        )
        exit_btn.pack(side="bottom", fill="x", padx=5, pady=20)