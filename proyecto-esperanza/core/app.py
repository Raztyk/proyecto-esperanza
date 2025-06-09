import customtkinter as ctk
from .analysis import SalesAnalyzer
from .views.dashboard_view import DashboardView
from .views.welcome_view import WelcomeView

class App(ctk.CTk):
    def __init__(self):
        super().__init__()  # ¡Esta línea es crucial!
        
        # Configuración inicial de la ventana
        self.title("Proyecto Esperanza - Sistema de Ventas")
        self.geometry("1200x700")
        self.minsize(1000, 600)
        
        # Configuración del tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Contenedor principal (DEBE crearse antes de show_welcome)
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)
        
        # Datos iniciales
        self.current_data = None
        
        # Mostrar vista inicial
        self.show_welcome()
    
    def clear_main_frame(self):
        """Limpia el frame principal de forma segura"""
        if hasattr(self, 'main_frame'):
            for widget in self.main_frame.winfo_children():
                widget.destroy()
    
    def show_welcome(self):
        self.clear_main_frame()
        WelcomeView(self.main_frame, self)
    
    def process_data(self, df):
        self.current_data = SalesAnalyzer(df)
        self.show_dashboard()
    
    def show_dashboard(self):
        self.clear_main_frame()
        DashboardView(self.main_frame, self.current_data)

if __name__ == "__main__":
    app = App()
    app.mainloop()