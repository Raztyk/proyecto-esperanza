import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración básica de la ventana
        self.title("Proyecto Esperanza - Sistema de Ventas")
        self.geometry("1000x700")
        self.minsize(800, 600)
        
        # Configura el tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Barra lateral
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        
        # Contenido principal
        self.main_content = ctk.CTkFrame(self)
        self.main_content.pack(side="right", expand=True, fill="both")
        
        # Configura la barra lateral
        self.setup_sidebar()
    
    def setup_sidebar(self):
        # Logo
        logo = ctk.CTkLabel(
            self.sidebar,
            text="Proyecto Esperanza",
            font=("Arial", 18, "bold")
        )
        logo.pack(pady=20)
        
        # Botones de navegación
        buttons = [
            ("🏠 Dashboard", self.show_dashboard),
            ("📈 Ventas", self.show_sales),
            ("📊 Gráficos", self.show_charts),
            ("⚙️ Configuración", self.show_settings)
        ]
        
        for text, command in buttons:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                command=command,
                anchor="w",
                fg_color="transparent",
                hover_color="#2b2b2b"
            )
            btn.pack(fill="x", padx=10, pady=5)
    
    def show_dashboard(self):
        self.clear_content()
        ctk.CTkLabel(
            self.main_content,
            text="Dashboard Principal",
            font=("Arial", 24)
        ).pack(pady=50)
    
    def clear_content(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()