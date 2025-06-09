import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ResultsView(ctk.CTkFrame):
    def __init__(self, parent, analysis):
        super().__init__(parent)
        self.analysis = analysis
        self.setup_ui()
    
    def setup_ui(self):
        # Pestañas
        self.tabs = ctk.CTkTabview(self)
        self.tabs.pack(fill="both", expand=True)
        
        # Añadir pestañas
        self.tabs.add("Resumen")
        self.tabs.add("Proyecciones")
        self.tabs.add("Consejos")
        
        # Contenido de pestañas
        self.create_summary_tab()
        self.create_projections_tab()
        self.create_tips_tab()
    
    def create_summary_tab(self):
        frame = self.tabs.tab("Resumen")
        summary = self.analysis.get_summary()
        
        ctk.CTkLabel(frame, text=f"Mejor Mes: {summary['best_month']}", font=("Arial", 16)).pack(pady=5)
        ctk.CTkLabel(frame, text=f"Peor Mes: {summary['worst_month']}", font=("Arial", 16)).pack(pady=5)
        
        # Gráfico de ventas mensuales
        fig, ax = plt.subplots(figsize=(10, 5))
        self.analysis.data.groupby('Mes')['Ventas'].sum().plot(kind='bar', ax=ax)
        ax.set_title("Ventas por Mes")
        
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)