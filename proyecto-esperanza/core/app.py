import customtkinter as ctk
from core.analysis import SalesAnalyzer
from core.views.welcome_view import WelcomeView
from core.views.dashboard_view import DashboardView
from core.views.dashboard_view import DashboardView
from core.views.upload_view import UploadView 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración básica de la ventana
        self.title("Proyecto Esperanza")
        self.geometry("1200x700")
        self.minsize(1000, 600)
        
        # Configuración del tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Frame principal con color de fondo explícito
        self.main_frame = ctk.CTkFrame(
            self,
            fg_color="#1e1e1e"  # Color oscuro personalizado
        )
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Mostrar vista inicial
        self.show_welcome()
    
    def clear_main_frame(self):
        """Limpia el frame principal de forma segura"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_welcome(self):
        self.clear_main_frame()
        WelcomeView(self.main_frame, self)
    
    def process_data(self, df):
        from core.views.dashboard_view import DashboardView
        self.clear_main_frame()
        self.current_data = SalesAnalyzer(df)
        DashboardView(self.main_frame, self.current_data)

    def show_upload(self):
        """Muestra la vista para subir archivos"""
        self.clear_main_frame()
        UploadView(self.main_frame, self)

if __name__ == "__main__":
    app = App()
    app.mainloop()