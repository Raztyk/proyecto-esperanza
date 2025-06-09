import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ..utils.theme import Theme
from ..utils.data import SalesData

class GraficosView:
    def __init__(self, parent):
        self.parent = parent
        self.data = SalesData.get_monthly_sales()
        self.setup_ui()
    
    def setup_ui(self):
        # Configuración de grid
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(1, weight=1)
        
        # Controles
        control_frame = ctk.CTkFrame(self.parent, fg_color=Theme.COLORS["surface"])
        control_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        ctk.CTkLabel(control_frame, text="Tipo de Gráfico:").pack(side="left", padx=5)
        
        self.graph_type = ctk.CTkOptionMenu(
            control_frame,
            values=["Barras", "Líneas", "Pastel", "Heatmap"],
            command=self.update_graph,
            fg_color=Theme.COLORS["primary"],
            button_color=Theme.COLORS["secondary"]
        )
        self.graph_type.pack(side="left", padx=5)
        
        # Contenedor del gráfico
        self.graph_frame = ctk.CTkFrame(self.parent, fg_color=Theme.COLORS["surface"])
        self.graph_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        
        # Gráfico inicial
        self.create_bar_chart()
    
    def update_graph(self, choice):
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        if choice == "Barras":
            self.create_bar_chart()
        elif choice == "Líneas":
            self.create_line_chart()
        elif choice == "Pastel":
            self.create_pie_chart()
        elif choice == "Heatmap":
            self.create_heatmap()
    
    def create_bar_chart(self):
        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.bar(
            self.data['meses'], 
            self.data['ventas'],
            color=Theme.COLORS["primary"]
        )
        
        # Personalización
        ax.set_title('Ventas Mensuales', pad=20, color=Theme.COLORS["text"])
        ax.set_ylabel('Ventas ($)', color=Theme.COLORS["text"])
        ax.tick_params(colors=Theme.COLORS["text"])
        
        # Añadir etiquetas
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height:,}',
                    ha='center', va='bottom',
                    color=Theme.COLORS["text"])
        
        self.embed_graph(fig)
    
    def create_pie_chart(self):
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Simular datos por categoría
        categorias = ['Electrónicos', 'Ropa', 'Alimentos', 'Hogar']
        ventas = [3500, 5200, 2800, 1900]
        colors = [
            Theme.COLORS["primary"],
            Theme.COLORS["secondary"],
            Theme.COLORS["accent"],
            Theme.COLORS["success"]
        ]
        
        wedges, texts, autotexts = ax.pie(
            ventas,
            labels=categorias,
            colors=colors,
            autopct='%1.1f%%',
            startangle=90,
            textprops={'color': Theme.COLORS["text"]}
        )
        
        ax.set_title('Ventas por Categoría', pad=20, color=Theme.COLORS["text"])
        self.embed_graph(fig)
    
    def embed_graph(self, fig):
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)
        def create_heatmap(self):
    # Datos de ejemplo para heatmap
    dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    horas = [f"{h}:00" for h in range(9, 21)]
    ventas = np.random.randint(10, 100, size=(len(horas), len(dias)))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    im = ax.imshow(ventas, cmap="YlGnBu")  # Cambiar a mapa de colores pastel
    
    # Personalización
    ax.set_xticks(np.arange(len(dias)), labels=dias)
    ax.set_yticks(np.arange(len(horas)), labels=horas)
    ax.set_title('Ventas por Día y Hora', pad=20, color=Theme.COLORS["text"])
    
    # Barra de color
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('Ventas', rotation=-90, va="bottom", color=Theme.COLORS["text"])
    
    self.embed_graph(fig)
    def create_bubble_chart(self):
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Datos de ejemplo
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
    
    # Añadir etiquetas
    for i, txt in enumerate(margen):
        ax.annotate(f"{txt}%", (categorias[i], ventas[i]), 
                   ha='center', va='center', 
                   color=Theme.COLORS["text"])
    
    ax.set_title('Ventas vs Margen (Tamaño = Unidades)', color=Theme.COLORS["text"])
    self.embed_graph(fig)

def create_radar_chart(self):
    fig, ax = plt.subplots(figsize=(8, 5), subplot_kw=dict(polar=True))
    
    # Datos de ejemplo
    categorias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    valores = [35, 40, 45, 50, 55, 60, 40]
    valores = np.concatenate((valores, [valores[0]]))
    
    angles = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))
    
    ax.plot(angles, valores, color=Theme.COLORS["primary"], linewidth=2)
    ax.fill(angles, valores, color=Theme.COLORS["primary"], alpha=0.25)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categorias, color=Theme.COLORS["text"])
    ax.set_title('Ventas por Día de la Semana', color=Theme.COLORS["text"], pad=20)
    
    self.embed_graph(fig)
    def create_heatmap(self):
    # Datos de ejemplo para heatmap
    dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    horas = [f"{h}:00" for h in range(9, 21)]
    ventas = np.random.randint(10, 100, size=(len(horas), len(dias)))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    im = ax.imshow(ventas, cmap="YlGnBu")  # Cambiar a mapa de colores pastel
    
    # Personalización
    ax.set_xticks(np.arange(len(dias)), labels=dias)
    ax.set_yticks(np.arange(len(horas)), labels=horas)
    ax.set_title('Ventas por Día y Hora', pad=20, color=Theme.COLORS["text"])
    
    # Barra de color
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('Ventas', rotation=-90, va="bottom", color=Theme.COLORS["text"])
    
    self.embed_graph(fig)