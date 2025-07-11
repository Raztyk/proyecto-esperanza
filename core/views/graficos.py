import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ..utils.theme import Theme
from ..utils.data import SalesData

class GraficosView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.pack(fill="both", expand=True)
        self.data = SalesData.get_monthly_sales()
        self.setup_ui()

    def setup_ui(self):
        # Puedes mostrar un gráfico por defecto o agregar botones para cambiar de gráfico
        self.create_heatmap()  # Muestra el heatmap por defecto

    def embed_graph(self, fig):
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, pady=10)

    def create_heatmap(self):
        dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
        horas = [f"{h}:00" for h in range(9, 21)]
        ventas = np.random.randint(10, 100, size=(len(horas), len(dias)))
        
        fig, ax = plt.subplots(figsize=(10, 6))
        im = ax.imshow(ventas, cmap="YlGnBu")
        ax.set_xticks(np.arange(len(dias)))
        ax.set_xticklabels(dias)
        ax.set_yticks(np.arange(len(horas)))
        ax.set_yticklabels(horas)
        ax.set_title('Ventas por Día y Hora', pad=20, color=Theme.COLORS["text"])
        cbar = ax.figure.colorbar(im, ax=ax)
        cbar.ax.set_ylabel('Ventas', rotation=-90, va="bottom", color=Theme.COLORS["text"])
        self.embed_graph(fig)

    def create_bubble_chart(self):
        fig, ax = plt.subplots(figsize=(8, 5))
        categorias = ['Electrónicos', 'Ropa', 'Alimentos', 'Hogar']
        ventas = [35, 52, 28, 19]
        margen = [12, 8, 15, 10]
        tamaño = [200, 300, 150, 100]
        colors = [
            Theme.COLORS["primary"],
            Theme.COLORS["secondary"],
            Theme.COLORS["accent"],
            Theme.COLORS["success"]
        ]
        scatter = ax.scatter(
            categorias, ventas, s=tamaño, c=colors, alpha=0.6,
            edgecolors=Theme.COLORS["text"], linewidths=1
        )
        for i, txt in enumerate(margen):
            ax.annotate(f"{txt}%", (categorias[i], ventas[i]), 
                       ha='center', va='center', 
                       color=Theme.COLORS["text"])
        ax.set_title('Ventas vs Margen', color=Theme.COLORS["text"])
        self.embed_graph(fig)

    def create_radar_chart(self):
        fig, ax = plt.subplots(figsize=(8, 5), subplot_kw=dict(polar=True))
        categorias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
        valores = [35, 40, 45, 50, 55, 60, 40]
        valores = np.concatenate((valores, [valores[0]]))
        angles = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))
        ax.plot(angles, valores, color=Theme.COLORS["primary"], linewidth=2)
        ax.fill(angles, valores, color=Theme.COLORS["primary"], alpha=0.25)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categorias, color=Theme.COLORS["text"])
        ax.set_title('Ventas por Día', color=Theme.COLORS["text"], pad=20)
        self.embed_graph(fig)