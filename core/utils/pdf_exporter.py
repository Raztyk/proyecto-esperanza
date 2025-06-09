from fpdf import FPDF
import matplotlib.pyplot as plt
from datetime import datetime
from ..utils.theme import Theme
import customtkinter as ctk

class PDFExporter:
    def __init__(self, data):
        self.data = data
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.setup_styles()
    
    def setup_styles(self):
        self.pdf.set_font("Arial", size=12)
        self.pdf.set_text_color(57, 62, 70)  # Similar a Theme.COLORS["text"]
    
    def add_title(self, title):
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, title, ln=True, align='C')
        self.pdf.ln(10)
    
    def add_sales_report(self, chart_path):
        self.add_title("Reporte de Ventas")
        
        # Información general
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(0, 10, f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True)
        self.pdf.cell(0, 10, f"Total Ventas: ${sum(self.data['ventas']):,}", ln=True)
        self.pdf.ln(5)
        
        # Gráfico
        self.pdf.image(chart_path, x=10, w=190)
        self.pdf.ln(10)
        
        # Tabla de datos
        self.add_table()
    
    def add_table(self):
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(95, 10, "Mes", border=1)
        self.pdf.cell(95, 10, "Ventas ($)", border=1, ln=True)
        
        self.pdf.set_font("Arial", size=10)
        for mes, venta in zip(self.data['meses'], self.data['ventas']):
            self.pdf.cell(95, 10, mes, border=1)
            self.pdf.cell(95, 10, f"${venta:,}", border=1, ln=True)
    
    def export(self, filename):
        temp_chart = "temp_chart.png"
        self.save_temp_chart(temp_chart)
        self.add_sales_report(temp_chart)
        self.pdf.output(filename)
    
    def save_temp_chart(self, path):
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(self.data['meses'], self.data['ventas'], color=Theme.COLORS["primary"])
        ax.set_title('Ventas Mensuales', color=Theme.COLORS["text"])
        fig.savefig(path, bbox_inches='tight', facecolor=Theme.COLORS["background"])
        plt.close(fig)