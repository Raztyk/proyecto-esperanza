import customtkinter as ctk
from .projections_view import ProjectionsView
from .tips_view import TipsView

from .tips_view import TipsView

class DashboardView(ctk.CTkFrame):
    def __init__(self, parent, analysis):
        # ... (código existente)
        self.tabview.add("Consejos")
        TipsView(self.tabview.tab("Consejos"), analysis)
        
class DashboardView(ctk.CTkFrame):
    def __init__(self, parent, analysis):
        super().__init__(parent, fg_color="transparent")
        self.analysis = analysis
        
        # Sistema de pestañas
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True)
        
        # Añadir pestañas
        self.tabview.add("Resumen")
        self.tabview.add("Proyecciones")
        self.tabview.add("Consejos")
        self.tabview.add("Gráficos")
        
        # Contenido de cada pestaña
        self.setup_summary_tab()
        ProjectionsView(self.tabview.tab("Proyecciones"), analysis)
        TipsView(self.tabview.tab("Consejos"), analysis)