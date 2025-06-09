import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ProjectionsView(ctk.CTkFrame):
    def __init__(self, parent, analysis):
        super().__init__(parent, fg_color="transparent")
        
        periods = [
            ("3 meses", 3),
            ("6 meses", 6), 
            ("1 año", 12),
            ("2 años", 24),
            ("3 años", 36)
        ]
        
        for text, months in periods:
            frame = ctk.CTkFrame(self)
            frame.pack(fill="x", pady=5)
            
            ctk.CTkLabel(frame, text=f"{text}:").pack(side="left")
            
            # Obtener proyección
            projection = analysis.get_projection(months)
            ctk.CTkLabel(frame, text=f"${projection:,.2f}").pack(side="right")
            
            # Gráfico lineal
            fig, ax = plt.subplots(figsize=(8, 2))
            ax.plot(projection)
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack()