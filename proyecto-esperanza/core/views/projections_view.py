import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ProjectionsView(ctk.CTkFrame):
    def __init__(self, parent, analysis):
        super().__init__(parent, fg_color="transparent")
        self.pack(fill="both", expand=True)

        # Scrollable frame para los gráficos
        scroll_frame = ctk.CTkScrollableFrame(self)
        scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

        periods = [
            ("3 meses", 3),
            ("6 meses", 6), 
            ("1 año", 12),
            ("2 años", 24),
            ("3 años", 36)
        ]

        for text, months in periods:
            frame = ctk.CTkFrame(scroll_frame)
            frame.pack(fill="x", pady=10, padx=5)

            ctk.CTkLabel(frame, text=f"{text}:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10, pady=(5, 0))

            projection = analysis.get_projection(months)
            ctk.CTkLabel(frame, text=f"Valor proyectado: ${projection[-1]:,.2f}").pack(anchor="w", padx=10, pady=(0, 5))

            # Gráfico tipo tendencia mensual
            fig, ax = plt.subplots(figsize=(8, 2))
            ax.plot(projection, marker='o', color='#4e79a7')
            ax.set_title("Tendencia Proyectada", fontsize=10)
            ax.grid(True, linestyle='--', alpha=0.6)
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="x", padx=10)