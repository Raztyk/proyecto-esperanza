from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt

class ReportExporter:
    @staticmethod
    def to_pdf(data, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Título
        pdf.cell(200, 10, txt="Reporte de Ventas", ln=1, align='C')
        
        # Datos
        pdf.cell(200, 10, txt=f"Total Ventas: ${data['total_sales']:,.2f}", ln=1)
        
        # Gráfico
        plt.figure(figsize=(8, 4))
        data['monthly_sales'].plot(kind='bar')
        plt.title("Ventas Mensuales")
        plt.savefig('temp_chart.png')
        pdf.image('temp_chart.png', x=10, y=40, w=180)
        
        pdf.output(filename)