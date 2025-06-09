import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DashboardView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        
        # Tarjetas superiores
        self.create_cards()
        
        # Gráfico principal
        self.create_chart()
    
    def create_cards(self):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", pady=10)
        
        cards_data = [
            {"title": "Ventas Totales", "value": "$15,230", "trend": "↑ 12%"},
            {"title": "Productos", "value": "42", "trend": "↓ 3%"},
            {"title": "Mejor Mes", "value": "Mayo", "trend": "$5,210"}
        ]
        
        for data in cards_data:
            card = ctk.CTkFrame(frame, height=100)
            card.pack(side="left", expand=True, padx=5)
            
            ctk.CTkLabel(card, text=data["title"]).pack(pady=(10,0))
            ctk.CTkLabel(card, text=data["value"], font=("Arial", 24)).pack()
            ctk.CTkLabel(card, text=data["trend"]).pack(pady=(0,10))
    
    def create_chart(self):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True)
        
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Datos de ejemplo
        meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
        ventas = [1200, 1500, 1800, 2100, 5200, 3400]
        
        ax.bar(meses, ventas, color='#4e79a7')
        ax.set_title('Ventas Mensuales')
        
        # Integración con Tkinter
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)