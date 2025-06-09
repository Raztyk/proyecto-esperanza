import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ..widgets.cards import InfoCard

class DashboardView:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()
        
    def setup_ui(self):
        # Frame superior con resumen
        top_frame = ctk.CTkFrame(self.parent)
        top_frame.pack(fill="x", padx=10, pady=10)
        
        # Tarjetas de información
        InfoCard(top_frame, "Ventas Totales", "$15,230", "↑ 12%").grid(row=0, column=0, padx=5)
        InfoCard(top_frame, "Productos", "42", "↓ 3%").grid(row=0, column=1, padx=5)
        InfoCard(top_frame, "Mejor Mes", "Mayo", "$5,210").grid(row=0, column=2, padx=5)
        
        # Frame de gráficos
        graph_frame = ctk.CTkFrame(self.parent)
        graph_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Gráfico de ventas mensuales
        self.create_sales_chart(graph_frame)
        
        # Panel de consejos
        self.create_tips_panel(graph_frame)
    
    def create_sales_chart(self, parent):
        frame = ctk.CTkFrame(parent)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
        ventas = [1200, 1500, 1800, 2100, 5200, 3400]
        
        ax.bar(meses, ventas, color='#4e79a7')
        ax.set_title('Ventas Mensuales', color='white')
        ax.set_ylabel('Ventas ($)', color='white')
        
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def create_tips_panel(self, parent):
        frame = ctk.CTkFrame(parent)
        frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        label = ctk.CTkLabel(frame, text="📊 Consejos de Ventas", font=("Arial", 14, "bold"))
        label.pack(pady=(10, 5))
        
        tips = [
            "➤ Mayo fue tu mejor mes, considera replicar estrategias",
            "➤ Las ventas aumentan un 15% los viernes",
            "➤ Producto estrella: Camisetas (35% de ventas)",
            "➤ Horario pico: 2PM - 5PM"
        ]
        
        for tip in tips:
            ctk.CTkLabel(frame, text=tip, justify="left").pack(anchor="w", padx=10, pady=5)
        
        # Botón para predicciones
        btn = ctk.CTkButton(
            frame, 
            text="Ver Predicción Anual",
            command=self.show_prediction,
            fg_color="#59a14f",
            hover_color="#47853d"
        )
        btn.pack(pady=10)
    
    def show_prediction(self):
        # Implementar lógica de predicción
        pass
        def create_prediction_panel(self, parent):
    frame = ctk.CTkFrame(parent, fg_color=Theme.COLORS["surface"])
    frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    
    # Título
    ctk.CTkLabel(
        frame,
        text="🔮 Predicción de Ventas",
        font=("Arial", 14, "bold"),
        text_color=Theme.COLORS["text"]
    ).pack(pady=(10, 5))
    
    # Selector de predicción
    pred_type = ctk.CTkOptionMenu(
        frame,
        values=["Próximo Año", "Análisis Estacional", "Outliers"],
        fg_color=Theme.COLORS["primary"],
        button_color=Theme.COLORS["secondary"]
    )
    pred_type.pack(pady=5)
    
    # Gráfico de predicción
    self.pred_graph_frame = ctk.CTkFrame(frame, fg_color=Theme.COLORS["surface"])
    self.pred_graph_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Botón para generar
    ctk.CTkButton(
        frame,
        text="Generar Predicción",
        command=lambda: self.generate_prediction(pred_type.get()),
        fg_color=Theme.COLORS["accent"],
        hover_color=Theme.COLORS["secondary"]
    ).pack(pady=10)

def generate_prediction(self, pred_type):
    predictor = SalesPredictor(SalesData.get_monthly_sales())
    
    for widget in self.pred_graph_frame.winfo_children():
        widget.destroy()
    
    fig, ax = plt.subplots(figsize=(8, 4))
    
    if pred_type == "Próximo Año":
        predictions = predictor.predict_year()
        meses = SalesData.get_monthly_sales()['meses'] + [
            'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
            'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'
        ]
        ax.plot(meses, predictions, marker='o', color=Theme.COLORS["secondary"])
        ax.set_title("Predicción para el Próximo Año", color=Theme.COLORS["text"])
    
    # ... (otros tipos de predicción) ...
    
    canvas = FigureCanvasTkAgg(fig, master=self.pred_graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    from ..utils.pdf_exporter import PDFExporter

def add_export_button(self, parent):
    export_frame = ctk.CTkFrame(parent, fg_color="transparent")
    export_frame.pack(pady=10)
    
    ctk.CTkButton(
        export_frame,
        text="📄 Exportar a PDF",
        command=self.export_to_pdf,
        fg_color=Theme.COLORS["accent"],
        hover_color=Theme.COLORS["secondary"],
        width=150
    ).pack(side="left", padx=5)

def export_to_pdf(self):
    from tkinter import filedialog
    filepath = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        initialfile="reporte_ventas.pdf"
    )
    
    if filepath:
        exporter = PDFExporter(SalesData.get_monthly_sales())
        exporter.export(filepath)
        self.notifier.show_notification("✅ Reporte exportado con éxito", "success")